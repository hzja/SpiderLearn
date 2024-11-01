cd ../Extension/manifest_v3/
node package.js
cd ../../ElectronJS
@REM 这段代码是用Batch脚本语言编写的。Batch脚本是一种在Windows操作系统中执行任务的脚本语言。
@REM 1. `cd ../Extension/manifest_v3/`：将当前目录切换到项目根目录下的"Extension"文件夹下的"manifest_v3"文件夹。
@REM 2. `node package.js`：在"manifest_v3"文件夹下运行"package.js"文件。这个文件通常包含构建和打包项目所需的所有命令。
@REM 3. `cd ../../ElectronJS/`：将当前目录切换到项目根目录下的"ElectronJS"文件夹。

@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
@REM 这段代码是用Batch脚本语言编写的，用于设置系统管理员权限。以下是代码的详细解释：
@REM 1. `@echo off`：关闭命令行窗口的回显功能，防止输出乱码。
@REM 2. `>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"`：执行以下命令：
@REM   ```
@REM   cacls.exe "C:\Windows\system32\config\system"
@REM   ```
@REM   这条命令用于设置文件"C:\Windows\system32\config\system"的访问权限。
@REM 3. `if '%errorlevel%' NEQ '0' (`：判断命令执行的错误码是否不等于0。
@REM 4. `goto UACPrompt`：如果错误码不等于0，则跳转到`:UACPrompt`标签。
@REM 5. `else ( goto gotAdmin )`：如果错误码等于0，则跳转到`:gotAdmin`标签。
@REM 6. `:UACPrompt`：此标签表示如果命令执行失败，将跳转到此处。
@REM 7. `:gotAdmin`：此标签表示如果命令执行成功，将跳转到此处。

echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"
rmdir /s /q C:\Users\q9823\AppData\Local\Temp\electron-packager
rmdir /s /q out
npm run package
@REM 这段代码是用Batch脚本语言编写的，主要用于在Windows系统中获取管理员权限并执行一些操作。以下是代码的详细解释：
@REM 1. 首先，使用`echo`命令创建一个名为`getadmin.vbs`的临时文件，并将以下内容写入文件：
@REM   - `Set UAC = CreateObject^("Shell.Application"^)`：设置一个名为`UAC`的变量，其值为`CreateObject("Shell.Application")`，这是用于处理UAC（用户访问控制）的COM对象。
@REM   - `echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"`：向`getadmin.vbs`文件中添加以下内容：
@REM     - `UAC.ShellExecute "%~s0", "", "", "runas", 1`：使用`UAC`对象的`ShellExecute`方法执行当前脚本（即`%~s0`），参数为空，表示不执行任何操作，空字符串（""），空字符串（""），"runas"，表示以管理员身份运行。
@REM     - `1 >> "%temp%\getadmin.vbs"`：将`1`写入`getadmin.vbs`文件的末尾。
@REM 2. 执行`"%temp%\getadmin.vbs"`，即运行刚刚创建的`getadmin.vbs`文件。
@REM 3. 判断`getadmin.vbs`文件是否存在，如果存在则删除该文件。
@REM 4. 切换回当前工作目录，即`%CD%`。
@REM 5. 切换到包含`package.json`文件的目录，即`%~dp0`。
@REM 6. 删除`C:\Users\q9823\AppData\Local\Temp\electron-packager`和`out`目录。
@REM 7. 运行`npm run package`，执行打包electron应用的操作。
@REM 总之，这段代码的作用是在Windows系统中以管理员身份运行一个批处理脚本，并执行一些操作，如删除目录、运行npm命令等。