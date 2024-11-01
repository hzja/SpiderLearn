import json
import os
import re
import subprocess
import sys
import requests
import platform
import shutil
import zipfile
import urllib.request
if sys.platform == "win32":
    import winreg
import re

def get_processor_info():
    if os.uname().sysname == 'Darwin':
        processor_info = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).strip()
        processor_info = str(processor_info)
        if 'Intel' in processor_info:
            return 'Intel'
        elif 'Apple' in processor_info:
            return 'Apple'
        else:
            return 'Unknown'
    else:
        return 'This method is only implemented for macOS.'
#    这段代码定义了一个名为`get_processor_info`的函数，用于获取操作系统的处理器信息。函数首先检查当前操作系统是否为macOS（通过检查`os.uname().sysname`的值）。如果是macOS，则使用`subprocess.check_output`函数调用`sysctl`命令来获取`machdep.cpu.brand_string`的值，并将其转换为字符串类型。然后，函数检查处理器信息中是否包含"Intel"或"Apple"，根据这些条件返回相应的处理器类型（'Intel'或'Apple'）或'Unknown'。如果不是macOS，函数返回一条消息，指示此方法仅适用于macOS。 

def download_and_extract_zip(url, destination_folder):
    # 下载ZIP文件
    urllib.request.urlretrieve(url, "temp.zip")

    # 解压ZIP文件
    with zipfile.ZipFile("temp.zip", "r") as zip_ref:
        zip_ref.extractall(destination_folder)

    # 删除临时ZIP文件
    os.remove("temp.zip")
# 这段代码是用Python编写的，定义了一个名为`download_and_extract_zip`的函数，用于下载并解压一个ZIP文件。
# 1. 首先，导入了`urllib.request`和`zipfile`两个模块。
# 2. 定义了一个名为`download_and_extract_zip`的函数，接受两个参数：`url`和`destination_folder`。`url`是ZIP文件的下载链接，`destination_folder`是ZIP文件解压后的目标文件夹。
# 3. 定义了一个名为`temp.zip`的临时文件，用于存储下载的ZIP文件。使用`urllib.request.urlretrieve(url, "temp.zip")`将ZIP文件下载到该文件中。
# 4. 定义了一个`with`语句，用于打开ZIP文件。使用`zipfile.ZipFile("temp.zip", "r") as zip_ref`创建一个`ZipFile`对象，并指定`"r"`参数表示以只读模式打开ZIP文件。
# 5. 使用`zip_ref.extractall(destination_folder)`将ZIP文件解压到指定的文件夹中。
# 6. 最后，使用`os.remove("temp.zip")`删除临时ZIP文件。

def copy_file(source_file, destination_file):
    # 使用copy2()函数复制文件
    shutil.copy2(source_file, destination_file)
# 这段代码定义了一个名为`copy_file`的函数，它接受两个参数`source_file`和`destination_file`，分别表示要复制的源文件路径和目标文件路径。函数内部使用`shutil.copy2()`函数将源文件复制到目标文件，这是一个用于复制文件的高级函数，可以保留文件的元数据（如权限、时间戳等）。

def copy_folder(source_folder, destination_folder):
    # 使用copytree()函数复制文件夹及其内容
    shutil.copytree(source_folder, destination_folder)
# 这段代码定义了一个名为`copy_folder`的函数，它接受两个参数`source_folder`和`destination_folder`。这个函数的功能是使用`shutil.copytree()`函数复制一个文件夹及其内容，从`source_folder`到`destination_folder`。

def get_chrome_version():
    version = "120"
    if sys.platform == "win32":
        version_re = re.compile(r"^[1-9]\d*\.\d*.\d*")
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon"
            )
            _v, type = winreg.QueryValueEx(key, "version")
            return version_re.findall(_v)[0][:3]
        except WindowsError as e:
            print("check Chrome failed:{}".format(e))
    else:
        return version
# 这段代码定义了一个名为`get_chrome_version`的函数，用于获取Chrome浏览器的版本信息。以下是代码的详细解释：

# 1. 定义一个名为`version`的变量，初始值为"120"。
# 2. 定义一个名为`version_re`的变量，使用正则表达式创建一个匹配Chrome版本号的编译器对象。
# 3. 判断系统平台是否为Windows，如果是，则执行以下操作：
#   a. 定义一个名为`key`的变量，使用`winreg.OpenKey`方法打开`HKEY_CURRENT_USER`下的`Software\Google\Chrome\BLBeacon`键。
#   b. 定义一个名为`_v`的变量，使用`winreg.QueryValueEx`方法查询键的值。
#   c. 定义一个名为`type`的变量，用于存储键值的类型。
#   d. 使用`winreg.QueryValueEx`方法查询键的值，并将其存储在`_v`变量中。
#   e. 定义一个名为`version_str`的变量，初始值为`_v`。
#   f. 使用`version_re.findall`方法在`version_str`中查找所有匹配的版本号，并将结果存储在`version_list`中。
#   g. 定义一个名为`version_str`的变量，初始值为`version_list[0]`。
#   h. 提取`version_str`的前三位，并将结果存储在`version`变量中。
# 4. 如果系统平台不是Windows，则返回`version`变量。
# 总之，这段代码的主要功能是获取Chrome浏览器的版本信息，并将其前三位作为字符串返回。

chrome_version = get_chrome_version()  # 要更新的chromedriver版本

print("Detected your chrome version is: ", chrome_version)

chrome_driver_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
win64_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application"
win32_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application"
mac_chrome_path = "/Applications/Google Chrome.app"
linux_chrome_path = "/opt/google/chrome"
old_driver_version = {
    "100":"100.0.4896.60",
    "101":"101.0.4951.41",
    "102":"102.0.5005.61",
    "103":"103.0.5060.134",
    "104":"104.0.5112.79",
    "105":"105.0.5195.52",
    "106":"106.0.5249.61",
    "107":"107.0.5304.62",
    "108":"108.0.5359.71",
    "109":"109.0.5414.74",
    "110":"110.0.5481.77",
    "111":"111.0.5563.64",
    "112":"112.0.5615.49",
    "113":"113.0.5672.63",
    "114":"114.0.5735.90",
}
# 这段代码是用Python编写的，主要目的是获取Chrome浏览器的版本号，并更新chromedriver版本。以下是代码的详细解释：
# 1. `chrome_version = get_chrome_version()`：这行代码调用了一个名为`get_chrome_version()`的函数来获取Chrome浏览器的版本号。这个函数的实现可能需要根据具体的使用环境进行调整。
# 2. `print("Detected your chrome version is: ", chrome_version)`：这行代码打印出获取到的Chrome版本号。
# 3. `chrome_driver_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"`：这行代码定义了一个变量`chrome_driver_url`，它指向一个网址，该网址包含一个JSON文件，其中包含了与Chrome浏览器版本相对应的chromedriver版本信息。
# 4. `win64_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application"`：这行代码定义了一个变量`win64_chrome_path`，它指向Windows系统下64位Chrome浏览器的安装路径。
# 5. `win32_chrome_path = "C:\\Program Files\\Google\\Chrome\\Application"`：这行代码定义了一个变量`win32_chrome_path`，它指向Windows系统下32位Chrome浏览器的安装路径。
# 6. `mac_chrome_path = "/Applications/Google Chrome.app"`：这行代码定义了一个变量`mac_chrome_path`，它指向Mac操作系统下Chrome浏览器的安装路径。
# 7. `linux_chrome_path = "/opt/google/chrome"`：这行代码定义了一个变量`linux_chrome_path`，它指向Linux操作系统下Chrome浏览器的安装路径。
# 8. `old_driver_version = {...}`：这行代码定义了一个名为`old_driver_version`的字典，其中包含了旧版本的chromedriver版本和对应的Chrome浏览器版本。这些版本信息是根据Chrome浏览器版本进行排列的。
# 总之，这段代码的主要目的是获取Chrome浏览器的版本号，并根据该版本号从指定的网址中获取相应的chromedriver版本信息，以便进行更新。

if __name__ == "__main__":
    driver_downloads = []
    response = requests.get(chrome_driver_url)
    # 这段代码的主要功能是下载ChromeDriver。
    # 1. 首先，创建一个空列表`driver_downloads`，用于存储下载的ChromeDriver文件。
    # 2. 使用`requests.get()`函数向`chrome_driver_url`发送GET请求，获取ChromeDriver文件的响应。`response`变量将存储这个响应。

    if response.status_code == 200:
        versions = json.loads(response.content)["versions"]
        versions = versions[::-1] # 倒序排列数组
        for info in versions:
            version = info["version"].split(".")[0]
            if version.find(chrome_version) == 0:
                downloads = info["downloads"]
                if "chromedriver" in downloads:
                    print(info["version"])
                    driver_downloads = downloads["chromedriver"]
                    break
    else:
        print("Error: " + response.status_code)
        exit(1)
# 这段代码是用Python编写的，用于从API获取Chrome浏览器和ChromeDriver的版本信息。以下是代码的详细解释：
# 1. 首先，检查响应的状态码是否为200，即请求成功。如果状态码为200，则继续执行以下操作；否则，打印错误信息并退出程序。
# 2. 如果响应状态码为200，则使用`json.loads()`函数将响应内容转换为Python对象，然后从该对象中提取"versions"字段的值。
# 3. 对"versions"列表进行倒序排列，以便按照版本号从高到低进行遍历。
# 4. 遍历"versions"列表中的每个元素（info），并提取其"version"字段的值。
# 5. 将版本号拆分为单个数字，并检查它们是否与Chrome浏览器的版本号匹配（即以chrome_version开头）。如果是，则获取info中的"downloads"字段的值。
# 6. 遍历"downloads"字典，检查其中是否包含"chromedriver"键。如果是，则打印info中的"version"字段，并获取"downloads"字典中的"chromedriver"键的值（即ChromeDriver的下载量）。
# 7. 如果找到了匹配的Chrome浏览器版本和ChromeDriver下载量，则跳出循环，否则继续遍历下一个info。

    if not driver_downloads and int(chrome_version) < 115:
        if chrome_version not in old_driver_version:
            print("没有可用的chromedriver")
            exit(1)
        # 这段代码是用于检查Chrome浏览器的版本是否与预先定义的版本兼容。如果不兼容，则输出“没有可用的chromedriver”并退出程序。以下是代码的详细解释：
        # 1. `if chrome_version not in old_driver_version:`：这一行使用Python的比较运算符`not in`来检查`chrome_version`是否不在`old_driver_version`中。如果`chrome_version`不在`old_driver_version`中，则表示Chrome浏览器版本与预先定义的版本不兼容。
        # 2. `print("没有可用的chromedriver")`：这一行使用`print`函数输出“没有可用的chromedriver”。
        # 3. `exit(1)`：这一行使用`exit`函数退出程序，并传递一个整数值作为参数。在这个例子中，参数值为1，表示程序异常退出。

        full_version = old_driver_version[chrome_version]
        driver_downloads = [
            {
                "platform": "linux64",
                "url": f"http://chromedriver.storage.googleapis.com/{full_version}/chromedriver_linux64.zip",
            },
            {
                "platform": "mac-arm64",
                "url": f"http://chromedriver.storage.googleapis.com/{full_version}/chromedriver_mac_arm64.zip",
            },
            {
                "platform": "mac-x64",
                "url": f"http://chromedriver.storage.googleapis.com/{full_version}/chromedriver_mac64.zip",
            },
            {
                "platform": "win32",
                "url": f"http://chromedriver.storage.googleapis.com/{full_version}/chromedriver_win32.zip",
            },
            {
                "platform": "win64",
                "url": f"http://chromedriver.storage.googleapis.com/{full_version}/chromedriver_win32.zip",
            },
        ]
        # 这段代码的主要功能是定义了一个名为`full_version`的变量，其值为`old_driver_version[chrome_version]`。然后，它定义了一个名为`driver_downloads`的列表，其中包含一个字典列表，每个字典表示一个可下载的浏览器驱动程序。字典的键包括`platform`（平台）和`url`（下载链接）。
        # 字典的值是通过将`full_version`和`chrome_version`作为参数传递给`f`字符串格式化来生成的。`full_version`的值是`old_driver_version[chrome_version]`，`chrome_version`是一个名为`chrome_version`的变量。
        # 字典的值表示不同平台（如Linux、Mac、Windows等）的浏览器驱动程序的下载链接。这些链接存储在`url`键中，该键的值是通过将`http://chromedriver.storage.googleapis.com/`、`full_version`和相应的平台名称（如`linux64`、`mac-arm64`等）连接在一起而获得的。

    if os.path.exists("./chromedrivers"):
        shutil.rmtree("./chromedrivers")
        # 这段代码是用于检查当前目录下是否存在名为 "chromedrivers" 的文件夹，如果存在，则使用 shutil 库中的 rmtree 函数将其删除。
        # 1. `if os.path.exists("./chromedrivers"):` 这一行使用 os.path.exists 函数检查当前目录下是否存在名为 "chromedrivers" 的文件夹。如果存在，则条件为真，继续执行后续的代码。
        # 2. `shutil.rmtree("./chromedrivers")` 这一行使用 shutil 库中的 rmtree 函数删除当前目录下名为 "chromedrivers" 的文件夹。注意，这里使用了绝对路径 "./chromedrivers"，表示从当前目录开始查找。

    os.mkdir("./chromedrivers")
    # 这段代码是用Python编写的，用于在当前工作目录下创建一个名为"chromedrivers"的文件夹。
    # `os`是Python的标准库，提供了操作文件和目录的功能。`mkdir()`函数用于创建目录（文件夹）。
    # `""./chromedrivers"`是一个字符串，表示要创建的文件夹的名称。`"./`表示当前工作目录，即代码所在的目录。因此，这段代码会创建一个名为"chromedrivers"的文件夹，其父目录是当前工作目录。

    if sys.platform == "win32" and platform.architecture()[0] == "64bit":
        for download in driver_downloads:
            if download["platform"] == "win64":
                url = download["url"]
                print("ChromeDriver will be downloaded from: ", url)
                break
        # 这段代码是用Python编写的，主要用于在Google Chrome浏览器驱动程序下载过程中进行条件判断和操作。
        # 1. `for download in driver_downloads:`：使用`for`循环遍历`driver_downloads`列表中的每个元素，将元素赋值给变量`download`。
        # 2. `if download["platform"] == "win64":`：判断`download`字典中的`platform`键的值是否等于"win64"。如果是，则执行下面的操作。
        # 3. `url = download["url"]`：将`download`字典中的`url`键的值赋值给变量`url`。
        # 4. `print("ChromeDriver will be downloaded from: ", url)`：打印一条消息，表示将要下载的ChromeDriver文件的URL。
        # 5. `break`：跳出循环，结束下载过程。

        download_and_extract_zip(url, "./chromedrivers")
        if os.path.exists("./chrome_win64"):
            shutil.rmtree("./chrome_win64")
        copy_folder(win64_chrome_path, "./chrome_win64")
        for folder in os.listdir("./chrome_win64"):
            if folder[0].isdigit() and os.path.isdir("./chrome_win64/"+folder):
                shutil.rmtree("./chrome_win64/"+folder+"/Installer") # 删除Installer文件夹
        copy_file("./execute_win64.bat", "./chrome_win64/execute.bat")
        copy_file("./stealth.min.js", "./chrome_win64/stealth.min.js")
        # 这段代码的主要功能如下：
        # 1. 下载并解压缩zip文件
        # 2. 检查是否存在名为"./chrome_win64"的文件夹，如果存在，则删除该文件夹
        # 3. 将名为"win64_chrome_path"的文件夹复制到"./chrome_win64"文件夹
        # 4. 遍历"./chrome_win64"文件夹中的所有文件夹
        # a. 如果文件夹名以数字开头且是一个文件夹，则删除该文件夹中的"Installer"文件夹
        # 5. 将"./execute_win64.bat"文件复制到"./chrome_win64/execute.bat"
        # 6. 将"./stealth.min.js"文件复制到"./chrome_win64/stealth.min.js"
        # 这段代码是用Python编写的，使用了Python的库，如os、shutil、copyfile等。

        try:
            copy_file(
                "./chromedrivers/chromedriver-win64/chromedriver.exe",
                "./chrome_win64/chromedriver_win64.exe",
            )
        except:
            copy_file(
                "./chromedrivers/chromedriver.exe",
                "./chrome_win64/chromedriver_win64.exe",
            )
        finally:
            shutil.rmtree("./chromedrivers")
        # 这段代码是用Python编写的，用于在尝试复制文件时处理异常，并在尝试复制文件后或发生异常时执行清理工作。以下是代码的详细解释：
        # 1. 使用`try`语句尝试执行`copy_file`函数，传入两个参数：`"./chromedrivers/chromedriver-win64/chromedriver.exe"`和`"./chrome_win64/chromedriver_win64.exe"`。
        # 2. 如果`try`语句中的代码发生异常，将跳转到`except`语句，执行`copy_file`函数，传入两个参数：`"./chromedrivers/chromedriver.exe"`和`"./chrome_win64/chromedriver_win64.exe"`。
        # 3. 无论是否发生异常，都会执行`finally`语句。在该语句中，使用`shutil.rmtree`函数删除`./chromedrivers`文件夹。
        # 总之，这段代码的作用是尝试复制一个文件，如果尝试失败，则使用另一个文件替换它，并在尝试复制文件或发生异常后清理工作。

    elif sys.platform == "win32" and platform.architecture()[0] == "32bit":
        for download in driver_downloads:
            if download["platform"] == "win32":
                url = download["url"]
                print("ChromeDriver will be downloaded from: ", url)
                break
        # 这段代码是用Python编写的，用于遍历一个名为`driver_downloads`的列表。列表中的每个元素都是一个字典，表示一个可下载的ChromeDriver版本。
        # 代码首先使用`for`循环遍历`driver_downloads`列表中的每个元素。对于每个元素，它会检查其键为`"platform"`的值是否等于`"win32"`。如果是，它会将该元素的键为`"url"`的值赋给变量`url`，然后打印一条消息，指出ChromeDriver将从该URL下载。同时，它会使用`break`语句跳出循环，停止遍历。
        
        download_and_extract_zip(url, "./chromedrivers")
        if os.path.exists("./chrome_win32"):
            shutil.rmtree("./chrome_win32")
        copy_folder(win64_chrome_path, "./chrome_win32")
        for folder in os.listdir("./chrome_win32"):
            if folder[0].isdigit() and os.path.isdir("./chrome_win32/"+folder):
                shutil.rmtree("./chrome_win32/"+folder+"/Installer") # 删除Installer文件夹
        copy_file("./execute_win32.bat", "./chrome_win32/execute.bat")
        copy_file("./stealth.min.js", "./chrome_win32/stealth.min.js")
        # 这段代码的主要功能如下：
        # 1. 下载并解压缩zip文件
        # 2. 检查是否存在名为"./chrome_win32"的文件夹，如果存在，则删除它
        # 3. 将名为"win64_chrome_path"的文件夹复制到"./chrome_win32"文件夹中
        # 4. 遍历"./chrome_win32"文件夹中的所有文件夹
        # a. 如果文件夹名以数字开头且是文件夹，则删除该文件夹下的"Installer"文件夹
        # 5. 将名为"./execute_win32.bat"的文件复制到"./chrome_win32/execute.bat"中
        # 6. 将名为"./stealth.min.js"的文件复制到"./chrome_win32/stealth.min.js"中

        try:
            copy_file(
                "./chromedrivers/chromedriver-win32/chromedriver.exe",
                "./chrome_win32/chromedriver_win32.exe",
            )
        except:
            copy_file(
                "./chromedrivers/chromedriver.exe",
                "./chrome_win32/chromedriver_win64.exe",
            )
        finally:
            shutil.rmtree("./chromedrivers")
        # 这段代码是用Python编写的，用于在Windows操作系统上处理chromedriver文件。以下是代码的详细解释：
        # 1. 使用`try`语句尝试执行`copy_file`函数，传入两个参数：
        #   - `"./chromedrivers/chromedriver-win32/chromedriver.exe"`：这是chromedriver的源文件路径。
        #   - `"./chrome_win32/chromedriver_win32.exe"`：这是chromedriver的目标文件路径。
        # 2. 如果`try`语句执行过程中发生异常，将执行`except`子句，传入两个参数：
        #   - `"./chromedrivers/chromedriver.exe"`：这是chromedriver的源文件路径。
        #   - `"./chrome_win32/chromedriver_win64.exe"`：这是chromedriver的目标文件路径。
        # 3. 无论`try`语句是否发生异常，都会执行`finally`子句。`finally`子句用于在完成操作后清理临时文件夹。传入的参数是`"./chromedrivers"`，表示要删除的临时文件夹路径。
        # 总之，这段代码的作用是在Windows操作系统上尝试复制chromedriver文件，如果尝试失败，则将chromedriver的64位版本复制到目标路径。无论是否成功，最后都会删除临时文件夹。

    elif sys.platform == "linux" and platform.architecture()[0] == "64bit":
        pass
        # 这段代码是用于判断当前操作系统是否为Linux系统且为64位架构。以下是代码的详细解释：
        # 1. 使用`sys.platform`检查当前操作系统是否为Linux系统。
        # 2. 使用`platform.architecture()`获取当前操作系统的架构信息，并检查是否为64位架构。
        # 3. 如果当前操作系统为Linux系统且为64位架构，则执行`pass`语句，表示满足条件。
        # 这段代码的作用是确保只有在Linux系统且为64位架构的情况下，才会执行后续的代码块。这样可以确保代码只在满足条件的情况下运行，避免在非Linux系统或非64位架构的系统上运行错误。

    elif sys.platform == "darwin" and platform.architecture()[0] == "64bit":
    # 这段代码是用于判断当前系统是否为macOS系统且系统架构为64位。
    # 1. `sys.platform` 是一个Python内置的模块，用于获取当前操作系统的名称。在这里，它被用来检查当前系统是否为macOS。
    # 2. `platform.architecture()` 是Python内置的模块，用于获取当前系统的架构信息。在这里，它被用来检查当前系统是否为64位架构。`architecture()`函数返回一个元组，包含两个元素：系统架构（如'32bit'或'64bit'）和Python解释器架构（如'x86_64'或'arm64'）。
    # 3. `and` 关键字用于连接两个条件。只有当同时满足这两个条件时，整个条件才为真。在这里，只有当系统为macOS且架构为64位时，整个条件才为真。

        processor = get_processor_info()
        if processor == "Intel":
            driver_arch = "mac-x64"
        elif processor == "Apple":
            driver_arch = "mac-arm64"
        for download in driver_downloads:
            if download["platform"] == driver_arch:
                url = download["url"]
                print("ChromeDriver will be downloaded from: ", url)
                break
        # download_and_extrac这段代码的主要功能是获取浏览器的处理器信息，并根据处理器类型下载相应的ChromeDriver。以下是代码的详细解释：
        # 1. `processor = get_processor_info()`：调用`get_processor_info()`函数获取当前浏览器的处理器信息，并将结果存储在`processor`变量中。
        # 2. `if processor == "Intel":`：判断当前处理器是否为Intel处理器。如果是，则进入`if`语句块。
        # 3. `driver_arch = "mac-x64"`：如果是Intel处理器，则将`driver_arch`变量设置为"mac-x64"，表示下载macOS x64版本的ChromeDriver。
        # 4. `elif processor == "Apple":`：判断当前处理器是否为Apple处理器（即ARM架构的Mac）。如果是，则进入`elif`语句块。
        # 5. `driver_arch = "mac-arm64"`：如果是Apple处理器，则将`driver_arch`变量设置为"mac-arm64"，表示下载macOS ARM架构版本的ChromeDriver。
        # 6. `for download in driver_downloads:`：遍历`driver_downloads`列表中的每个元素。
        # 7. `if download["platform"] == driver_arch:`：判断当前元素的`platform`属性是否与`driver_arch`变量相等。如果是，则进入`if`语句块。
        # 8. `url = download["url"]`：如果是，则将当前元素的`url`属性存储在`url`变量中。
        # 9. `print("ChromeDriver will be downloaded from: ", url)`：打印下载ChromeDriver的URL。
        # 10. `break`：跳出循环，结束遍历。t_zip(url, "./chromedrivers")

        if os.path.exists("./chrome_mac64.app"):
            shutil.rmtree("./chrome_mac64.app")
        # copy_folder(mac_chrome_path, "./chrome_mac64.app")
        subprocess.call(["cp", "-R", mac_chrome_path, "./chrome_mac64.app"])
        try:
            copy_file(
                "./chromedrivers/chromedriver-%s/chromedriver" % driver_arch,
                "./chromedriver_mac64",
            )
        except:
            copy_file(
                "./chromedrivers/chromedriver",
                "./chromedriver_mac64",
            )
        finally:
            shutil.rmtree("./chromedrivers")
        os.chmod("./chromedriver_mac64", 0o755)
        os.chmod("./chrome_mac64.app", 0o555)
        os.chmod("./chrome_mac64.app/Contents/MacOS/Google Chrome", 0o555)
        # 这段代码是在Python环境中执行的，主要功能是安装和配置Chrome浏览器和ChromeDriver。以下是代码的详细解释：
        # 1. 首先，代码检查`./chrome_mac64.app`文件夹是否存在。如果存在，则使用`shutil.rmtree()`方法将其删除。
        # 2. 然后，代码将`mac_chrome_path`（即从macOS系统上获取的Chrome浏览器文件夹路径）复制到`./chrome_mac64.app`文件夹中。这里使用了`subprocess.call()`方法来执行`cp -R mac_chrome_path ./chrome_mac64.app`命令。
        # 3. 接下来，代码尝试使用`copy_file()`函数将`./chromedrivers/chromedriver-%s/chromedriver`（其中`%s`是`driver_arch`变量的值）复制到`./chromedriver_mac64`文件夹中。如果这个过程失败，则使用`copy_file()`函数将`./chromedrivers/chromedriver`复制到`./chromedriver_mac64`文件夹中。
        # 4. 最后，代码使用`shutil.rmtree()`方法删除`./chromedrivers`文件夹。
        # 5. 代码使用`os.chmod()`方法将`./chromedriver_mac64`文件夹的权限更改为`0o755`，将`./chrome_mac64.app`的权限更改为`0o555`，将`./chrome_mac64.app/Contents/MacOS/Google Chrome`的权限更改为`0o555`。这些权限分别表示：可读、可写、可执行、可执行、可执行。
   
    print("Done and don't forget to generate executestage EXEcutable program!")
