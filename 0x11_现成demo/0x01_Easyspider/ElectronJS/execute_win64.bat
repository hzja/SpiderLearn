@REM msg * %cd%
if exist EasySpider (
   start EasySpider/resources/app/chrome_win64/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
) else (
if exist resources (
   cd ../
   start EasySpider/resources/app/chrome_win64/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
  ) else (
   start chrome_win64/easyspider_executestage.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
  )
)
@REM 这段代码是用Batch脚本语言编写的，主要用于在Windows操作系统中启动EasySpider程序。以下是代码的详细解释：
@REM 1. 首先，代码检查当前目录下是否存在名为"EasySpider"的文件夹。如果存在，则执行以下操作：
@REM 2. 然后，代码检查"EasySpider"文件夹下是否存在名为"resources"的文件夹。如果存在，则将工作目录切换到"EasySpider/resources"文件夹，并执行以下操作：
@REM 3. 接下来，代码检查"resources"文件夹下是否存在名为"app/chrome_win64"的文件夹。如果存在，则在该文件夹下查找名为"easyspider_executestage.exe"的可执行文件，并将其作为命令行参数传递给该文件，同时传递传递给该文件的参数%1到%9。
@REM 4. 如果"resources"文件夹不存在，则执行以下操作：
@REM 5. 最后，代码在当前目录下查找名为"chrome_win64"的文件夹。如果存在，则在该文件夹下查找名为"easyspider_executestage.exe"的可执行文件，并将其作为命令行参数传递给该文件，同时传递给该文件的参数%1到%9。
@REM 总之，这段代码的作用是在Windows操作系统中启动EasySpider程序，并根据是否存在"resources"文件夹来决定是使用默认的"chrome_win64"文件夹还是"EasySpider/resources/app/chrome_win64"文件夹。