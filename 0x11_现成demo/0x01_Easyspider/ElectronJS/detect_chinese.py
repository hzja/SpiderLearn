import re

with open('src/taskGrid/FlowChart.js', 'r', encoding='utf-8') as file:
    for line in file:
        line = re.split('//', line)[0]
        if re.search('[\u4e00-\u9fff]', line):
            print(line)

# 这段代码是用Python编写的，用于处理一个名为`FlowChart.js`的文件。`with open`语句用于打开文件，参数`'src/taskGrid/FlowChart.js'`表示要打开的文件路径，`'r'`表示以只读模式打开文件，`encoding='utf-8'`表示使用UTF-8编码读取文件。
# 接下来，使用`for line in file`语句遍历文件中的每一行。对于每一行，首先使用正则表达式`re.split('//', line)[0]`将其分成两部分，第一部分是去掉注释的部分，第二部分是注释本身。然后，使用正则表达式`re.search('[\u4e00-\u9fff]', line)`检查去掉注释的部分是否包含中文字符。如果包含中文字符，则使用`print(line)`语句将其打印出来。