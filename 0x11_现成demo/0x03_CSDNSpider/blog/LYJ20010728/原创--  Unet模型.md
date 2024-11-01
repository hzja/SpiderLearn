# 原创
：  Unet模型

# Unet模型

**搭建模型结构代码**

```
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import models

def Unet(input_shape=(512,512,3), num_classes=21):
    # 输入图片的尺寸
    inputs = layers.Input(input_shape)
    
    # 512,512,3 -&gt; 512,512,64
    conv1 = layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
    conv1 = layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
    
    # 512,512,64 -&gt; 256,256,64
    pool1 = layers.MaxPooling2D(pool_size=(2, 2))(conv1)
    
    # 256,256,64 -&gt; 256,256,128
    conv2 = layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
    conv2 = layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
    
    # 256,256,128 -&gt; 128,128,128
    pool2 = layers.MaxPooling2D(pool_size=(2, 2))(conv2)
    
    # 128,128,128 -&gt; 128,128,256
    conv3 = layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
    conv3 = layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
    
    # 128,128,256 -&gt; 64,64,256
    pool3 = layers.MaxPooling2D(pool_size=(2, 2))(conv3)
    
    # 64,64,256 -&gt; 64,64,512
    conv4 = layers.Conv2D(filters=512, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
    conv4 = layers.Conv2D(filters=512, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
    drop4 = layers.Dropout(0.5)(conv4)
    
    # 64,64,512 -&gt; 32,32,512
    pool4 = layers.MaxPooling2D(pool_size=(2, 2))(drop4)
    
    # 32,32,512 -&gt; 32,32,1024
    conv5 = layers.Conv2D(filters=1024, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
    conv5 = layers.Conv2D(filters=1024, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
    drop5 = layers.Dropout(0.5)(conv5)
    
    
    # 32,32,1024 -&gt; 64,64,512 
    up6 = layers.Conv2D(filters=512, kernel_size=2, activation='relu', padding='same', kernel_initializer='he_normal')(layers.UpSampling2D(size=(2,2))(drop5))
    merge6 = layers.Concatenate(axis=3)([drop4,up6])
    conv6 = layers.Conv2D(filters=512, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(merge6)
    conv6 = layers.Conv2D(filters=512, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)
 
    # 64,64,512 -&gt; 128,128,256
    up7 = layers.Conv2D(filters=256, kernel_size=2, activation='relu', padding='same', kernel_initializer='he_normal')(layers.UpSampling2D(size=(2,2))(conv6))
    merge7 = layers.Concatenate(axis=3)([conv3,up7])
    conv7 = layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(merge7)
    conv7 = layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)
 
    # 128,128,256 -&gt; 256,256,128
    up8 = layers.Conv2D(filters=128, kernel_size=2, activation='relu', padding='same', kernel_initializer='he_normal')(layers.UpSampling2D(size=(2,2))(conv7))
    merge8 = layers.Concatenate(axis=3)([conv2,up8])
    conv8 = layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(merge8)
    conv8 = layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)
     
    # 256,256,128 -&gt; 512,512,64
    up9 = layers.Conv2D(filters=64, kernel_size=2, activation='relu', padding='same', kernel_initializer='he_normal')(layers.UpSampling2D(size=(2,2))(conv8))
    merge9 = layers.Concatenate(axis=3)([conv1,up9])
    conv9 = layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
    conv9 = layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
    
    # 512,512,64 -&gt; 512,512,num_classes
    conv10 = layers.Conv2D(filters=num_classes, kernel_size=1, activation='softmax')(conv9)
 
    model = models.Model(inputs=inputs, outputs=conv10)
    return model

```

**测试模型并的出模型结构层次**

```
inupt_size = (512,512,3)
num_classes = 21
model = Unet(inupt_size, num_classes)
model.summary()

```

```
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 512, 512, 3) 0                                            
__________________________________________________________________________________________________
conv2d (Conv2D)                 (None, 512, 512, 64) 1792        input_1[0][0]                    
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 512, 512, 64) 36928       conv2d[0][0]                     
__________________________________________________________________________________________________
max_pooling2d (MaxPooling2D)    (None, 256, 256, 64) 0           conv2d_1[0][0]                   
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 256, 256, 128 73856       max_pooling2d[0][0]              
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 256, 256, 128 147584      conv2d_2[0][0]                   
__________________________________________________________________________________________________
max_pooling2d_1 (MaxPooling2D)  (None, 128, 128, 128 0           conv2d_3[0][0]                   
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 128, 128, 256 295168      max_pooling2d_1[0][0]            
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 128, 128, 256 590080      conv2d_4[0][0]                   
__________________________________________________________________________________________________
max_pooling2d_2 (MaxPooling2D)  (None, 64, 64, 256)  0           conv2d_5[0][0]                   
__________________________________________________________________________________________________
conv2d_6 (Conv2D)               (None, 64, 64, 512)  1180160     max_pooling2d_2[0][0]            
__________________________________________________________________________________________________
conv2d_7 (Conv2D)               (None, 64, 64, 512)  2359808     conv2d_6[0][0]                   
__________________________________________________________________________________________________
dropout (Dropout)               (None, 64, 64, 512)  0           conv2d_7[0][0]                   
__________________________________________________________________________________________________
max_pooling2d_3 (MaxPooling2D)  (None, 32, 32, 512)  0           dropout[0][0]                    
__________________________________________________________________________________________________
conv2d_8 (Conv2D)               (None, 32, 32, 1024) 4719616     max_pooling2d_3[0][0]            
__________________________________________________________________________________________________
conv2d_9 (Conv2D)               (None, 32, 32, 1024) 9438208     conv2d_8[0][0]                   
__________________________________________________________________________________________________
dropout_1 (Dropout)             (None, 32, 32, 1024) 0           conv2d_9[0][0]                   
__________________________________________________________________________________________________
up_sampling2d (UpSampling2D)    (None, 64, 64, 1024) 0           dropout_1[0][0]                  
__________________________________________________________________________________________________
conv2d_10 (Conv2D)              (None, 64, 64, 512)  2097664     up_sampling2d[0][0]              
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 64, 64, 1024) 0           dropout[0][0]                    
                                                                 conv2d_10[0][0]                  
__________________________________________________________________________________________________
conv2d_11 (Conv2D)              (None, 64, 64, 512)  4719104     concatenate[0][0]                
__________________________________________________________________________________________________
conv2d_12 (Conv2D)              (None, 64, 64, 512)  2359808     conv2d_11[0][0]                  
__________________________________________________________________________________________________
up_sampling2d_1 (UpSampling2D)  (None, 128, 128, 512 0           conv2d_12[0][0]                  
__________________________________________________________________________________________________
conv2d_13 (Conv2D)              (None, 128, 128, 256 524544      up_sampling2d_1[0][0]            
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 128, 128, 512 0           conv2d_5[0][0]                   
                                                                 conv2d_13[0][0]                  
__________________________________________________________________________________________________
conv2d_14 (Conv2D)              (None, 128, 128, 256 1179904     concatenate_1[0][0]              
__________________________________________________________________________________________________
conv2d_15 (Conv2D)              (None, 128, 128, 256 590080      conv2d_14[0][0]                  
__________________________________________________________________________________________________
up_sampling2d_2 (UpSampling2D)  (None, 256, 256, 256 0           conv2d_15[0][0]                  
__________________________________________________________________________________________________
conv2d_16 (Conv2D)              (None, 256, 256, 128 131200      up_sampling2d_2[0][0]            
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 256, 256, 256 0           conv2d_3[0][0]                   
                                                                 conv2d_16[0][0]                  
__________________________________________________________________________________________________
conv2d_17 (Conv2D)              (None, 256, 256, 128 295040      concatenate_2[0][0]              
__________________________________________________________________________________________________
conv2d_18 (Conv2D)              (None, 256, 256, 128 147584      conv2d_17[0][0]                  
__________________________________________________________________________________________________
up_sampling2d_3 (UpSampling2D)  (None, 512, 512, 128 0           conv2d_18[0][0]                  
__________________________________________________________________________________________________
conv2d_19 (Conv2D)              (None, 512, 512, 64) 32832       up_sampling2d_3[0][0]            
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 512, 512, 128 0           conv2d_1[0][0]                   
                                                                 conv2d_19[0][0]                  
__________________________________________________________________________________________________
conv2d_20 (Conv2D)              (None, 512, 512, 64) 73792       concatenate_3[0][0]              
__________________________________________________________________________________________________
conv2d_21 (Conv2D)              (None, 512, 512, 64) 36928       conv2d_20[0][0]                  
__________________________________________________________________________________________________
conv2d_22 (Conv2D)              (None, 512, 512, 21) 1365        conv2d_21[0][0]                  
==================================================================================================
Total params: 31,033,045
Trainable params: 31,033,045
Non-trainable params: 0
__________________________________________________________________________________________________

```
