@REM msg * %cd%
if exist EasySpider (
   start EasySpider/resources/app/chrome_win32/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
) else (
if exist resources (
   cd ../
   start EasySpider/resources/app/chrome_win32/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
  ) else (
   start chrome_win64/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
  )
)
@REM 这段代码是用于判断EasySpider的可执行文件是否存在于指定的目录中，并根据结果执行相应的操作。以下是代码的详细解释：
@REM 1. 首先，代码使用`if exist EasySpider`语句检查EasySpider可执行文件是否存在。如果文件存在，则继续执行下面的操作；否则，执行`else`语句中的内容。
@REM 2. `else`语句中，代码使用`if exist resources`语句检查`resources`文件夹是否存在。如果文件夹存在，则进入该文件夹；否则，执行下面的操作。
@REM 3. 如果在`resources`文件夹中，代码会切换到上一级目录，然后执行`start EasySpider/resources/app/chrome_win32/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9`命令。这个命令会启动EasySpider的可执行文件，并传递参数%1、%2、%3等。
@REM 4. 如果在`resources`文件夹不存在，代码会直接执行`start chrome_win64/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9`命令。这个命令会启动EasySpider的可执行文件，并传递参数%1、%2、%3等。
@REM 总之，这段代码的作用是检查EasySpider的可执行文件是否存在于指定的目录中，并根据结果执行相应的操作。