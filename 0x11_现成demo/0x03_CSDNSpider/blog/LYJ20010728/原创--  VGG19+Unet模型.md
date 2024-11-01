# 原创
：  VGG19+Unet模型

# VGG19+Unet模型

**搭建模型结构代码**

```
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import models

def VGG19(img_input):
    # 512,512,3 -&gt; 512,512,64
    x = layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv1-1')(img_input)
    x = layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv1-2')(x)
    conv1 = x
    
    # 512,512,64 -&gt; 256,256,64
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), name='pool1')(x)
    
    # 256,256,64 -&gt; 256,256,128
    x = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv2-1')(x)
    x = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv2-2')(x)
    conv2 = x
    
    # 256,256,128 -&gt; 128,128,128
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), name='pool2')(x)
    
    # 128,128,128 -&gt; 128,128,256
    x = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv3-1')(x)
    x = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv3-2')(x)
    x = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv3-3')(x)
    x = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv3-4')(x)
    conv3 = x
    
    # 128,128,256 -&gt; 64,64,256
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), name='pool3')(x)
    
    # 64,64,256 -&gt; 64,64,512
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv4-1')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv4-2')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv4-3')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv4-4')(x)
    conv4 = x
    
    # 64,64,512 -&gt; 32,32,512
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), name='pool4')(x)
    
    # 32,32,512 -&gt; 32,32,512
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv5-1')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv5-2')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv5-3')(x)
    x = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', name='conv5-4')(x)
    conv5 = x
    
    return conv1, conv2, conv3, conv4, conv5

def Unet(input_shape=(512,512,3), num_classes=21):
    '''获取输入的图片的尺寸'''
    inputs = layers.Input(input_shape)
    
    '''
    获取之前VGG19生成的五个有效特征层
    conv1    512,512,64
    conv2    256,256,128
    conv3    128,128,256
    conv4    64,64,512
    conv5    32,32,512
    '''
    conv1, conv2, conv3, conv4, conv5 = VGG19(inputs)
    
    # 32,32,512 -&gt; 64,64,512
    U5_up = layers.UpSampling2D(size=(2,2), interpolation='nearest')(conv5)
    
    # 64,64,512 + 64,64,512 -&gt; 64,64,1024
    U4 = layers.Concatenate(axis=3)([conv4, U5_up])
    
    # 64,64,1024 -&gt; 64,64,512
    U4 = layers.Conv2D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U4)
    U4 = layers.Conv2D(filters=512, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U4)
    
    # 64,64,512 -&gt; 128,128,512
    U4_up = layers.UpSampling2D(size=(2,2), interpolation='nearest')(U4)
    
    # 128,128,512 + 128,128,256 -&gt; 128,128,768
    U3 = layers.Concatenate(axis=3)([conv3, U4_up])
    
    # 128,128,768 -&gt; 128,128,256
    U3 = layers.Conv2D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U3)
    U3 = layers.Conv2D(filters=256, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U3)
    
    # 128,128,256 -&gt; 256,256,256
    U3_up = layers.UpSampling2D(size=(2,2), interpolation='nearest')(U3)
    
    # 256,256,256 + 256,256,128 -&gt; 256,256,384
    U2 = layers.Concatenate(axis=3)([conv2, U3_up])
    
    # 256,256,384 -&gt; 256,256,128
    U2 = layers.Conv2D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U2)
    U2 = layers.Conv2D(filters=128, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U2)
    
    # 256,256,128 -&gt; 512,512,128
    U2_up = layers.UpSampling2D(size=(2,2), interpolation='nearest')(U2)
    
    # 512,512,128 + 512,512,64 -&gt; 512,512,192
    U1 = layers.Concatenate(axis=3)([conv1, U2_up])
    
    # 512,512,192 -&gt; 512,512,64
    U1 = layers.Conv2D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U1)
    U1 = layers.Conv2D(filters=64, kernel_size=3, strides=1, activation='relu', padding='same', kernel_initializer='he_normal')(U1)
    
    # 512,512,64 -&gt; 512,512,num_classes
    outputs = layers.Conv2D(filters=num_classes, kernel_size=1, strides=1, activation='softmax')(U1)
    
    model = models.Model(inputs=inputs, outputs=outputs)
    return model

```

**测试模型并的出模型结构层次**

```
image_size = (512,512,3)
num_classes = 21
model = Unet(image_size, num_classes)
model.summary()

```

```
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 512, 512, 3) 0                                            
__________________________________________________________________________________________________
conv1-1 (Conv2D)                (None, 512, 512, 64) 1792        input_1[0][0]                    
__________________________________________________________________________________________________
conv1-2 (Conv2D)                (None, 512, 512, 64) 36928       conv1-1[0][0]                    
__________________________________________________________________________________________________
pool1 (MaxPooling2D)            (None, 256, 256, 64) 0           conv1-2[0][0]                    
__________________________________________________________________________________________________
conv2-1 (Conv2D)                (None, 256, 256, 128 73856       pool1[0][0]                      
__________________________________________________________________________________________________
conv2-2 (Conv2D)                (None, 256, 256, 128 147584      conv2-1[0][0]                    
__________________________________________________________________________________________________
pool2 (MaxPooling2D)            (None, 128, 128, 128 0           conv2-2[0][0]                    
__________________________________________________________________________________________________
conv3-1 (Conv2D)                (None, 128, 128, 256 295168      pool2[0][0]                      
__________________________________________________________________________________________________
conv3-2 (Conv2D)                (None, 128, 128, 256 590080      conv3-1[0][0]                    
__________________________________________________________________________________________________
conv3-3 (Conv2D)                (None, 128, 128, 256 590080      conv3-2[0][0]                    
__________________________________________________________________________________________________
conv3-4 (Conv2D)                (None, 128, 128, 256 590080      conv3-3[0][0]                    
__________________________________________________________________________________________________
pool3 (MaxPooling2D)            (None, 64, 64, 256)  0           conv3-4[0][0]                    
__________________________________________________________________________________________________
conv4-1 (Conv2D)                (None, 64, 64, 512)  1180160     pool3[0][0]                      
__________________________________________________________________________________________________
conv4-2 (Conv2D)                (None, 64, 64, 512)  2359808     conv4-1[0][0]                    
__________________________________________________________________________________________________
conv4-3 (Conv2D)                (None, 64, 64, 512)  2359808     conv4-2[0][0]                    
__________________________________________________________________________________________________
conv4-4 (Conv2D)                (None, 64, 64, 512)  2359808     conv4-3[0][0]                    
__________________________________________________________________________________________________
pool4 (MaxPooling2D)            (None, 32, 32, 512)  0           conv4-4[0][0]                    
__________________________________________________________________________________________________
conv5-1 (Conv2D)                (None, 32, 32, 512)  2359808     pool4[0][0]                      
__________________________________________________________________________________________________
conv5-2 (Conv2D)                (None, 32, 32, 512)  2359808     conv5-1[0][0]                    
__________________________________________________________________________________________________
conv5-3 (Conv2D)                (None, 32, 32, 512)  2359808     conv5-2[0][0]                    
__________________________________________________________________________________________________
conv5-4 (Conv2D)                (None, 32, 32, 512)  2359808     conv5-3[0][0]                    
__________________________________________________________________________________________________
up_sampling2d (UpSampling2D)    (None, 64, 64, 512)  0           conv5-4[0][0]                    
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 64, 64, 1024) 0           conv4-4[0][0]                    
                                                                 up_sampling2d[0][0]              
__________________________________________________________________________________________________
conv2d (Conv2D)                 (None, 64, 64, 512)  4719104     concatenate[0][0]                
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 64, 64, 512)  2359808     conv2d[0][0]                     
__________________________________________________________________________________________________
up_sampling2d_1 (UpSampling2D)  (None, 128, 128, 512 0           conv2d_1[0][0]                   
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 128, 128, 768 0           conv3-4[0][0]                    
                                                                 up_sampling2d_1[0][0]            
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 128, 128, 256 1769728     concatenate_1[0][0]              
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 128, 128, 256 590080      conv2d_2[0][0]                   
__________________________________________________________________________________________________
up_sampling2d_2 (UpSampling2D)  (None, 256, 256, 256 0           conv2d_3[0][0]                   
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 256, 256, 384 0           conv2-2[0][0]                    
                                                                 up_sampling2d_2[0][0]            
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 256, 256, 128 442496      concatenate_2[0][0]              
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 256, 256, 128 147584      conv2d_4[0][0]                   
__________________________________________________________________________________________________
up_sampling2d_3 (UpSampling2D)  (None, 512, 512, 128 0           conv2d_5[0][0]                   
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 512, 512, 192 0           conv1-2[0][0]                    
                                                                 up_sampling2d_3[0][0]            
__________________________________________________________________________________________________
conv2d_6 (Conv2D)               (None, 512, 512, 64) 110656      concatenate_3[0][0]              
__________________________________________________________________________________________________
conv2d_7 (Conv2D)               (None, 512, 512, 64) 36928       conv2d_6[0][0]                   
__________________________________________________________________________________________________
conv2d_8 (Conv2D)               (None, 512, 512, 21) 1365        conv2d_7[0][0]                   
==================================================================================================
Total params: 30,202,133
Trainable params: 30,202,133
Non-trainable params: 0
__________________________________________________________________________________________________

```
