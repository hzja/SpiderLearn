cd ../Extension/manifest_v3/
node package.js
cd ../../ElectronJS
rmdir /s /q out
npm run package
@REM 这段代码是用Batch脚本编写的。以下是代码的逐行解释：
@REM 1. `cd ../Extension/manifest_v3/`：将当前工作目录切换到项目根目录下的"Extension"文件夹下的"manifest_v3"文件夹。
@REM 2. `node package.js`：运行"manifest_v3"文件夹下的"package.js"文件，这个文件可能包含了项目的构建和打包命令。
@REM 3. `cd ../../ElectronJS`：将当前工作目录切换到项目根目录下的"ElectronJS"文件夹。
@REM 4. `rmdir /s /q out`：删除"ElectronJS"文件夹下的"out"文件夹，参数"/s"表示删除子文件夹及其内容，参数"/q"表示静默模式，不显示提示信息。
@REM 5. `npm run package`：运行npm脚本"package"，这个脚本可能包含了项目的打包命令。