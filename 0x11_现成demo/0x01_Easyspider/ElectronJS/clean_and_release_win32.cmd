move out\EasySpider-win32-ia32 out\EasySpider
rmdir /s /q out\EasySpider\resources\app\chrome_win64
rmdir /s /q out\EasySpider\resources\app\chromedrivers
rmdir /s /q out\EasySpider\resources\app\Data
rmdir /s /q out\EasySpider\resources\app\.idea
rmdir /s /q out\EasySpider\resources\app\tasks
rmdir /s /q out\EasySpider\resources\app\execution_instances
rmdir /s /q out\EasySpider\resources\app\user_data
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\EasySpider
del out\EasySpider\resources\app\vs_BuildTools.exe
move out\EasySpider ..\.temp_to_pub\EasySpider_windows_x32\EasySpider
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\Code
mkdir ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\easyspider_executestage.py ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\myChrome.py ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\utils.py ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\requirements.txt ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\Readme.md ..\.temp_to_pub\EasySpider_windows_x32\Code
copy ..\ExecuteStage\myCode.py ..\.temp_to_pub\EasySpider_windows_x32
xcopy ..\ExecuteStage\undetected_chromedriver_ES ..\.temp_to_pub\EasySpider_windows_x32\Code\undetected_chromedriver_ES /E /I /Y
xcopy ..\ExecuteStage\.vscode ..\.temp_to_pub\EasySpider_windows_x32\Code\.vscode /E /I /Y
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\user_data
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\execution_instances
mkdir ..\.temp_to_pub\EasySpider_windows_x32\execution_instances
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\Data
mkdir ..\.temp_to_pub\EasySpider_windows_x32\Data
del EasySpider_en.crx
del EasySpider_zh.crx

@REM 这段代码主要用于将EasySpider项目从一个文件夹移动到另一个文件夹，并删除或保留某些文件和文件夹。以下是代码的详细解释：
@REM  `move out\EasySpider-win32-ia32 out\EasySpider`：将`out\EasySpider-win32-ia32`文件夹移动到`out\EasySpider`文件夹。
@REM  `rmdir /s /q out\EasySpider\resources\app\chrome_win64`：删除`out\EasySpider\resources\app\chrome_win64`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\chromedrivers`：删除`out\EasySpider\resources\app\chromedrivers`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\Data`：删除`out\EasySpider\resources\app\Data`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\.idea`：删除`out\EasySpider\resources\app\.idea`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\tasks`：删除`out\EasySpider\resources\app\tasks`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\execution_instances`：删除`out\EasySpider\resources\app\execution_instances`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q out\EasySpider\resources\app\user_data`：删除`out\EasySpider\resources\app\user_data`文件夹及其子文件夹和文件。
@REM  `rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\EasySpider`：删除`..\.temp_to_pub\EasySpider_windows_x32\EasySpider`文件夹及其子文件夹和文件。
@REM  `del out\EasySpider\resources\app\vs_BuildTools.exe`：删除`out\EasySpider\resources\app\vs_BuildTools.exe`文件。
@REM  `move out\EasySpider ..\.temp_to_pub\EasySpider_windows_x32\EasySpider`：将`out\EasySpider`文件夹移动到`..\.temp_to_pub\EasySpider_windows_x32\EasySpider`文件夹。
@REM  `rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\Code`：删除`..\.temp_to_pub\EasySpider_windows_x32\Code`文件夹及其子文件夹和文件。
@REM  `mkdir ..\.temp_to_pub\EasySpider_windows_x32\Code`：创建`..\.temp_to_pub\EasySpider_windows_x32\Code`文件夹。
@REM  `copy ..\ExecuteStage\easyspider_executestage.py ..\.temp_to_pub\EasySpider_windows_x32\Code`：将`..\ExecuteStage\easyspider_executestage.py`文件复制到`..\.temp_to_pub\EasySpider_windows_x32\Code`文件夹。
@REM  `copy ..\ExecuteStage\myChrome.py ..\.temp_to_pub\EasySpider_windows_x32\Code`：将`..\ExecuteStage\myChrome.py`文件复制到`..\.temp_to_pub\EasySpider_windows_x32\Code`文件夹。
@REM copy ..\ExecuteStage\utils.py ..\.temp_to_pub\EasySpider_windows_x32\Code：将utils.py文件从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32\Code文件夹。
@REM copy ..\ExecuteStage\requirements.txt ..\.temp_to_pub\EasySpider_windows_x32\Code：将requirements.txt文件从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32\Code文件夹。
@REM copy ..\ExecuteStage\Readme.md ..\.temp_to_pub\EasySpider_windows_x32\Code：将Readme.md文件从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32\Code文件夹。
@REM copy ..\ExecuteStage\myCode.py ..\.temp_to_pub\EasySpider_windows_x32：将myCode.py文件从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32文件夹。
@REM xcopy ..\ExecuteStage\undetected_chromedriver_ES ..\.temp_to_pub\EasySpider_windows_x32\Code\undetected_chromedriver_ES /E /I /Y：将undetected_chromedriver_ES文件夹从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32\Code\undetected_chromedriver_ES文件夹，采用递归复制模式（/E），覆盖已存在的文件（/Y），保持文件夹结构（/I）。
@REM xcopy ..\ExecuteStage\.vscode ..\.temp_to_pub\EasySpider_windows_x32\Code\.vscode /E /I /Y：将.vscode文件夹从..\ExecuteStage文件夹复制到..\.temp_to_pub\EasySpider_windows_x32\Code\.vscode文件夹，采用递归复制模式（/E），覆盖已存在的文件（/Y），保持文件夹结构（/I）。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\user_data：删除..\.temp_to_pub\EasySpider_windows_x32\user_data文件夹及其子文件夹和文件。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\execution_instances：删除..\.temp_to_pub\EasySpider_windows_x32\execution_instances文件夹及其子文件夹和文件。
@REM mkdir ..\.temp_to_pub\EasySpider_windows_x32\execution_instances：创建..\.temp_to_pub\EasySpider_windows_x32\execution_instances文件夹。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x32\Data：删除..\.temp_to_pub\EasySpider_windows_x32\Data文件夹及其子文件夹和文件。
@REM mkdir ..\.temp_to_pub\EasySpider_windows_x32\Data：创建..\.temp_to_pub\EasySpider_windows_x32\Data文件夹。
@REM del EasySpider_en.crx：删除EasySpider_en.crx