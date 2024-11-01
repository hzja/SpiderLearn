# 原创
：  pima-indians-diabetes

# pima-indians-diabetes

**搭建模型**

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 12)                108       
_________________________________________________________________
dense_1 (Dense)              (None, 8)                 104       
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 9         
=================================================================
Total params: 221
Trainable params: 221
Non-trainable params: 0
_________________________________________________________________
None

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210309204502924.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> **程序代码**

```
# 调用要使用的包
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

# 指定随机种子，为了确保每次运行的结果一致
np.random.seed(5)

# 准备数据
dataset = np.loadtxt('PimaIndiansdiabetes.csv', delimiter=",")

# 生成数据集
x_train = dataset[:700, 0:8]
y_train = dataset[:700, 8]
x_test = dataset[700:, 0:8]
y_test = dataset[700:, 8]

# 搭建模型
models = Sequential()
models.add(Dense(12, input_dim=8, activation='relu'))
models.add(Dense(8, activation='relu'))
models.add(Dense(1, activation='sigmoid'))

# 设置模型训练过程
models.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 训练模型
models.fit(x_train, y_train, epochs=1500, batch_size=64)

# 评价模型
scores = models.evaluate(x_test, y_test)
print(scores)
print(models.metrics_names)
print("%s: %.2f%%" % (models.metrics_names[1], scores[1]*100))

```

**训练模型**

```
Epoch 1/1500
11/11 [==============================] - 0s 940us/step - loss: 3.7088 - accuracy: 0.4714
Epoch 2/1500
11/11 [==============================] - 0s 635us/step - loss: 2.4963 - accuracy: 0.4843
Epoch 3/1500
11/11 [==============================] - 0s 725us/step - loss: 1.8659 - accuracy: 0.4757
...
Epoch 1498/1500
11/11 [==============================] - 0s 725us/step - loss: 0.3812 - accuracy: 0.8057
Epoch 1499/1500
11/11 [==============================] - 0s 725us/step - loss: 0.3819 - accuracy: 0.8143
Epoch 1500/1500
11/11 [==============================] - 0s 635us/step - loss: 0.3864 - accuracy: 0.8057

```

**评价模型**

```
3/3 [==============================] - 0s 1ms/step - loss: 0.5841 - accuracy: 0.7353
[0.5841068625450134, 0.7352941036224365]
['loss', 'accuracy']
accuracy: 73.53%

```

**CSV文件链接**<br/> `链接：https://pan.baidu.com/s/1dIGqSmUv61TBw0lCAgGM9Q 提取码：0728 复制这段内容后打开百度网盘手机App，操作更方便哦`
