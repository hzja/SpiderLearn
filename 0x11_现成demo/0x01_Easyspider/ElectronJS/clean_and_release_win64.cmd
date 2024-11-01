move out\EasySpider-win32-x64 out\EasySpider
rmdir /s /q out\EasySpider\resources\app\chrome_win32
rmdir /s /q out\EasySpider\resources\app\chromedrivers
rmdir /s /q out\EasySpider\resources\app\Data
rmdir /s /q out\EasySpider\resources\app\.idea
rmdir /s /q out\EasySpider\resources\app\tasks
rmdir /s /q out\EasySpider\resources\app\execution_instances
rmdir /s /q out\EasySpider\resources\app\user_data
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\EasySpider
del out\EasySpider\resources\app\vs_BuildTools.exe
move out\EasySpider ..\.temp_to_pub\EasySpider_windows_x64\EasySpider
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\Code
mkdir ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\easyspider_executestage.py ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\myChrome.py ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\utils.py ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\requirements.txt ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\Readme.md ..\.temp_to_pub\EasySpider_windows_x64\Code
copy ..\ExecuteStage\myCode.py ..\.temp_to_pub\EasySpider_windows_x64
xcopy ..\ExecuteStage\undetected_chromedriver_ES ..\.temp_to_pub\EasySpider_windows_x64\Code\undetected_chromedriver_ES /E /I /Y
xcopy ..\ExecuteStage\.vscode ..\.temp_to_pub\EasySpider_windows_x64\Code\.vscode /E /I /Y
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\user_data
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\execution_instances
mkdir ..\.temp_to_pub\EasySpider_windows_x64\execution_instances
rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\Data
mkdir ..\.temp_to_pub\EasySpider_windows_x64\Data

@REM move out\EasySpider-win32-x64 out\EasySpider：将名为out\EasySpider-win32-x64的文件夹移动到名为out\EasySpider的文件夹。
@REM rmdir /s /q out\EasySpider\resources\app\chrome_win32：删除名为out\EasySpider\resources\app\chrome_win32的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\chromedrivers：删除名为out\EasySpider\resources\app\chromedrivers的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\Data：删除名为out\EasySpider\resources\app\Data的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\.idea：删除名为out\EasySpider\resources\app\.idea的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\tasks：删除名为out\EasySpider\resources\app\tasks的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\execution_instances：删除名为out\EasySpider\resources\app\execution_instances的文件夹及其内容。
@REM rmdir /s /q out\EasySpider\resources\app\user_data：删除名为out\EasySpider\resources\app\user_data的文件夹及其内容。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\EasySpider：删除名为..\.temp_to_pub\EasySpider_windows_x64\EasySpider的文件夹及其内容。
@REM del out\EasySpider\resources\app\vs_BuildTools.exe：删除名为out\EasySpider\resources\app\vs_BuildTools.exe的文件。
@REM move out\EasySpider ..\.temp_to_pub\EasySpider_windows_x64\EasySpider：将名为out\EasySpider的文件夹移动到名为..\.temp_to_pub\EasySpider_windows_x64\EasySpider的文件夹。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\Code：删除名为..\.temp_to_pub\EasySpider_windows_x64\Code的文件夹及其内容。
@REM mkdir ..\.temp_to_pub\EasySpider_windows_x64\Code：创建名为..\.temp_to_pub\EasySpider_windows_x64\Code的文件夹。
@REM copy ..\ExecuteStage\easyspider_executestage.py ..\.temp_to_pub\EasySpider_windows_x64\Code：将..\ExecuteStage\easyspider_executestage.py文件复制到名为..\.temp_to_pub\EasySpider_windows_x64\Code的文件夹中。
@REM copy ..\ExecuteStage\myChrome.py ..\.temp_to_pub\EasySpider_windows_x64\Code：将..\ExecuteStage\myChrome.py文件复制到名为..\.temp_to_pub\EasySpider_windows_x64\Code的文件夹中。
@REM copy ..\ExecuteStage\utils.py ..\.temp_to_pub\EasySpider_windows_x64\Code：将项目文件夹中的utils.py文件复制到目标文件夹.temp_to_pub\EasySpider_windows_x64\Code中。
@REM copy ..\ExecuteStage\requirements.txt ..\.temp_to_pub\EasySpider_windows_x64\Code：将项目文件夹中的requirements.txt文件复制到目标文件夹.temp_to_pub\EasySpider_windows_x64\Code中。
@REM copy ..\ExecuteStage\Readme.md ..\.temp_to_pub\EasySpider_windows_x64\Code：将项目文件夹中的Readme.md文件复制到目标文件夹.temp_to_pub\EasySpider_windows_x64\Code中。
@REM copy ..\ExecuteStage\myCode.py ..\.temp_to_pub\EasySpider_windows_x64：将项目文件夹中的myCode.py文件复制到目标文件夹.temp_to_pub\EasySpider_windows_x64中。
@REM xcopy ..\ExecuteStage\undetected_chromedriver_ES ..\.temp_to_pub\EasySpider_windows_x64\Code\undetected_chromedriver_ES /E /I /Y：使用xcopy命令将项目文件夹中的undetected_chromedriver_ES文件夹复制到目标文件夹.temp_to_pub\EasySpider_windows_x64\Code\undetected_chromedriver_ES中，并保留文件夹结构。
@REM xcopy ..\ExecuteStage\.vscode ..\.temp_to_pub\EasySpider_windows_x64\Code\.vscode /E /I /Y：使用xcopy命令将项目文件夹中的.vscode文件夹复制到目标文件夹.temp_to_pub\EasySpider_windows_x64\Code\.vscode中，并保留文件夹结构。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\user_data：删除目标文件夹.temp_to_pub\EasySpider_windows_x64\user_data中的所有文件和子文件夹。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\execution_instances：删除目标文件夹.temp_to_pub\EasySpider_windows_x64\execution_instances中的所有文件和子文件夹。
@REM mkdir ..\.temp_to_pub\EasySpider_windows_x64\execution_instances：在目标文件夹.temp_to_pub\EasySpider_windows_x64中创建一个名为execution_instances的子文件夹。
@REM rmdir /s /q ..\.temp_to_pub\EasySpider_windows_x64\Data：删除目标文件夹.temp_to_pub\EasySpider_windows_x64\Data中的所有文件和子文件夹。
@REM mkdir ..\.temp_to_pub\EasySpider_windows_x64\Data：在目标文件夹.temp_to_pub\EasySpider_windows_x64中创建一个名为Data的子文件夹。