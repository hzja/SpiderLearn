# 原创
：  【web-避开客户端控件】（2.3.2）收集使用数据：拦截浏览器扩展的流量

# 【web-避开客户端控件】（2.3.2）收集使用数据：拦截浏览器扩展的流量

**目录**

[拦截浏览器扩展的流量](#%E6%8B%A6%E6%88%AA%E6%B5%8F%E8%A7%88%E5%99%A8%E6%89%A9%E5%B1%95%E7%9A%84%E6%B5%81%E9%87%8F)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、测试扩展组件的障碍](#1.2%E3%80%81%E6%B5%8B%E8%AF%95%E6%89%A9%E5%B1%95%E7%BB%84%E4%BB%B6%E7%9A%84%E9%9A%9C%E7%A2%8D)

[处理序列化数据](#%E5%A4%84%E7%90%86%E5%BA%8F%E5%88%97%E5%8C%96%E6%95%B0%E6%8D%AE)

[序列化格式](#%E5%BA%8F%E5%88%97%E5%8C%96%E6%A0%BC%E5%BC%8F)

[1.3、拦截扩展流量的障碍](#1.3%E3%80%81%E6%8B%A6%E6%88%AA%E6%89%A9%E5%B1%95%E6%B5%81%E9%87%8F%E7%9A%84%E9%9A%9C%E7%A2%8D)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

---


## 拦截浏览器扩展的流量

> 
<h3>1.1、简介：</h3>
浏览器配置为使用拦截代理服务器， 并且应用程序使用浏览器扩展加载客户端组件，该组件提出的请求将经过代理服务器。这时就可以开始测试相关功能，以常规方式拦截并修改组件提出的请求
在需要避开在浏览器扩展中实施的客户端输入确认的情况下， 如果组件以透明方式向服务器提供经过确认的数据，可以直接使用拦截代理服务器修改这些数据。
支持身份验证机制的浏览器扩展可能会收集用户证书， 并对这些证书进行确认， 然后在请求中以明文（或处理后的形式）参数的形式向服务器提交这些证书。攻击者不需要对组件本身进行任何分析或攻击， 就可以轻松解除这种确认


### 1.2、测试扩展组件的障碍

> 
<h4>处理序列化数据</h4>
应用程序可能会首先对数据或对象进行序列化处理，然后再通过HTTP请求传送这些数据或对象。
通过检查原始的序列化数据，可以解译一些基于字符串的数据， 但是，需要对序列化数据进行解压缩才能了解这些数据。（修改这些数据， 以破坏应用程序的处理过程）需要解压缩序列化内容， 对其进行必要的编辑， 然后重新对其进行序列化处理。直接编辑原始的序列化数据将破坏其格式， 并在应用程序处理请求时导致解析错误

每种浏览器扩展技术都具有各自处理HTTP消息中数据的序列化方案。通常可以根据所采用的客户端组件推断出相关数据的序列化格式，仔细检查相关HTTP消息才能确认序列化格式


> 
<h4>序列化格式</h4>
**1、Java序列化**
Java语言本身支持对象序列化，Java applet可能会以这种方式在客户端与服务器应用程序组件之间传送序列化数据结构。包含序列化Java对象的消息很容易辨别，它们使用以下消息头
Content-Type:application/x-java-serialized-object

使用代理服务器拦截原始的序列化数据后， 就可以通过Java对这些数据进行去序列化处理，以查看其中包含的原语数据项。
Dser是Bp中的一个插件， 该插件提供一个框架，可用于查看和处理Bp中拦截的序列化Java对象。该工具将拦截到的对象中的原语数据转换为XML格式， 以便于进行编辑。编辑相关数据后，Dser将重新对对象进行序列化， 并对HTTP请求进行相应的更新。
<hr/>
**2、Flash序列化**
Flash使用自己的可用于在服务器和客户端组件之间传输复杂数据结构的序列化格式。通过以下消息头辨别动作信息格式(AMF)
Content-Type:application/x-amf

Bp本身支持AMF格式。确定包含序列化AMF数据的HTTP请求或响应后， 它会解压缩并以树状形式显示相关内容， 以便于查看和编辑。在修改结构中的相关原语数据项后，Bp将重新对消息进行序列化，然后就可以将该消息转发给服务器或客户端， 由它们进行处理
<hr/>
**3、Silverligh序列化**
Silverligh应用程序能够利用NET平台内置的windows通信基础(WCF)远程框架。使用WCF的Silverligh客户端组件通常采用微软的用于SOAP的NET二进制格式( NBFS)。通过以下消息头辨别该格式
Content-Type:application/soap+msbin1
bp中的一个插件能够自动对NBFS编辑的数据进行去序列化， 然后在Bp的拦截窃口中显示这些数据。在查看或编辑已解码的数据后， 该插件会对数据项新进行编辑， 然后将数据转发给服务器或客户端， 由它们进行处理。


---


### 1.3、拦截扩展流量的障碍

> 
<h4>简介：</h4>
1、代理服务器可能并不会拦截或无法拦截浏览器扩展组件提出的请求
可能是由于组件的HTTP代理或SSL出现问题， 或者二者同时出现问题（仔细配置代理服务器）
<hr/>
2、客户端组件可能并不执行在浏览器或计算机的设置中指定的代理配置
组件可能会在浏览器本身或扩展框架提供的API以外发出它们自己的HTTP请求。出现这种情况仍然可以拦截组件的请求，需要修改计算机的hosts文件以实现拦截目的， 同时将代理服务器配置为支持匿名代理， 并自动重定向到正确的目标主机
<hr/>
3、客户端组件可能不接受拦截代理服务器提供的SSL证书。即使代理服务器使用的是一般自签名证书， 并且浏览器已配置为接受这类证书， 但浏览器扩展组件仍有可能拒绝此类证书。
可能是因为浏览器扩展组件不接受浏览器在暂时可信的证书方面的配置， 或组件本身以编程方式要求拒绝接受不可信的证书。可以将代理服务器配置为使用一个主CA证书（用于为访问的每个站点的每台主机签署有效的证书）， 并在计算机的可信证书库中安装该CA证书
<hr/>
4、客户端组件还使用除HTTP以外的协议进行通信， 而拦截代理服务器却无法处理这些协议
可以通过使用网络嗅探器或功能挂钩工具查看并修改相关流量Echo Mirage就是一个这样的工具， 它能够注入进程并拦截套接字API调用， 以便查看并修改数据，然后通过网络传送修改后的数据


---

