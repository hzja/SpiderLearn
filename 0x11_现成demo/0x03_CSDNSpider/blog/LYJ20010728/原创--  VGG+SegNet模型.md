# 原创
：  VGG+SegNet模型

# VGG+SegNet模型

**搭建模型结构代码**

```
from tensorflow.keras import layers
from tensorflow.keras import models


def VggSegNet(input_shape, num_classes):
    # 输入图片的尺寸
    inputs = layers.Input(shape=input_shape)
    
    # 512,512,3 -&gt; 512,512,64
    conv_1 = layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same')(inputs)
    conv_1 = layers.BatchNormalization()(conv_1)
    conv_1 = layers.Activation('relu')(conv_1)
    conv_2 = layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding='same')(conv_1)
    conv_2 = layers.BatchNormalization()(conv_2)
    conv_2 = layers.Activation('relu')(conv_2)
    
    # 512,512,64 -&gt; 256,256,64
    pool_1 = layers.MaxPooling2D(pool_size=(2,2))(conv_2)

    # 256,256,64 -&gt; 256,256,128
    conv_3 = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding='same')(pool_1)
    conv_3 = layers.BatchNormalization()(conv_3)
    conv_3 = layers.Activation('relu')(conv_3)
    conv_4 = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding='same')(conv_3)
    conv_4 = layers.BatchNormalization()(conv_4)
    conv_4 = layers.Activation('relu')(conv_4)

    # 256,256,128 -&gt; 128,128,128
    pool_2 = layers.MaxPooling2D(pool_size=(2,2))(conv_4)

    # 128,128,128 -&gt; 128,128,256
    conv_5 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='same')(pool_2)
    conv_5 = layers.BatchNormalization()(conv_5)
    conv_5 = layers.Activation('relu')(conv_5)
    conv_6 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='same')(conv_5)
    conv_6 = layers.BatchNormalization()(conv_6)
    conv_6 = layers.Activation('relu')(conv_6)
    conv_7 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='same')(conv_6)
    conv_7 = layers.BatchNormalization()(conv_7)
    conv_7 = layers.Activation('relu')(conv_7)

    # 128,128,256 -&gt; 64,64,256
    pool_3 = layers.MaxPooling2D(pool_size=(2,2))(conv_7)

    # 64,64,256 -&gt; 64,64,512
    conv_8 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding='same')(pool_3)
    conv_8 = layers.BatchNormalization()(conv_8)
    conv_8 = layers.Activation('relu')(conv_8)
    conv_9 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding='same')(conv_8)
    conv_9 = layers.BatchNormalization()(conv_9)
    conv_9 = layers.Activation('relu')(conv_9)
    conv_10 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1) ,padding='same')(conv_9)
    conv_10 = layers.BatchNormalization()(conv_10)
    conv_10 = layers.Activation('relu')(conv_10)

    # 64,64,512 -&gt; 32,32,512
    pool_4 = layers.MaxPooling2D(pool_size=(2,2))(conv_10)

    # 32,32,512 -&gt; 32,32,512
    conv_11 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding='same')(pool_4)
    conv_11 = layers.BatchNormalization()(conv_11)
    conv_11 = layers.Activation('relu')(conv_11)
    conv_12 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding='same')(conv_11)
    conv_12 = layers.BatchNormalization()(conv_12)
    conv_12 = layers.Activation('relu')(conv_12)
    conv_13 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding='same')(conv_12)
    conv_13 = layers.BatchNormalization()(conv_13)
    conv_13 = layers.Activation('relu')(conv_13)

    pool_5 = layers.MaxPooling2D(pool_size=(2,2))(conv_13)


    # 32,32,512 -&gt; 64,64,512
    unpool_1 = layers.UpSampling2D(size=(2,2))(pool_5)

    # 64,64,512 -&gt; 
    conv_14 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding="same")(unpool_1)
    conv_14 = layers.BatchNormalization()(conv_14)
    conv_14 = layers.Activation("relu")(conv_14)
    conv_15 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding="same")(conv_14)
    conv_15 = layers.BatchNormalization()(conv_15)
    conv_15 = layers.Activation("relu")(conv_15)
    conv_16 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding="same")(conv_15)
    conv_16 = layers.BatchNormalization()(conv_16)
    conv_16 = layers.Activation("relu")(conv_16)

    unpool_2 = layers.UpSampling2D(size=(2,2))(conv_16)

    conv_17 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding="same")(unpool_2)
    conv_17 = layers.BatchNormalization()(conv_17)
    conv_17 = layers.Activation("relu")(conv_17)
    conv_18 = layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding="same")(conv_17)
    conv_18 = layers.BatchNormalization()(conv_18)
    conv_18 = layers.Activation("relu")(conv_18)
    conv_19 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding="same")(conv_18)
    conv_19 = layers.BatchNormalization()(conv_19)
    conv_19 = layers.Activation("relu")(conv_19)

    unpool_3 = layers.MaxPooling2D(pool_size=(2,2))(conv_19)

    conv_20 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding="same")(unpool_3)
    conv_20 = layers.BatchNormalization()(conv_20)
    conv_20 = layers.Activation("relu")(conv_20)
    conv_21 = layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding="same")(conv_20)
    conv_21 = layers.BatchNormalization()(conv_21)
    conv_21 = layers.Activation("relu")(conv_21)
    conv_22 = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding="same")(conv_21)
    conv_22 = layers.BatchNormalization()(conv_22)
    conv_22 = layers.Activation("relu")(conv_22)

    unpool_4 = layers.MaxPooling2D(pool_size=(2,2))(conv_22)

    conv_23 = layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding="same")(unpool_4)
    conv_23 = layers.BatchNormalization()(conv_23)
    conv_23 = layers.Activation("relu")(conv_23)
    conv_24 = layers.Conv2D(64, kernel_size=(3,3), strides=(1,1), padding="same")(conv_23)
    conv_24 = layers.BatchNormalization()(conv_24)
    conv_24 = layers.Activation("relu")(conv_24)

    unpool_5 = layers.MaxPooling2D(pool_size=(2,2))(conv_24)

    conv_25 = layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding="same")(unpool_5)
    conv_25 = layers.BatchNormalization()(conv_25)
    conv_25 = layers.Activation("relu")(conv_25)

    conv_26 = layers.Conv2D(filters=num_classes, kernel_size=(1, 1), strides=(1,1), padding="valid")(conv_25)
    conv_26 = layers.BatchNormalization()(conv_26)
#     conv_26 = Reshape(
#         (input_shape[0] * input_shape[1], n_labels),
#         input_shape=(input_shape[0], input_shape[1], n_labels),
#     )(conv_26)

    outputs = layers.Activation('softmax')(conv_26)
    
    model = models.Model(inputs=inputs, outputs=outputs)
    return model

```

**测试模型并的出模型结构层次**

```
input_size = (512,512,3)
num_classes = 21
model = VggSegNet(input_size, num_classes)
model.summary()

```

```
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 512, 512, 3)]     0         
_________________________________________________________________
conv2d (Conv2D)              (None, 512, 512, 64)      1792      
_________________________________________________________________
batch_normalization (BatchNo (None, 512, 512, 64)      256       
_________________________________________________________________
activation (Activation)      (None, 512, 512, 64)      0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 512, 512, 64)      36928     
_________________________________________________________________
batch_normalization_1 (Batch (None, 512, 512, 64)      256       
_________________________________________________________________
activation_1 (Activation)    (None, 512, 512, 64)      0         
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 256, 256, 64)      0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 256, 256, 128)     73856     
_________________________________________________________________
batch_normalization_2 (Batch (None, 256, 256, 128)     512       
_________________________________________________________________
activation_2 (Activation)    (None, 256, 256, 128)     0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 256, 256, 128)     147584    
_________________________________________________________________
batch_normalization_3 (Batch (None, 256, 256, 128)     512       
_________________________________________________________________
activation_3 (Activation)    (None, 256, 256, 128)     0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 128, 128, 128)     0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 128, 128, 256)     295168    
_________________________________________________________________
batch_normalization_4 (Batch (None, 128, 128, 256)     1024      
_________________________________________________________________
activation_4 (Activation)    (None, 128, 128, 256)     0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 128, 128, 256)     590080    
_________________________________________________________________
batch_normalization_5 (Batch (None, 128, 128, 256)     1024      
_________________________________________________________________
activation_5 (Activation)    (None, 128, 128, 256)     0         
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 128, 128, 256)     590080    
_________________________________________________________________
batch_normalization_6 (Batch (None, 128, 128, 256)     1024      
_________________________________________________________________
activation_6 (Activation)    (None, 128, 128, 256)     0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 64, 64, 256)       0         
_________________________________________________________________
conv2d_7 (Conv2D)            (None, 64, 64, 512)       1180160   
_________________________________________________________________
batch_normalization_7 (Batch (None, 64, 64, 512)       2048      
_________________________________________________________________
activation_7 (Activation)    (None, 64, 64, 512)       0         
_________________________________________________________________
conv2d_8 (Conv2D)            (None, 64, 64, 512)       2359808   
_________________________________________________________________
batch_normalization_8 (Batch (None, 64, 64, 512)       2048      
_________________________________________________________________
activation_8 (Activation)    (None, 64, 64, 512)       0         
_________________________________________________________________
conv2d_9 (Conv2D)            (None, 64, 64, 512)       2359808   
_________________________________________________________________
batch_normalization_9 (Batch (None, 64, 64, 512)       2048      
_________________________________________________________________
activation_9 (Activation)    (None, 64, 64, 512)       0         
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_10 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_10 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_10 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_11 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_11 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_11 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_12 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_12 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_12 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 16, 16, 512)       0         
_________________________________________________________________
up_sampling2d (UpSampling2D) (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_13 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_13 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_13 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_14 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_14 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_14 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
conv2d_15 (Conv2D)           (None, 32, 32, 512)       2359808   
_________________________________________________________________
batch_normalization_15 (Batc (None, 32, 32, 512)       2048      
_________________________________________________________________
activation_15 (Activation)   (None, 32, 32, 512)       0         
_________________________________________________________________
up_sampling2d_1 (UpSampling2 (None, 64, 64, 512)       0         
_________________________________________________________________
conv2d_16 (Conv2D)           (None, 64, 64, 512)       2359808   
_________________________________________________________________
batch_normalization_16 (Batc (None, 64, 64, 512)       2048      
_________________________________________________________________
activation_16 (Activation)   (None, 64, 64, 512)       0         
_________________________________________________________________
conv2d_17 (Conv2D)           (None, 64, 64, 512)       2359808   
_________________________________________________________________
batch_normalization_17 (Batc (None, 64, 64, 512)       2048      
_________________________________________________________________
activation_17 (Activation)   (None, 64, 64, 512)       0         
_________________________________________________________________
conv2d_18 (Conv2D)           (None, 64, 64, 256)       1179904   
_________________________________________________________________
batch_normalization_18 (Batc (None, 64, 64, 256)       1024      
_________________________________________________________________
activation_18 (Activation)   (None, 64, 64, 256)       0         
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 32, 32, 256)       0         
_________________________________________________________________
conv2d_19 (Conv2D)           (None, 32, 32, 256)       590080    
_________________________________________________________________
batch_normalization_19 (Batc (None, 32, 32, 256)       1024      
_________________________________________________________________
activation_19 (Activation)   (None, 32, 32, 256)       0         
_________________________________________________________________
conv2d_20 (Conv2D)           (None, 32, 32, 256)       590080    
_________________________________________________________________
batch_normalization_20 (Batc (None, 32, 32, 256)       1024      
_________________________________________________________________
activation_20 (Activation)   (None, 32, 32, 256)       0         
_________________________________________________________________
conv2d_21 (Conv2D)           (None, 32, 32, 128)       295040    
_________________________________________________________________
batch_normalization_21 (Batc (None, 32, 32, 128)       512       
_________________________________________________________________
activation_21 (Activation)   (None, 32, 32, 128)       0         
_________________________________________________________________
max_pooling2d_6 (MaxPooling2 (None, 16, 16, 128)       0         
_________________________________________________________________
conv2d_22 (Conv2D)           (None, 16, 16, 128)       147584    
_________________________________________________________________
batch_normalization_22 (Batc (None, 16, 16, 128)       512       
_________________________________________________________________
activation_22 (Activation)   (None, 16, 16, 128)       0         
_________________________________________________________________
conv2d_23 (Conv2D)           (None, 16, 16, 64)        73792     
_________________________________________________________________
batch_normalization_23 (Batc (None, 16, 16, 64)        256       
_________________________________________________________________
activation_23 (Activation)   (None, 16, 16, 64)        0         
_________________________________________________________________
max_pooling2d_7 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
conv2d_24 (Conv2D)           (None, 8, 8, 64)          36928     
_________________________________________________________________
batch_normalization_24 (Batc (None, 8, 8, 64)          256       
_________________________________________________________________
activation_24 (Activation)   (None, 8, 8, 64)          0         
_________________________________________________________________
conv2d_25 (Conv2D)           (None, 8, 8, 21)          1365      
_________________________________________________________________
batch_normalization_25 (Batc (None, 8, 8, 21)          84        
_________________________________________________________________
activation_25 (Activation)   (None, 8, 8, 21)          0         
=================================================================
Total params: 29,460,329
Trainable params: 29,444,415
Non-trainable params: 15,914
_________________________________________________________________

```
