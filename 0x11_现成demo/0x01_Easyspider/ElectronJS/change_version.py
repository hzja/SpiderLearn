import json
import os
import re
import sys

# 读取JSON文件


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
    # 这段代码定义了一个名为`read_json_file`的函数，它接受一个参数`file_path`，表示要读取的JSON文件的路径。
    # 函数内部首先使用`with open()`语句打开文件，并指定文件读取模式为`'r'`（只读），编码为`'utf-8'`。
    # 然后，使用`json.load()`函数将文件内容加载到一个变量`data`中。最后，函数返回`data`。
    # 保存为JSON文件


def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    # 这段代码定义了一个名为`save_json_file`的函数，用于将数据保存到以`file_path`为参数的JSON文件中。函数接受两个参数：`data`和`file_path`。
    # 1. `data`：这个参数是要保存到JSON文件中的数据。它可以是任何可以被`json.dump()`函数序列化的Python对象，例如字典、列表等。
    # 2. `file_path`：这个参数是要保存数据的文件路径。它是一个字符串，表示要保存数据的文件的完整路径。
    # 3. 使用`with open()`语句打开文件。`open()`函数的第一个参数是文件路径，第二个参数是文件模式（'w'表示写入模式）。`encoding='utf-8'`表示文件以UTF-8编码方式打开。
    # 4. 使用`json.dump()`函数将数据`data`保存到打开的文件`file`中。`indent=4`表示在输出中使用4个空格作为缩进，`ensure_ascii=False`表示不将非ASCII字符作为转义字符输出。

def update_file_version(file_path, new_version, key="当前版本/Current Version: v"):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if key in line:
                pattern = r'('+key+')\d+\.\d+\.\d+'
                line = re.sub(pattern, r'\g<1>'+new_version, line)
            file.write(line)
    # 这段代码定义了一个名为`update_file_version`的函数，用于更新指定文件中指定的版本信息。函数接受三个参数：`file_path`（文件路径），`new_version`（新的版本号）和`key`（用于查找版本信息的关键字）。
    # 函数首先使用`with open()`语句以读取模式打开文件，并读取文件的所有行。然后，它使用`with open()`语句以写入模式打开文件，并遍历文件的所有行。
    # 对于每一行，函数首先检查`key`是否存在于该行中。如果`key`存在于该行中，函数将使用正则表达式`pattern`来匹配该行中的版本信息，并将新的版本号替换为已匹配的部分。正则表达式`pattern`的构造如下：`(key)(\d+\.\d+\.\d+)`，其中`()`用于捕获分组，`\g<1>`表示将捕获的第一个组（即`key`）插入到替换字符串中。
    # 最后，函数将修改后的行写入文件。

version = "0.6.0"

# py html js

if __name__ == "__main__":

    file_path = "../.temp_to_pub/compress.py"
    update_file_version(file_path, version, key='easyspider_version = "')

    file_path = "./src/taskGrid/logic.js"
    update_file_version(file_path, version, key='"version": "')

    file_path = "../ExecuteStage/easyspider_executestage.py"
    update_file_version(file_path, version, key='"version": "')

    # index.html
    file_path = "./src/index.html"
    update_file_version(file_path, version, key="当前版本/Current Version: <b>v")

    # package.json
    file_path = "./package.json"

    # 读取JSON文件
    electron_config = read_json_file(file_path)
    print(electron_config["version"])

    # 修改数据
    electron_config["version"] = version
    electron_config["config"]["forge"]["packagerConfig"]["appVersion"] = version

    # 保存为JSON文件
    save_json_file(electron_config, file_path)

    # 插件的package.json
    file_path = "../Extension/manifest_v3/package.json"

    # 读取JSON文件
    electron_config = read_json_file(file_path)
    print(electron_config["version"])

    # 修改数据
    electron_config["version"] = version

    # 保存为JSON文件
    save_json_file(electron_config, file_path)

    file_path = "../Extension/manifest_v3/src/manifest.json"

    # 读取JSON文件
    electron_config = read_json_file(file_path)
    print(electron_config["version"])

    # 修改数据
    electron_config["version"] = version

    # 保存为JSON文件
    save_json_file(electron_config, file_path)
    # 这段Python代码的主要功能是对不同文件进行版本更新。具体来说，它首先定义了一个名为`update_file_version`的函数，该函数接受三个参数：文件路径、版本号和关键字。然后，它遍历了五个文件，分别对它们进行版本更新。
    # 1. 第一个文件：`file_path = "../.temp_to_pub/compress.py"`，版本更新关键字为`easyspider_version = "`。
    # 2. 第二个文件：`file_path = "./src/taskGrid/logic.js"`，版本更新关键字为`"version": "`。
    # 3. 第三个文件：`file_path = "../ExecuteStage/easyspider_executestage.py"`，版本更新关键字为`"version": "`。
    # 4. 第四个文件：`file_path = "./src/index.html"`，版本更新关键字为`当前版本/Current Version: <b>v`。
    # 5. 第五个文件：`file_path = "./package.json"`。首先，它读取了`package.json`文件，并打印了其中的版本号。然后，它将版本号修改为传入的参数`version`，并将修改后的数据保存回`package.json`文件。
    # 6. 第六个文件：`file_path = "../Extension/manifest_v3/package.json"`。与第五个文件类似，首先读取`package.json`文件，并打印其中的版本号。然后，将版本号修改为传入的参数`version`，并将修改后的数据保存回`package.json`文件。
    # 7. 第七个文件：`file_path = "../Extension/manifest_v3/src/manifest.json"`。与第六个文件类似，首先读取`manifest.json`文件，并打印其中的版本号。然后，将版本号修改为传入的参数`version`，并将修改后的数据保存回`manifest.json`文件。
