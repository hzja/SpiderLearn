# 原创
：  2-5 Linux文件特殊权限与特殊属性

# 2-5 Linux文件特殊权限与特殊属性

## Linux特殊权限

### 一、粘滞位权限：

#### 功能：

#### 使用场景：

#### 示例：

#### 数字权限：

赋予方法：`chmod o+t 目录名称`

```
chmod o+t dir
```

**例：**

#### 以下是一个使用粘滞位权限的示例：

##### 1）创建一个目录（例如，.`/shared/directory`）并赋予所有用户读写权限。

```
sudo mkdir -p ./shared/directory

# 这里的1是粘滞位权限
sudo chmod 1777 ./shared/directory
```

 
