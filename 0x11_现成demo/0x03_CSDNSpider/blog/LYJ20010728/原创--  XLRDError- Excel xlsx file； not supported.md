# 原创
：  XLRDError: Excel xlsx file； not supported

# XLRDError: Excel xlsx file； not supported

**报错原因**

```
xlrd版本的问题，现在安装的xlrd是2.0.1版本，不支持xlsx格式

```

**解决方法**

```
1、
卸载当前安装的xlrd  --&gt;  pip uninstall xlrd
安装低版本的xlrd --&gt;  pip install xlrd==1.2.0

2、
用openpyxl代替xlrd打开.xlsx文件(推荐)
data = pd.read_excel('test.xlsx', engine='openpyxl')
openpyxl版本 --&gt; 3.0.5

```
