# 原创
：  burpsuite模块介绍之decoder

# burpsuite模块介绍之decoder

#### 导语

decoder模块是一个简单的工具，用于将原始数据转换成各种编码和哈希表。它能够智能地识别多种编码格式采用启发式技术。支持的编码解码类型包括：

1. Url
1. HTML
1. Base64
1. ASCII码
1. Hex（十六进制）
1. Octal（八进制）
1. Binary（二进制）
1. GZIP

#### 界面介绍

BurpDecoder是BurpSuite中的一款编码解码工具，用于对原始数据进行各种编码格式和散列的转换。它的界面主要分为三个部分：输入域、输出域和编码解码选项。

1.  输入域（Input Field）：这是你需要输入待解码或待编码的数据的地方。你可以在这里输入需要进行解码或编码的数据，例如URL、文本等。输入域支持文本和Hex两种格式，你可以根据需要选择合适的格式。 
1.  输出域（Output Field）：这是BurpDecoder将处理后的结果显示给你的地方。在进行解码或编码操作后，处理结果将以文本形式显示在输出域中。 
1.  编码解码选项（Encoding/Decoding Options）：这是用于选择编码或解码方式的选项。BurpDecoder提供了多种编码和解码选项，包括但不限于URL编码、Base64编码、HTML实体编码等。你可以根据需要选择相应的解码选项（Decode as）或编码选项（Encode as），以便对数据进行解码或编码操作。此外，还提供了散列（Hash）选项，用于进行散列算法的计算，例如MD5、SHA-1等。&lt;/
