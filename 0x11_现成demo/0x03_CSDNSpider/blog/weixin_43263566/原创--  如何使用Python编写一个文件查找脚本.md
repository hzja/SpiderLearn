# 原创
：  如何使用Python编写一个文件查找脚本

# 如何使用Python编写一个文件查找脚本

**部分数据来源：**ChatGPT 

#### 引言

        对于计算机用户来说，文件查找是一个常见且重要的任务。无论是找到特定类型的文件，还是按照文件大小进行筛选，一个高效的文件查找脚本都能够提供便利，帮助我们快速找到需要的文件。

本文将介绍如何使用Python编写一个简单的文件查找脚本，并且适合小白阅读和使用。

#### 脚本实现的功能：

首先，我们需要导入Python的os模块，以便能够访问文件系统相关的功能。

```
import os

```

接下来，我们定义一个名为`find_files`的函数，该函数接受以下参数：

```
def find_files(root_dir, file_extension, min_file_size, max_file_size, output_file):
    with open(output_file, 'w') as file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(file_extension):
                    file_path = os.path.join(dirpath, filename)
                    size = os.path.getsize(file_path) / 1024  # 转换为 KB

                    if (min_file_size is None or size &gt;= min_file_size) and \
                            (max_file_size is None or size &lt;= max_file_size):
                        file.write(f"{file_path}\tSize: {size:.2f} KB\n")

```

在这个函数中，我们使用了`os.walk`函数遍历指定根目录下的所有文件和文件夹。然后，我们检查每个文件的文件类型是否与指定的文件类型一致，并且检查文件的大小是否在指定范围内。如果满足条件，我们将文件的路径和大小写入输出文件中。

最后，我们需要获取用户的输入来执行文件查找操作。

```
root_directory = input("请输入要查找的根目录：")
file_extension = input("请输入要查找的文件类型（例如：.txt）：")
min_size = float(input("请输入最小文件大小（按KB计算），不需要限制请留空：") or -1)
max_size = float(input("请输入最大文件大小（按KB计算），不需要限制请留空：") or -1)
output_filename = input("请输入输出文件名：")

find_files(root_directory, file_extension, min_size, max_size, output_filename)
print("文件查找完成！结果已保存到", output_filename, "中。")

```

通过以上代码，我们首先接收用户输入的根目录、文件类型、最小和最大文件大小以及输出文件名。然后，我们调用`find_files`函数，并将用户输入作为参数传递给函数。最后，我们打印出查找完成的提示信息。

现在，我们只需保存以上代码为一个Python脚本文件，比如`file_search.py`，然后在命令行中运行这个脚本。按照提示输入需要的信息，脚本将会在指定的根目录下进行文件查找，并将结果保存到指定的输出文件中。

这个脚本的好处在于，它可以根据用户的需求快速查找文件，并且能够灵活地按照文件类型和大小进行筛选。无论是在个人使用还是工作场景中，这个文件查找脚本都能为用户提供便利。

#### 完整代码

```
import os

def find_files(root_dir, file_extension, min_file_size, max_file_size, output_file):
    with open(output_file, 'w') as file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(file_extension):
                    file_path = os.path.join(dirpath, filename)
                    size = os.path.getsize(file_path) / 1024  # 转换为 KB

                    if (min_file_size is None or size &gt;= min_file_size) and \
                            (max_file_size is None or size &lt;= max_file_size):
                        file.write(f"{file_path}\tSize: {size:.2f} KB\n")

root_directory = input("请输入要查找的根目录：")
file_extension = input("请输入要查找的文件类型（例如：.txt）：")
min_size = float(input("请输入最小文件大小（按KB计算），不需要限制请留空：") or -1)
max_size = float(input("请输入最大文件大小（按KB计算），不需要限制请留空：") or -1)
output_filename = input("请输入输出文件名：")

find_files(root_directory, file_extension, min_size, max_size, output_filename)
print("文件查找完成！结果已保存到", output_filename, "中。")
```

 
