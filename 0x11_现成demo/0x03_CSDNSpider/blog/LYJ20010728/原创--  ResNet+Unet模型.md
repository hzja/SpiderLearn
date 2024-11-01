# 原创
：  ResNet+Unet模型

# ResNet+Unet模型

**搭建模型结构代码**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210407165517164.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

```
from tensorflow.keras import layers
from tensorflow.keras import models

def ResNet(image_input, is_training=True):
    dropout_rate = 0.5 if is_training else 1.0
    
    # (512,512,3) -&gt; (512,512,64)
    y = layers.Conv2D(64, kernel_size=4, strides=1, padding='same', name='resBlock1_convolution1')(image_input)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    y = layers.Dropout(dropout_rate)(y)
    x1 = y
    
    # (512,512,64) -&gt; (256,256,64)
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='same', name='resBlock1_pool')(x1)
    
    # (256,256,64) -&gt; (256,256,128)
    x = layers.Conv2D(128, kernel_size=1, strides=1, padding='same', name='resBlock2_convolution1')(x)
    x = layers.ReLU()(x)
    
    y = layers.Conv2D(128, kernel_size=4, strides=1, padding='same', name='resBlock2_convolution2')(x)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    
    y = layers.Conv2D(128, kernel_size=4, strides=1, padding='same', name='resBlock2_convolution3')(y)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    y = layers.Dropout(dropout_rate)(y)
    x2 = y + x
    
    # (256,256,128) -&gt; (128,128,128)
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='same', name='resBlock2_pool')(x2)
    
    # (128,128,128) -&gt; (128,128,256)
    x = layers.Conv2D(256, kernel_size=1, strides=1, padding='same', name='resBlock3_convolution1')(x)
    x = layers.ReLU()(x)
    
    y = layers.Conv2D(256, kernel_size=4, strides=1, padding='same', name='resBlock3_convolution2')(x)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    
    y = layers.Conv2D(256, kernel_size=4, strides=1, padding='same', name='resBlock3_convolution3')(y)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    y = layers.Dropout(dropout_rate)(y)
    x3 = y + x
    
    # (128,128,256) -&gt; (64,64,256)
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='same', name='resBlock3_pool')(x3)
    
    # (64,64,256) -&gt; (64,64,512)
    x = layers.Conv2D(512, kernel_size=1, strides=1, padding='same', name='resBlock4_convolution1')(x)
    x = layers.ReLU()(x)
    
    y = layers.Conv2D(512, kernel_size=4, strides=1, padding='same', name='resBlock4_convolution2')(x)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    
    y = layers.Conv2D(512, kernel_size=4, strides=1, padding='same', name='resBlock4_convolution3')(y)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    y = layers.Dropout(dropout_rate)(y)
    x4 = y + x
    
    # (64,64,512) -&gt; (32,32,512)
    x = layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='same', name='resBlock4_pool')(x4)
    
    # (32,32,512) -&gt; (32,32,1024)
    x = layers.Conv2D(1024, kernel_size=1, strides=1, padding='same', name='resBlock5_convolution1')(x)
    x = layers.ReLU()(x)
    
    y = layers.Conv2D(1024, kernel_size=4, strides=1, padding='same', name='resBlock5_convolution2')(x)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    
    y = layers.Conv2D(1024, kernel_size=4, strides=1, padding='same', name='resBlock5_convolution3')(y)
    y = layers.BatchNormalization()(y)
    y = layers.ReLU()(y)
    y = layers.Dropout(dropout_rate)(y)
    x5 = y + x
    
    return x1, x2, x3, x4, x5

def Unet(input_shape=(512,512,3), num_classes=4, is_training=True):
    inputs = layers.Input(input_shape)
    dropout_rate = 0.5 if is_training else 1.0
    x1, x2, x3, x4, x5 = ResNet(image_input=inputs, is_training=True)
    
    # (32,32,1024) -&gt; (64,64,1024)
    m = layers.UpSampling2D(size=(2,2))(x5)
#     m = layers.Conv2DTranspose(512, kernel_size=4, name='Conv2DTranspose1')(x5)
    m = layers.BatchNormalization()(m)
    
    # (32,32,512) -&gt; (32,32,512)
    c1 = layers.Concatenate(axis=3)([m, x4])
    
    #
    m = layers.Conv2D(512, kernel_size=1, strides=1, padding='same', name='resBlock6_convolution1')(c1)
    m = layers.ReLU()(m)
    
    n = layers.Conv2D(512, kernel_size=4, strides=1, padding='same', name='resBlock6_convolution2')(m)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    
    n = layers.Conv2D(512, kernel_size=4, strides=1, padding='same', name='resBlock6_convolution3')(n)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    n = layers.Dropout(dropout_rate)(n)
    m1 = m + n
    
    #
    m = layers.UpSampling2D(size=(2,2))(m1)
#     m = layers.Conv2DTranspose(256, kernel_size=4, name='Conv2DTranspose2')(m1)
    m = layers.BatchNormalization()(m)
    
    #
    c2 = layers.Concatenate(axis=3)([m, x3])
    
    #
    m = layers.Conv2D(256, kernel_size=1, strides=1, padding='same', name='resBlock7_convolution1')(c2)
    m = layers.ReLU()(m)
    
    n = layers.Conv2D(256, kernel_size=4, strides=1, padding='same', name='resBlock7_convolution2')(m)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    
    n = layers.Conv2D(256, kernel_size=4, strides=1, padding='same', name='resBlock7_convolution3')(n)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    n = layers.Dropout(dropout_rate)(n)
    m2 = m + n
    
    #
    m = layers.UpSampling2D(size=(2,2))(m2)
#     m = layers.Conv2DTranspose(128, kernel_size=4, name='Conv2DTranspose3')(m2)
    m = layers.BatchNormalization()(m)
    
    #
    c3 = layers.Concatenate(axis=3)([m, x2])
    
    # 
    m = layers.Conv2D(128, kernel_size=1, strides=1, padding='same', name='resBlock8_convolution1')(c3)
    m = layers.ReLU()(m)
    
    n = layers.Conv2D(128, kernel_size=4, strides=1, padding='same', name='resBlock8_convolution2')(m)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    
    n = layers.Conv2D(128, kernel_size=4, strides=1, padding='same', name='resBlock8_convolution3')(n)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    n = layers.Dropout(dropout_rate)(n)
    m3 = m + n
    
    #
    m = layers.UpSampling2D(size=(2,2))(m3)
#     m = layers.Conv2DTranspose(64, kernel_size=4, name='Conv2DTranspose4')(m3)
    m = layers.BatchNormalization()(m)
    
    #
    c4 = layers.Concatenate(axis=3)([m, x1])
    
    #
    m = layers.Conv2D(64, kernel_size=1, strides=1, padding='same', name='resBlock9_convolution1')(c4)
    m = layers.ReLU()(m)
    
    n = layers.Conv2D(64, kernel_size=4, strides=1, padding='same', name='resBlock9_convolution2')(m)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    
    n = layers.Conv2D(64, kernel_size=4, strides=1, padding='same', name='resBlock9_convolution3')(n)
    n = layers.BatchNormalization()(n)
    n = layers.ReLU()(n)
    n = layers.Dropout(dropout_rate)(n)
    m4 = m + n
    
    m5 = layers.Conv2D(num_classes, kernel_size=1, strides=1, padding='same', name='resBlock10_output')(m4)
    
    model = models.Model(inputs=inputs, outputs=m5)
    return model

```

**测试模型并的出模型结构层次**

```
inputs_size = (512,512,3)
num_classes = 4
model = Unet(inputs_size, num_classes)
model.summary()

```

```
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_5 (InputLayer)            [(None, 512, 512, 3) 0                                            
__________________________________________________________________________________________________
resBlock1_convolution1 (Conv2D) (None, 512, 512, 64) 3136        input_5[0][0]                    
__________________________________________________________________________________________________
batch_normalization_44 (BatchNo (None, 512, 512, 64) 256         resBlock1_convolution1[0][0]     
__________________________________________________________________________________________________
re_lu_55 (ReLU)                 (None, 512, 512, 64) 0           batch_normalization_44[0][0]     
__________________________________________________________________________________________________
dropout_20 (Dropout)            (None, 512, 512, 64) 0           re_lu_55[0][0]                   
__________________________________________________________________________________________________
resBlock1_pool (MaxPooling2D)   (None, 256, 256, 64) 0           dropout_20[0][0]                 
__________________________________________________________________________________________________
resBlock2_convolution1 (Conv2D) (None, 256, 256, 128 8320        resBlock1_pool[0][0]             
__________________________________________________________________________________________________
re_lu_56 (ReLU)                 (None, 256, 256, 128 0           resBlock2_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock2_convolution2 (Conv2D) (None, 256, 256, 128 262272      re_lu_56[0][0]                   
__________________________________________________________________________________________________
batch_normalization_45 (BatchNo (None, 256, 256, 128 512         resBlock2_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_57 (ReLU)                 (None, 256, 256, 128 0           batch_normalization_45[0][0]     
__________________________________________________________________________________________________
resBlock2_convolution3 (Conv2D) (None, 256, 256, 128 262272      re_lu_57[0][0]                   
__________________________________________________________________________________________________
batch_normalization_46 (BatchNo (None, 256, 256, 128 512         resBlock2_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_58 (ReLU)                 (None, 256, 256, 128 0           batch_normalization_46[0][0]     
__________________________________________________________________________________________________
dropout_21 (Dropout)            (None, 256, 256, 128 0           re_lu_58[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_16 (TensorFlo [(None, 256, 256, 12 0           dropout_21[0][0]                 
                                                                 re_lu_56[0][0]                   
__________________________________________________________________________________________________
resBlock2_pool (MaxPooling2D)   (None, 128, 128, 128 0           tf_op_layer_AddV2_16[0][0]       
__________________________________________________________________________________________________
resBlock3_convolution1 (Conv2D) (None, 128, 128, 256 33024       resBlock2_pool[0][0]             
__________________________________________________________________________________________________
re_lu_59 (ReLU)                 (None, 128, 128, 256 0           resBlock3_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock3_convolution2 (Conv2D) (None, 128, 128, 256 1048832     re_lu_59[0][0]                   
__________________________________________________________________________________________________
batch_normalization_47 (BatchNo (None, 128, 128, 256 1024        resBlock3_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_60 (ReLU)                 (None, 128, 128, 256 0           batch_normalization_47[0][0]     
__________________________________________________________________________________________________
resBlock3_convolution3 (Conv2D) (None, 128, 128, 256 1048832     re_lu_60[0][0]                   
__________________________________________________________________________________________________
batch_normalization_48 (BatchNo (None, 128, 128, 256 1024        resBlock3_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_61 (ReLU)                 (None, 128, 128, 256 0           batch_normalization_48[0][0]     
__________________________________________________________________________________________________
dropout_22 (Dropout)            (None, 128, 128, 256 0           re_lu_61[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_17 (TensorFlo [(None, 128, 128, 25 0           dropout_22[0][0]                 
                                                                 re_lu_59[0][0]                   
__________________________________________________________________________________________________
resBlock3_pool (MaxPooling2D)   (None, 64, 64, 256)  0           tf_op_layer_AddV2_17[0][0]       
__________________________________________________________________________________________________
resBlock4_convolution1 (Conv2D) (None, 64, 64, 512)  131584      resBlock3_pool[0][0]             
__________________________________________________________________________________________________
re_lu_62 (ReLU)                 (None, 64, 64, 512)  0           resBlock4_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock4_convolution2 (Conv2D) (None, 64, 64, 512)  4194816     re_lu_62[0][0]                   
__________________________________________________________________________________________________
batch_normalization_49 (BatchNo (None, 64, 64, 512)  2048        resBlock4_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_63 (ReLU)                 (None, 64, 64, 512)  0           batch_normalization_49[0][0]     
__________________________________________________________________________________________________
resBlock4_convolution3 (Conv2D) (None, 64, 64, 512)  4194816     re_lu_63[0][0]                   
__________________________________________________________________________________________________
batch_normalization_50 (BatchNo (None, 64, 64, 512)  2048        resBlock4_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_64 (ReLU)                 (None, 64, 64, 512)  0           batch_normalization_50[0][0]     
__________________________________________________________________________________________________
dropout_23 (Dropout)            (None, 64, 64, 512)  0           re_lu_64[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_18 (TensorFlo [(None, 64, 64, 512) 0           dropout_23[0][0]                 
                                                                 re_lu_62[0][0]                   
__________________________________________________________________________________________________
resBlock4_pool (MaxPooling2D)   (None, 32, 32, 512)  0           tf_op_layer_AddV2_18[0][0]       
__________________________________________________________________________________________________
resBlock5_convolution1 (Conv2D) (None, 32, 32, 1024) 525312      resBlock4_pool[0][0]             
__________________________________________________________________________________________________
re_lu_65 (ReLU)                 (None, 32, 32, 1024) 0           resBlock5_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock5_convolution2 (Conv2D) (None, 32, 32, 1024) 16778240    re_lu_65[0][0]                   
__________________________________________________________________________________________________
batch_normalization_51 (BatchNo (None, 32, 32, 1024) 4096        resBlock5_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_66 (ReLU)                 (None, 32, 32, 1024) 0           batch_normalization_51[0][0]     
__________________________________________________________________________________________________
resBlock5_convolution3 (Conv2D) (None, 32, 32, 1024) 16778240    re_lu_66[0][0]                   
__________________________________________________________________________________________________
batch_normalization_52 (BatchNo (None, 32, 32, 1024) 4096        resBlock5_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_67 (ReLU)                 (None, 32, 32, 1024) 0           batch_normalization_52[0][0]     
__________________________________________________________________________________________________
dropout_24 (Dropout)            (None, 32, 32, 1024) 0           re_lu_67[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_19 (TensorFlo [(None, 32, 32, 1024 0           dropout_24[0][0]                 
                                                                 re_lu_65[0][0]                   
__________________________________________________________________________________________________
up_sampling2d_5 (UpSampling2D)  (None, 64, 64, 1024) 0           tf_op_layer_AddV2_19[0][0]       
__________________________________________________________________________________________________
batch_normalization_53 (BatchNo (None, 64, 64, 1024) 4096        up_sampling2d_5[0][0]            
__________________________________________________________________________________________________
concatenate_6 (Concatenate)     (None, 64, 64, 1536) 0           batch_normalization_53[0][0]     
                                                                 tf_op_layer_AddV2_18[0][0]       
__________________________________________________________________________________________________
resBlock6_convolution1 (Conv2D) (None, 64, 64, 512)  786944      concatenate_6[0][0]              
__________________________________________________________________________________________________
re_lu_68 (ReLU)                 (None, 64, 64, 512)  0           resBlock6_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock6_convolution2 (Conv2D) (None, 64, 64, 512)  4194816     re_lu_68[0][0]                   
__________________________________________________________________________________________________
batch_normalization_54 (BatchNo (None, 64, 64, 512)  2048        resBlock6_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_69 (ReLU)                 (None, 64, 64, 512)  0           batch_normalization_54[0][0]     
__________________________________________________________________________________________________
resBlock6_convolution3 (Conv2D) (None, 64, 64, 512)  4194816     re_lu_69[0][0]                   
__________________________________________________________________________________________________
batch_normalization_55 (BatchNo (None, 64, 64, 512)  2048        resBlock6_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_70 (ReLU)                 (None, 64, 64, 512)  0           batch_normalization_55[0][0]     
__________________________________________________________________________________________________
dropout_25 (Dropout)            (None, 64, 64, 512)  0           re_lu_70[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_20 (TensorFlo [(None, 64, 64, 512) 0           re_lu_68[0][0]                   
                                                                 dropout_25[0][0]                 
__________________________________________________________________________________________________
up_sampling2d_6 (UpSampling2D)  (None, 128, 128, 512 0           tf_op_layer_AddV2_20[0][0]       
__________________________________________________________________________________________________
batch_normalization_56 (BatchNo (None, 128, 128, 512 2048        up_sampling2d_6[0][0]            
__________________________________________________________________________________________________
concatenate_7 (Concatenate)     (None, 128, 128, 768 0           batch_normalization_56[0][0]     
                                                                 tf_op_layer_AddV2_17[0][0]       
__________________________________________________________________________________________________
resBlock7_convolution1 (Conv2D) (None, 128, 128, 256 196864      concatenate_7[0][0]              
__________________________________________________________________________________________________
re_lu_71 (ReLU)                 (None, 128, 128, 256 0           resBlock7_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock7_convolution2 (Conv2D) (None, 128, 128, 256 1048832     re_lu_71[0][0]                   
__________________________________________________________________________________________________
batch_normalization_57 (BatchNo (None, 128, 128, 256 1024        resBlock7_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_72 (ReLU)                 (None, 128, 128, 256 0           batch_normalization_57[0][0]     
__________________________________________________________________________________________________
resBlock7_convolution3 (Conv2D) (None, 128, 128, 256 1048832     re_lu_72[0][0]                   
__________________________________________________________________________________________________
batch_normalization_58 (BatchNo (None, 128, 128, 256 1024        resBlock7_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_73 (ReLU)                 (None, 128, 128, 256 0           batch_normalization_58[0][0]     
__________________________________________________________________________________________________
dropout_26 (Dropout)            (None, 128, 128, 256 0           re_lu_73[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_21 (TensorFlo [(None, 128, 128, 25 0           re_lu_71[0][0]                   
                                                                 dropout_26[0][0]                 
__________________________________________________________________________________________________
up_sampling2d_7 (UpSampling2D)  (None, 256, 256, 256 0           tf_op_layer_AddV2_21[0][0]       
__________________________________________________________________________________________________
batch_normalization_59 (BatchNo (None, 256, 256, 256 1024        up_sampling2d_7[0][0]            
__________________________________________________________________________________________________
concatenate_8 (Concatenate)     (None, 256, 256, 384 0           batch_normalization_59[0][0]     
                                                                 tf_op_layer_AddV2_16[0][0]       
__________________________________________________________________________________________________
resBlock8_convolution1 (Conv2D) (None, 256, 256, 128 49280       concatenate_8[0][0]              
__________________________________________________________________________________________________
re_lu_74 (ReLU)                 (None, 256, 256, 128 0           resBlock8_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock8_convolution2 (Conv2D) (None, 256, 256, 128 262272      re_lu_74[0][0]                   
__________________________________________________________________________________________________
batch_normalization_60 (BatchNo (None, 256, 256, 128 512         resBlock8_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_75 (ReLU)                 (None, 256, 256, 128 0           batch_normalization_60[0][0]     
__________________________________________________________________________________________________
resBlock8_convolution3 (Conv2D) (None, 256, 256, 128 262272      re_lu_75[0][0]                   
__________________________________________________________________________________________________
batch_normalization_61 (BatchNo (None, 256, 256, 128 512         resBlock8_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_76 (ReLU)                 (None, 256, 256, 128 0           batch_normalization_61[0][0]     
__________________________________________________________________________________________________
dropout_27 (Dropout)            (None, 256, 256, 128 0           re_lu_76[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_22 (TensorFlo [(None, 256, 256, 12 0           re_lu_74[0][0]                   
                                                                 dropout_27[0][0]                 
__________________________________________________________________________________________________
up_sampling2d_8 (UpSampling2D)  (None, 512, 512, 128 0           tf_op_layer_AddV2_22[0][0]       
__________________________________________________________________________________________________
batch_normalization_62 (BatchNo (None, 512, 512, 128 512         up_sampling2d_8[0][0]            
__________________________________________________________________________________________________
concatenate_9 (Concatenate)     (None, 512, 512, 192 0           batch_normalization_62[0][0]     
                                                                 dropout_20[0][0]                 
__________________________________________________________________________________________________
resBlock9_convolution1 (Conv2D) (None, 512, 512, 64) 12352       concatenate_9[0][0]              
__________________________________________________________________________________________________
re_lu_77 (ReLU)                 (None, 512, 512, 64) 0           resBlock9_convolution1[0][0]     
__________________________________________________________________________________________________
resBlock9_convolution2 (Conv2D) (None, 512, 512, 64) 65600       re_lu_77[0][0]                   
__________________________________________________________________________________________________
batch_normalization_63 (BatchNo (None, 512, 512, 64) 256         resBlock9_convolution2[0][0]     
__________________________________________________________________________________________________
re_lu_78 (ReLU)                 (None, 512, 512, 64) 0           batch_normalization_63[0][0]     
__________________________________________________________________________________________________
resBlock9_convolution3 (Conv2D) (None, 512, 512, 64) 65600       re_lu_78[0][0]                   
__________________________________________________________________________________________________
batch_normalization_64 (BatchNo (None, 512, 512, 64) 256         resBlock9_convolution3[0][0]     
__________________________________________________________________________________________________
re_lu_79 (ReLU)                 (None, 512, 512, 64) 0           batch_normalization_64[0][0]     
__________________________________________________________________________________________________
dropout_28 (Dropout)            (None, 512, 512, 64) 0           re_lu_79[0][0]                   
__________________________________________________________________________________________________
tf_op_layer_AddV2_23 (TensorFlo [(None, 512, 512, 64 0           re_lu_77[0][0]                   
                                                                 dropout_28[0][0]                 
__________________________________________________________________________________________________
resBlock10_output (Conv2D)      (None, 512, 512, 4)  260         tf_op_layer_AddV2_23[0][0]       
==================================================================================================
Total params: 57,489,412
Trainable params: 57,473,924
Non-trainable params: 15,488
__________________________________________________________________________________________________
​

```
