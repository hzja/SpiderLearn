#!/bin/bash

# This script is used to build.md the package for MacOS.
cd ../Extension/manifest_v3/
node package.js
cd ../../ElectronJS
rm -rf out
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app
npm run make
unzip out/make/zip/darwin/*64/EasySpider-darwin* -d ../.temp_to_pub/EasySpider_MacOS_all_arch/
# 这段代码的主要功能如下：
# 1. 切换到父目录下的 "Extension" 文件夹下的 "manifest_v3" 文件夹。
# 2. 运行 "package.js" 文件，这个文件可能与 Electron 项目的构建和发布有关。
# 3. 切换回父目录下的 "ElectronJS" 文件夹。
# 4. 删除 "out" 文件夹。
# 5. 删除父目录下的 ".temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app" 文件夹。
# 6. 运行 "npm run make" 命令，这个命令可能用于构建和发布 Electron 项目。
# 7. 解压缩 "out/make/zip/darwin/*64/EasySpider-darwin*" 文件夹到父目录下的 ".temp_to_pub/EasySpider_MacOS_all_arch/" 文件夹。

# mv out/EasySpider-darwin-*64/EasySpider.app ../.temp_to_pub/EasySpider_MacOS_all_arch/
rm ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/VS_BuildTools.exe
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chrome_win64
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chromedrivers
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/Data
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/.idea
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/tasks
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/execution_instances
rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/user_data
rm -rf ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
# 这段代码是用Shell脚本语言编写的，用于删除指定目录下的文件或文件夹。
# 1. `rm ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/VS_BuildTools.exe`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/VS_BuildTools.exe`文件。
# 2. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chrome_win64`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chrome_win64`文件夹及其内容。
# 3. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chromedrivers`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/chromedrivers`文件夹及其内容。
# 4. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/Data`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/Data`文件夹及其内容。
# 5. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/.idea`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/.idea`文件夹及其内容。
# 6. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/tasks`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/tasks`文件夹及其内容。
# 7. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/execution_instances`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/execution_instances`文件夹及其内容。
# 8. `rm -r ../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/user_data`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/EasySpider.app/Contents/Resources/app/user_data`文件夹及其内容。
# 9. `rm -rf ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：删除`../.temp_to_pub/EasySpider_MacOS_all_arch/Code`文件夹及其内容。

mkdir ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/easyspider_executestage.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/myChrome.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/utils.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/requirements.txt ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/Readme.md ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp ../ExecuteStage/myCode.py ../.temp_to_pub/EasySpider_MacOS_all_arch
cp -Rf ../ExecuteStage/undetected_chromedriver_ES ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
cp -Rf ../ExecuteStage/.vscode ../.temp_to_pub/EasySpider_MacOS_all_arch/Code
# 这段代码是用Shell脚本语言编写的，用于创建目录、复制文件到目录和复制文件夹到目录。以下是代码的详细解释：
# 1. `mkdir ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：创建一个名为“Code”的目录，其父目录为“../.temp_to_pub/EasySpider_MacOS_all_arch”。
# 2. `cp ../ExecuteStage/easyspider_executestage.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/easyspider_executestage.py”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 3. `cp ../ExecuteStage/myChrome.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/myChrome.py”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 4. `cp ../ExecuteStage/utils.py ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecteStage/utils.py”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 5. `cp ../ExecuteStage/requirements.txt ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/requirements.txt”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 6. `cp ../ExecuteStage/Readme.md ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/Readme.md”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 7. `cp ../ExecuteStage/myCode.py ../.temp_to_pub/EasySpider_MacOS_all_arch`：将“../ExecuteStage/myCode.py”文件复制到“../.temp_to_pub/EasySpider_MacOS_all_arch”目录。
# 8. `cp -Rf ../ExecuteStage/undetected_chromedriver_ES ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/undetected_chromedriver_ES”文件夹（包括其所有子文件和子目录）复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。
# 9. `cp -Rf ../ExecuteStage/.vscode ../.temp_to_pub/EasySpider_MacOS_all_arch/Code`：将“../ExecuteStage/.vscode”文件夹（包括其所有子文件和子目录）复制到“../.temp_to_pub/EasySpider_MacOS_all_arch/Code”目录。