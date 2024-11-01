#!/bin/bash

# This script is used to build.md the package for Linux 64-bit.
rm -r out
cd ../Extension/manifest_v3
node package.js
cd ../../ElectronJS
npm run package
mv out/EasySpider-linux-x64 out/EasySpider
# 这段代码是用Shell脚本语言编写的，用于在Linux操作系统上执行一些命令。以下是对这段代码的解释：
# 1. `rm -r out`：删除名为"out"的文件夹（包括其中的所有文件和子文件夹）。
# 2. `cd ../Extension/manifest_v3`：切换到父目录下的"Extension"文件夹，然后进入到"manifest_v3"文件夹。
# 3. `node package.js`：在当前目录下运行"package.js"文件，这通常是一个包含构建和打包命令的Node.js脚本。
# 4. `cd ../../ElectronJS`：切换到父目录下的"ElectronJS"文件夹。
# 5. `npm run package`：在"ElectronJS"文件夹中运行"package"命令，这通常是一个构建和打包命令，用于构建Electron应用程序。
# 6. `mv out/EasySpider-linux-x64 out/EasySpider`：将名为"EasySpider-linux-x64"的文件夹从"out"文件夹移动到"EasySpider"文件夹。

rm -rf out/EasySpider/resources/app/chrome_win64
rm -rf out/EasySpider/resources/app/chromedrivers
rm -rf out/EasySpider/resources/app/Data
rm -rf out/EasySpider/resources/app/.idea
rm -rf out/EasySpider/resources/app/tasks
rm -rf out/EasySpider/resources/app/execution_instances
rm -rf out/EasySpider/resources/app/user_data
rm -rf ../.temp_to_pub/EasySpider_Linux_x64/EasySpider
rm out/EasySpider/resources/app/vs_BuildTools.exe
mv out/EasySpider ../.temp_to_pub/EasySpider_Linux_x64/EasySpider
rm -rf ../.temp_to_pub/EasySpider_Linux_x64/Code
mkdir ../.temp_to_pub/EasySpider_Linux_x64/Code
# 这段代码是用Shell脚本语言编写的，用于在Linux系统上清理EasySpider项目中的某些文件和文件夹。以下是代码的逐行解释：
# 1. `rm -rf out/EasySpider/resources/app/chrome_win64`：删除out/EasySpider/resources/app/chrome_win64文件夹及其内容。
# 2. `rm -rf out/EasySpider/resources/app/chromedrivers`：删除out/EasySpider/resources/app/chromedrivers文件夹及其内容。
# 3. `rm -rf out/EasySpider/resources/app/Data`：删除out/EasySpider/resources/app/Data文件夹及其内容。
# 4. `rm -rf out/EasySpider/resources/app/.idea`：删除out/EasySpider/resources/app/.idea文件夹及其内容。
# 5. `rm -rf out/EasySpider/resources/app/tasks`：删除out/EasySpider/resources/app/tasks文件夹及其内容。
# 6. `rm -rf out/EasySpider/resources/app/execution_instances`：删除out/EasySpider/resources/app/execution_instances文件夹及其内容。
# 7. `rm -rf out/EasySpider/resources/app/user_data`：删除out/EasySpider/resources/app/user_data文件夹及其内容。
# 8. `rm out/EasySpider/resources/app/vs_BuildTools.exe`：删除out/EasySpider/resources/app/vs_BuildTools.exe文件。
# 9. `mv out/EasySpider ../.temp_to_pub/EasySpider_Linux_x64/EasySpider`：将out/EasySpider文件夹移动到../.temp_to_pub/EasySpider_Linux_x64/EasySpider文件夹。
# 10. `rm -rf ../.temp_to_pub/EasySpider_Linux_x64/EasySpider/Code`：删除../.temp_to_pub/EasySpider_Linux_x64/EasySpider/Code文件夹及其内容。
# 11. `mkdir ../.temp_to_pub/EasySpider_Linux_x64/EasySpider/Code`：在../.temp_to_pub/EasySpider_Linux_x64/EasySpider/Code目录下创建一个空目录。

cp ../ExecuteStage/easyspider_executestage.py ../.temp_to_pub/EasySpider_Linux_x64/Code
cp ../ExecuteStage/myChrome.py ../.temp_to_pub/EasySpider_Linux_x64/Code
cp ../ExecuteStage/utils.py ../.temp_to_pub/EasySpider_Linux_x64/Code
cp ../ExecuteStage/requirements.txt ../.temp_to_pub/EasySpider_Linux_x64/Code
cp ../ExecuteStage/Readme.md ../.temp_to_pub/EasySpider_Linux_x64/Code
cp ../ExecuteStage/myCode.py ../.temp_to_pub/EasySpider_Linux_x64
cp -Rf ../ExecuteStage/undetected_chromedriver_ES ../.temp_to_pub/EasySpider_Linux_x64/Code
cp -Rf ../ExecuteStage/.vscode ../.temp_to_pub/EasySpider_Linux_x64/Code
chmod 777 ../.temp_to_pub/EasySpider_Linux_x64/easy-spider.sh
# 这段代码的主要功能是将一些文件从当前目录（即`../ExecuteStage`）复制到另一个目录（即`../.temp_to_pub/EasySpider_Linux_x64`）。
# 1. 复制`easyspider_executestage.py`到目标目录的`Code`文件夹。
# 2. 复制`myChrome.py`到目标目录的`Code`文件夹。
# 3. 复制`utils.py`到目标目录的`Code`文件夹。
# 4. 复制`requirements.txt`到目标目录的`Code`文件夹。
# 5. 复制`Readme.md`到目标目录的`Code`文件夹。
# 6. 复制`myCode.py`到目标目录的`EasySpider_Linux_x64`目录。
# 7. 将`undetected_chromedriver_ES`文件夹复制到目标目录的`Code`文件夹。
# 8. 将`.vscode`文件夹复制到目标目录的`Code`文件夹。
# 9. 为目标目录的`easy-spider.sh`文件设置权限为777。

rm -rf ../.temp_to_pub/EasySpider_Linux_x64/user_data
rm -rf  ../.temp_to_pub/EasySpider_Linux_x64/execution_instances
mkdir ../.temp_to_pub/EasySpider_Linux_x64/execution_instances
rm -rf  ../.temp_to_pub/EasySpider_Linux_x64/Data
mkdir ../.temp_to_pub/EasySpider_Linux_x64/Data
rm EasySpider_zh.crx
rm EasySpider_en.crx
# 这段代码的主要功能是清理当前目录下的某些文件和文件夹。
# 1. 删除`../.temp_to_pub/EasySpider_Linux_x64/user_data`和`../.temp_to_pub/EasySpider_Linux_x64/execution_instances`文件夹。
# 2. 创建`../.temp_to_pub/EasySpider_Linux_x64/execution_instances`空文件夹。
# 3. 删除`../.temp_to_pub/EasySpider_Linux_x64/Data`文件夹。
# 4. 创建`../.temp_to_pub/EasySpider_Linux_x64/Data`空文件夹。
# 5. 删除`EasySpider_zh.crx`和`EasySpider_en.crx`文件。