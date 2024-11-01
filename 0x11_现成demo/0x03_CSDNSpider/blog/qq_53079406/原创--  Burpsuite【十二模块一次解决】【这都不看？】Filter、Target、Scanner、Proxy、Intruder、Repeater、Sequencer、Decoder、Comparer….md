# 原创
：  Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…

# Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…

**目录**

[Filter showing all items（过滤器）](#Filter%20showing%20all%20items%EF%BC%88%E8%BF%87%E6%BB%A4%E5%99%A8%EF%BC%89)

[筛选功能：](#%E7%AD%9B%E9%80%89%E5%8A%9F%E8%83%BD%EF%BC%9A)

[过滤器在哪呢？](#%E8%BF%87%E6%BB%A4%E5%99%A8%E5%9C%A8%E5%93%AA%E5%91%A2%EF%BC%9F)

[你使用过滤器了嘛？](#%E4%BD%A0%E4%BD%BF%E7%94%A8%E8%BF%87%E6%BB%A4%E5%99%A8%E4%BA%86%E5%98%9B%EF%BC%9F)

[Target（目标）](#Target%EF%BC%88%E7%9B%AE%E6%A0%87%EF%BC%89)

[URL不同颜色，它的区别是？](#URL%E4%B8%8D%E5%90%8C%E9%A2%9C%E8%89%B2%EF%BC%8C%E5%AE%83%E7%9A%84%E5%8C%BA%E5%88%AB%E6%98%AF%EF%BC%9F)

[如何查看一个/多个指定的URL地址？](#%E5%A6%82%E4%BD%95%E6%9F%A5%E7%9C%8B%E4%B8%80%E4%B8%AA%2F%E5%A4%9A%E4%B8%AA%E6%8C%87%E5%AE%9A%E7%9A%84URL%E5%9C%B0%E5%9D%80%EF%BC%9F)

[scope（范围）](#2.scope%EF%BC%88%E8%8C%83%E5%9B%B4%EF%BC%89)

[将指定URL添加/删除scope（范围）的方法？](#%E5%B0%86%E6%8C%87%E5%AE%9AURL%E6%B7%BB%E5%8A%A0%2F%E5%88%A0%E9%99%A4scope%EF%BC%88%E8%8C%83%E5%9B%B4%EF%BC%89%E7%9A%84%E6%96%B9%E6%B3%95%EF%BC%9F)

[Scanner（扫描）](#Scanner%EF%BC%88%E6%89%AB%E6%8F%8F%EF%BC%89)

[在哪开始scanner（扫描）/spider（爬取）？](#%E5%9C%A8%E5%93%AA%E5%BC%80%E5%A7%8Bscanner%EF%BC%88%E6%89%AB%E6%8F%8F%EF%BC%89%2Fspider%EF%BC%88%E7%88%AC%E5%8F%96%EF%BC%89%EF%BC%9F)

[怎么开始相关scanner（扫描）或者spider（爬取）？](#%E6%80%8E%E4%B9%88%E5%BC%80%E5%A7%8B%E7%9B%B8%E5%85%B3scanner%EF%BC%88%E6%89%AB%E6%8F%8F%EF%BC%89%E6%88%96%E8%80%85spider%EF%BC%88%E7%88%AC%E5%8F%96%EF%BC%89%EF%BC%9F)

[在哪查看扫描和爬取的相关信息？](#%E5%9C%A8%E5%93%AA%E6%9F%A5%E7%9C%8B%E6%89%AB%E6%8F%8F%E5%92%8C%E7%88%AC%E5%8F%96%E7%9A%84%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF%EF%BC%9F)

[Proxy（代理）](#Proxy%EF%BC%88%E4%BB%A3%E7%90%86%EF%BC%89)

[intercept（截断）](#intercept%EF%BC%88%E6%88%AA%E6%96%AD%EF%BC%89)

[对于截取信息的分析和处理](#%E5%AF%B9%E4%BA%8E%E6%88%AA%E5%8F%96%E4%BF%A1%E6%81%AF%E7%9A%84%E5%88%86%E6%9E%90%E5%92%8C%E5%A4%84%E7%90%86)

[选项1：Raw](#%E9%80%89%E9%A1%B91%EF%BC%9ARaw)

[选项2：params（参数）](#%E9%80%89%E9%A1%B92%EF%BC%9Aparams%EF%BC%88%E5%8F%82%E6%95%B0%EF%BC%89)

[选项3：headers](#%E9%80%89%E9%A1%B93%EF%BC%9Aheaders)

[选项4：hex](#%E9%80%89%E9%A1%B94%EF%BC%9Ahex%3A)

[对于数据包的执行处理](#%E5%AF%B9%E4%BA%8E%E6%95%B0%E6%8D%AE%E5%8C%85%E7%9A%84%E6%89%A7%E8%A1%8C%E5%A4%84%E7%90%86)

[ 选项1：Forward（放包）](#%E9%80%89%E9%A1%B91%EF%BC%9AForward%EF%BC%88%E6%94%BE%E5%8C%85%EF%BC%89)

[选项2：Drop（废包）](#%E9%80%89%E9%A1%B92%EF%BC%9ADrop%EF%BC%88%E5%BA%9F%E5%8C%85%EF%BC%89)

[选项3：Interceptionis on/off（拦截  请求/关闭）](#%E9%80%89%E9%A1%B93%EF%BC%9AInterceptionis%20on%2Foff%EF%BC%88%E6%8B%A6%E6%88%AA%C2%A0%20%E8%AF%B7%E6%B1%82%2F%E5%85%B3%E9%97%AD%EF%BC%89)

[选项4：Action（行动）](#%E9%80%89%E9%A1%B94%EF%BC%9AAction%EF%BC%88%E8%A1%8C%E5%8A%A8%EF%BC%89)

[选项5：评论和染色](#%E9%80%89%E9%A1%B95%EF%BC%9A%E8%AF%84%E8%AE%BA%E5%92%8C%E6%9F%93%E8%89%B2)

[数据包的更多执行模块使用：](#%E6%95%B0%E6%8D%AE%E5%8C%85%E7%9A%84%E6%9B%B4%E5%A4%9A%E6%89%A7%E8%A1%8C%E6%A8%A1%E5%9D%97%E4%BD%BF%E7%94%A8%EF%BC%9A)

[英语基础： ](#%E8%8B%B1%E8%AF%AD%E5%9F%BA%E7%A1%80%EF%BC%9A%C2%A0)

[相关处理操作：](#%E7%9B%B8%E5%85%B3%E5%A4%84%E7%90%86%E6%93%8D%E4%BD%9C%EF%BC%9A)

[选项1.Change request method（变更请求方法）：](#1.Change%20request%20method%EF%BC%88%E5%8F%98%E6%9B%B4%E8%AF%B7%E6%B1%82%E6%96%B9%E6%B3%95%EF%BC%89%EF%BC%9A)

[选项2.Change body encoding（身体编码改变）：](#2.Change%20body%20encoding%EF%BC%88%E8%BA%AB%E4%BD%93%E7%BC%96%E7%A0%81%E6%94%B9%E5%8F%98%EF%BC%89%EF%BC%9A)

[选项3.Copy URL （复制网址）](#3.Copy%20URL%C2%A0%EF%BC%88%E5%A4%8D%E5%88%B6%E7%BD%91%E5%9D%80%EF%BC%89)

[选项4.Cope as curl command（复制curl命令）](#4.Cope%20as%20curl%20command%EF%BC%88%E5%A4%8D%E5%88%B6curl%E5%91%BD%E4%BB%A4%EF%BC%89)

[选项5.Cope to file（复制到文件）：](#5.Cope%20to%20file%EF%BC%88%E5%A4%8D%E5%88%B6%E5%88%B0%E6%96%87%E4%BB%B6%EF%BC%89%EF%BC%9A)

[选项6.Pase form file（从文件粘贴）：](#6.Pase%20form%20file%EF%BC%88%E4%BB%8E%E6%96%87%E4%BB%B6%E7%B2%98%E8%B4%B4%EF%BC%89%EF%BC%9A)

[选项7.Save item（保存项目）：](#7.Save%20item%EF%BC%88%E4%BF%9D%E5%AD%98%E9%A1%B9%E7%9B%AE%EF%BC%89%EF%BC%9A)

[拦截：](#%E6%8B%A6%E6%88%AA%EF%BC%9A)

[选项1.Don't intercept requests（请求不要拦截）：](#1.Don'%20rel=)

[选项2.Do intercept（拦截执行）：](#2.Do%20intercept%EF%BC%88%E6%8B%A6%E6%88%AA%E6%89%A7%E8%A1%8C%EF%BC%89%EF%BC%9A)

[选项3.Convert seiection（转换）：](#3.Convert%20seiection%EF%BC%88%E8%BD%AC%E6%8D%A2%EF%BC%89%EF%BC%9A)

[选项4.URL-encode as you type（URL编码输入）：](#4.URL-encode%20as%20you%20type%EF%BC%88URL%E7%BC%96%E7%A0%81%E8%BE%93%E5%85%A5%EF%BC%89%EF%BC%9A)

[基操：](#%E5%9F%BA%E6%93%8D%EF%BC%9A)

[HTTP History](#%E9%80%89%E9%A1%B92%EF%BC%9AHTTP%20History)

[如何处理相关HTTP History信息？](#%E5%A6%82%E4%BD%95%E5%A4%84%E7%90%86%E7%9B%B8%E5%85%B3HTTP%20History%E4%BF%A1%E6%81%AF%EF%BC%9F)

[WebSockets history（WebSockets历史记录）](#%E9%80%89%E9%A1%B93%EF%BC%9AWebSockets%20history%EF%BC%88WebSockets%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95%EF%BC%89)

[简单介绍下WebSockets history 喽](#%E7%AE%80%E5%8D%95%E4%BB%8B%E7%BB%8D%E4%B8%8BWebSockets%20history%20%E5%96%BD)

[Options（选项）](#%E9%80%89%E9%A1%B94%EF%BC%9AOptions%EF%BC%88%E9%80%89%E9%A1%B9%EF%BC%89)

[英语基础：](#%E8%8B%B1%E8%AF%AD%E5%9F%BA%E7%A1%80%EF%BC%9A)

[OPtions大全介绍](#OPtions%E5%A4%A7%E5%85%A8%E4%BB%8B%E7%BB%8D)

[选项1、Proxy Listeners（代理监听器）](#Proxy%20Listeners%EF%BC%88%E4%BB%A3%E7%90%86%E7%9B%91%E5%90%AC%E5%99%A8%EF%BC%89)

[选项2：Intercept Client Requests（拦截客户端请求）](#%E9%80%89%E9%A1%B92%EF%BC%9AIntercept%20Client%20Requests%EF%BC%88%E6%8B%A6%E6%88%AA%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%AF%B7%E6%B1%82%EF%BC%89)

[选项3：Intercept Server Responses（拦截服务器响应）](#%E9%80%89%E9%A1%B93%EF%BC%9AIntercept%20Server%20Responses%EF%BC%88%E6%8B%A6%E6%88%AA%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%93%8D%E5%BA%94%EF%BC%89)

[选项4：Intercept WebSockets Messages（拦截WebSockets消息）](#%E9%80%89%E9%A1%B94%EF%BC%9AIntercept%20WebSockets%20Messages%EF%BC%88%E6%8B%A6%E6%88%AAWebSockets%E6%B6%88%E6%81%AF%EF%BC%89)

[选项5：Response Modification（响应修改操作）](#%E9%80%89%E9%A1%B95%EF%BC%9AResponse%20Modification%EF%BC%88%E5%93%8D%E5%BA%94%E4%BF%AE%E6%94%B9%E6%93%8D%E4%BD%9C%EF%BC%89)

[选项6：Match and replace（匹配和替换）](#%E9%80%89%E9%A1%B96%EF%BC%9AMatch%20and%20replace%EF%BC%88%E5%8C%B9%E9%85%8D%E5%92%8C%E6%9B%BF%E6%8D%A2%EF%BC%89)

[选项7：SSL Pass Through（SSL通过）](#%E9%80%89%E9%A1%B97%EF%BC%9ASSL%20Pass%20Through%EF%BC%88SSL%E9%80%9A%E8%BF%87%EF%BC%89)

[选项8：Miscellaneous](#%E9%80%89%E9%A1%B98%EF%BC%9AMiscellaneous)

[Intruder（测试器）](#Intruder%EF%BC%88%E6%B5%8B%E8%AF%95%E5%99%A8%EF%BC%89)

[Target（目标）](#Target%EF%BC%88%E7%9B%AE%E6%A0%87%EF%BC%89)

[Positions（位置）](#Positions%EF%BC%88%E4%BD%8D%E7%BD%AE%EF%BC%89)

[选项1、Payload Positions（有效载荷位置）](#Payload%20Positions%EF%BC%88%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%E4%BD%8D%E7%BD%AE%EF%BC%89)

[选项2、Attack type（攻击类型）：](#Attack%20type%EF%BC%88%E6%94%BB%E5%87%BB%E7%B1%BB%E5%9E%8B%EF%BC%89%EF%BC%9A)

[Payloads（有效载荷）](#Payloads%EF%BC%88%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%EF%BC%89)

[ 选项1、Payload Sets（设置）](#Payload%20Sets%EF%BC%88%E8%AE%BE%E7%BD%AE%EF%BC%89)

[选项2、Payload Options（有效载荷选项）](#Payload%20Options%EF%BC%88%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%E9%80%89%E9%A1%B9%EF%BC%89)

[选项3、Payload Processing（有效载荷处理）](#Payload%C2%A0Processing%EF%BC%88%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%E5%A4%84%E7%90%86%EF%BC%89)

[选项4、Payload Encoding（有效载荷编码）](#Payload%20Encoding%EF%BC%88%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%E7%BC%96%E7%A0%81%EF%BC%89)

[Options（选项）](#Options%EF%BC%88%E9%80%89%E9%A1%B9%EF%BC%89)

[选项1、Request Headers（请求标头）](#Request%20Headers%EF%BC%88%E8%AF%B7%E6%B1%82%E6%A0%87%E5%A4%B4%EF%BC%89)

[选项2、Request Engine（请求引擎）](#Request%20Engine%EF%BC%88%E8%AF%B7%E6%B1%82%E5%BC%95%E6%93%8E%EF%BC%89)

[选项3、Attack Results（攻击结果）](#Attack%20Results%EF%BC%88%E6%94%BB%E5%87%BB%E7%BB%93%E6%9E%9C%EF%BC%89)

[选项4、Grep - Match](#Grep%20-%20Match)

[选项5、Grep - Extract（提取物）](#Grep%20-%20Extract%EF%BC%88%E6%8F%90%E5%8F%96%E7%89%A9%EF%BC%89)

[选项6、Grep - Payloads（Grep有效载荷）](#Grep%20-%20Payloads%EF%BC%88Grep%E6%9C%89%E6%95%88%E8%BD%BD%E8%8D%B7%EF%BC%89)

[选项7、Redirections（重定向）](#Redirections%EF%BC%88%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%89)

[Repeater（重发器）](#Repeater%EF%BC%88%E9%87%8D%E5%8F%91%E5%99%A8%EF%BC%89)

[Repeater介绍一下吧](#Repeater%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%E5%90%A7)

[英语基础：](#%E8%8B%B1%E8%AF%AD%E5%9F%BA%E7%A1%80%EF%BC%9A)

[Sequencer模块(定序器)](#articleContentId)

[Live capture 信息截取](#1%EF%BC%9ALive%20capture%20%E4%BF%A1%E6%81%AF%E6%88%AA%E5%8F%96)

[ 选项1：Select Live Capture Request（选择实时捕获请求）](#%E9%80%89%E9%A1%B91%EF%BC%9ASelect%20Live%20Capture%20Request%EF%BC%88%E9%80%89%E6%8B%A9%E5%AE%9E%E6%97%B6%E6%8D%95%E8%8E%B7%E8%AF%B7%E6%B1%82%EF%BC%89)

[选项2：Token Location Within Response  （响应中的令牌位置）](#%E9%80%89%E9%A1%B92%EF%BC%9AToken%20Location%20Within%20Response%C2%A0%20%EF%BC%88%E5%93%8D%E5%BA%94%E4%B8%AD%E7%9A%84%E4%BB%A4%E7%89%8C%E4%BD%8D%E7%BD%AE%EF%BC%89)

[选项3：Live Capture Options （实时捕获选项）](#%E9%80%89%E9%A1%B93%EF%BC%9ALive%20Capture%20Options%20%EF%BC%88%E5%AE%9E%E6%97%B6%E6%8D%95%E8%8E%B7%E9%80%89%E9%A1%B9%EF%BC%89)

[Manual load 手动加载](#2%EF%BC%9AManual%20load%20%E6%89%8B%E5%8A%A8%E5%8A%A0%E8%BD%BD)

[选项1：Manual Load（手动阅读）](#%E9%80%89%E9%A1%B91%EF%BC%9AManual%20Load%EF%BC%88%E6%89%8B%E5%8A%A8%E9%98%85%E8%AF%BB%EF%BC%89)

[Analysis options 选项分析](#3%EF%BC%9AAnalysis%20options%20%E9%80%89%E9%A1%B9%E5%88%86%E6%9E%90)

[ 选项1：Token Handling  (令牌处理)](#%E9%80%89%E9%A1%B91%EF%BC%9AToken%20Handling%C2%A0%20%28%E4%BB%A4%E7%89%8C%E5%A4%84%E7%90%86%29)

[选项2：Token Analysis  （令牌分析)](#%E9%80%89%E9%A1%B92%EF%BC%9AToken%20Analysis%C2%A0%20%EF%BC%88%E4%BB%A4%E7%89%8C%E5%88%86%E6%9E%90%29)

[Decoder(编码器)](#Decoder%28%E7%BC%96%E7%A0%81%E5%99%A8%29)

[Comparer（对比器）](#Comparer%EF%BC%88%E5%AF%B9%E6%AF%94%E5%99%A8%EF%BC%89)

[Comparer基操：](#Comparer%E5%9F%BA%E6%93%8D%EF%BC%9A)

[Extender(扩展器)](#articleContentId)

[扩展是万能的，没扩展是万万不能的](#%E6%89%A9%E5%B1%95%E6%98%AF%E4%B8%87%E8%83%BD%E7%9A%84%EF%BC%8C%E6%B2%A1%E6%89%A9%E5%B1%95%E6%98%AF%E4%B8%87%E4%B8%87%E4%B8%8D%E8%83%BD%E7%9A%84)

[Extensions  扩展](#1.Extensions%20%C2%A0%E6%89%A9%E5%B1%95)

[BApp Store(应用程序商店)](#2.BApp%20Store%28%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%95%86%E5%BA%97%29)

[3.APIS](#3.APIS)

[4.Options  选项](#4.Options%20%C2%A0%E9%80%89%E9%A1%B9)

[Project Options](#Project%20Options)（项目选项）

[connect（连接）](#connect%EF%BC%88%E8%BF%9E%E6%8E%A5%EF%BC%89)

[ 选项1、Platform Authentication（平台验证）](#%C2%A0Platform%20Authentication%EF%BC%88%E5%B9%B3%E5%8F%B0%E9%AA%8C%E8%AF%81%EF%BC%89)

[选项2、Upstream Proxy Servers（顶级代理服务器）](#Upstream%20Proxy%20Servers%EF%BC%88%E9%A1%B6%E7%BA%A7%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%89)

[选项3、SOCKS代理](#SOCKS%E4%BB%A3%E7%90%86)

[选项4、Timeout（超时）](#Timeout%EF%BC%88%E8%B6%85%E6%97%B6%EF%BC%89)

[选项5、Hostname Resolution（主机名解析，可添加）](#Hostname%20Resolution%EF%BC%88%E4%B8%BB%E6%9C%BA%E5%90%8D%E8%A7%A3%E6%9E%90%EF%BC%8C%E5%8F%AF%E6%B7%BB%E5%8A%A0%EF%BC%89)

[选项6、Out-of-Scope Requests（超出范围的请求）](#Out-of-Scope%20Requests%EF%BC%88%E8%B6%85%E5%87%BA%E8%8C%83%E5%9B%B4%E7%9A%84%E8%AF%B7%E6%B1%82%EF%BC%89)

[HTTP](#HTTP)

[选项1、Redirections（重定向）](#Redirections%EF%BC%88%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%89)

[选项2、Streaming Responses（流式响应） ](#Streaming%20Responses%EF%BC%88%E6%B5%81%E5%BC%8F%E5%93%8D%E5%BA%94%EF%BC%89%C2%A0)

[选项3、Status 100 Responses（状态100响应）](#Status%20100%20Responses%EF%BC%88%E7%8A%B6%E6%80%81100%E5%93%8D%E5%BA%94%EF%BC%89)

[SSL](#SSL)

[选项1、SSL Negotiation（SSL协商）](#SSL%20Negotiation%EF%BC%88SSL%E5%8D%8F%E5%95%86%EF%BC%89)

[选项2、Client SSL Certificates（客户端SSL证书）](#Client%20SSL%20Certificates%EF%BC%88%E5%AE%A2%E6%88%B7%E7%AB%AFSSL%E8%AF%81%E4%B9%A6%EF%BC%89)

[选项3、SSL Certificates（服务器SSL证书）](#SSL%20Certificates%EF%BC%88%E6%9C%8D%E5%8A%A1%E5%99%A8SSL%E8%AF%81%E4%B9%A6%EF%BC%89)

[选项4、Sessions（会话）](#Sessions%EF%BC%88%E4%BC%9A%E8%AF%9D%EF%BC%89)

[选项5、Session Handing Rules（会话处理规则）](#Session%20Handing%20Rules%EF%BC%88%E4%BC%9A%E8%AF%9D%E5%A4%84%E7%90%86%E8%A7%84%E5%88%99%EF%BC%89)

[选项6、Cookie Jar（饼干罐）](#Cookie%20Jar%EF%BC%88%E9%A5%BC%E5%B9%B2%E7%BD%90%EF%BC%89)

[选项7、Macros（宏）](#Macros%EF%BC%88%E5%AE%8F%EF%BC%89)

[Misc（杂项）](#Misc%EF%BC%88%E6%9D%82%E9%A1%B9%EF%BC%89)

[ 选项1、Scheduled Tasks（预定任务）](#Scheduled%20Tasks%EF%BC%88%E9%A2%84%E5%AE%9A%E4%BB%BB%E5%8A%A1%EF%BC%89)

[选项2、Collaborator Server（协作服务器）​](#Collaborator%20Server%EF%BC%88%E5%8D%8F%E4%BD%9C%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%89%E2%80%8B)

[选项3、Logging（日志记录）](#Logging%EF%BC%88%E6%97%A5%E5%BF%97%E8%AE%B0%E5%BD%95%EF%BC%89)

[User options（用户选项）](#User%20options%EF%BC%88%E7%94%A8%E6%88%B7%E9%80%89%E9%A1%B9%EF%BC%89)

[Connections 连接](#1.Connections%20%E8%BF%9E%E6%8E%A5)

[选项1：Platform Authentication（平台认证）](#%E9%80%89%E9%A1%B91%EF%BC%9APlatform%20Authentication%EF%BC%88%E5%B9%B3%E5%8F%B0%E8%AE%A4%E8%AF%81%EF%BC%89)

[选项2：Upstream Proxy Servers（顶级代理服务器）](#%E9%80%89%E9%A1%B92%EF%BC%9AUpstream%20Proxy%20Servers%EF%BC%88%E9%A1%B6%E7%BA%A7%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%89)

[选项3：Socks Proxy（SOCKS代理）](#%E9%80%89%E9%A1%B93%EF%BC%9ASocks%20Proxy%EF%BC%88SOCKS%E4%BB%A3%E7%90%86%EF%BC%89)

[SSL](#2.SSL)

[选项1：Java SSL Options（JAVA SSL选项）](#%E9%80%89%E9%A1%B91%EF%BC%9AJava%20SSL%20Options%EF%BC%88JAVA%20SSL%E9%80%89%E9%A1%B9%EF%BC%89)

[选项2：Client SSL Certificates（客户端SSL证书）](#%E9%80%89%E9%A1%B92%EF%BC%9AClient%20SSL%20Certificates%EF%BC%88%E5%AE%A2%E6%88%B7%E7%AB%AFSSL%E8%AF%81%E4%B9%A6%EF%BC%89)

[3.Display（表示）](#3.Display%EF%BC%88%E8%A1%A8%E7%A4%BA%EF%BC%89)

[选项1：User Interface（用户界面）](#%E9%80%89%E9%A1%B91%EF%BC%9AUser%20Interface%EF%BC%88%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2%EF%BC%89)

[选项2：Http Message Display（HTTP消息显示）](#%E9%80%89%E9%A1%B92%EF%BC%9AHttp%20Message%20Display%EF%BC%88HTTP%E6%B6%88%E6%81%AF%E6%98%BE%E7%A4%BA%EF%BC%89)

[选项3：Character Sets（字符集）](#%E9%80%89%E9%A1%B93%EF%BC%9ACharacter%20Sets%EF%BC%88%E5%AD%97%E7%AC%A6%E9%9B%86%EF%BC%89)

[选项4：HTML呈现](#%E9%80%89%E9%A1%B94%EF%BC%9AHTML%E5%91%88%E7%8E%B0)

[4.Misc  杂项](#4.Misc%20%C2%A0%E6%9D%82%E9%A1%B9)

[ 选项1：Hotkeys（热键）](#%E9%80%89%E9%A1%B91%EF%BC%9AHotkeys%EF%BC%88%E7%83%AD%E9%94%AE%EF%BC%89)

[选项2：Project automatic backup（项目自动备份）](#%E9%80%89%E9%A1%B92%EF%BC%9AProject%20automatic%20backup%EF%BC%88%E9%A1%B9%E7%9B%AE%E8%87%AA%E5%8A%A8%E5%A4%87%E4%BB%BD%EF%BC%89)

[选项3：Temporary Files Location（临时文件位置）​](#%E9%80%89%E9%A1%B93%EF%BC%9ATemporary%20Files%20Location%EF%BC%88%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6%E4%BD%8D%E7%BD%AE%EF%BC%89%E2%80%8B)

[选项4、REST API（API）](#REST%20API%EF%BC%88API%EF%BC%89)

[选项5、Proxy Interception（代理拦截）](#Proxy%20Interception%EF%BC%88%E4%BB%A3%E7%90%86%E6%8B%A6%E6%88%AA%EF%BC%89)

[选项6、Agent history（代理历史记录）选项7、Performance Feedback（表现反馈）](#Agent%20history%EF%BC%88%E4%BB%A3%E7%90%86%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95%EF%BC%89Performance%20Feedback%EF%BC%88%E8%A1%A8%E7%8E%B0%E5%8F%8D%E9%A6%88%EF%BC%89)

---


 （下的中文版，看着中文打英文，练成我这样，攻估计看见英文就和看见中文一样了）

## Filter showing all items（过滤器）

### 筛选功能：

#### 过滤器在哪呢？

> 
①在Proxy（代理）中的HTTP history 和WebSocket中下面


②在目标的map site（网站地图）下面


③在仪表盘上（对任务、事件事志、问题活动的过滤）



#### 你使用过滤器了嘛？

> 
  从URL中筛选带参数的URL,（进行代码层面的攻击,如SQL注入等）




可以通过关键字、扩展名来进行搜索



点击左边的设置按钮，可以恢复默认值，加载或者保存选项<img alt="" height="523" src="https://img-blog.csdnimg.cn/cb9243875c984da684bc124d1b36b145.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="934"/>

相关工具（简单了解一下）



 如何使用筛选器将染色过的URL筛选出来？
①首先你需要对指定URL进行染色


②再点击筛选器，然后在右下角勾选仅显示彩色项目，再点击空白区域就可以筛选出来了



 

## Target（目标）

被代理的浏览器在访问web服务器后HTTP请求包保存在：

①Proxy（代理） HTTP History（HTTP历史记录）

②Target（目标）site map（网站地图）

#### URL不同颜色，它的区别是？

> 
 深色：已经发送过请求的URL地址
浅色：所请求的地址网页里所存在的其它URL地址（未访问过）




#### 如何查看一个/多个指定的URL地址？

> 
 点击选中要添加的URL地址-------&gt;右键Add to scope（添加到范围）
（弹出的提示我点的没有）

 <img alt="" height="238" src="https://img-blog.csdnimg.cn/114cfb7ab714496484affce818d0f161.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_11,color_FFFFFF,t_70,g_se,x_16" width="463"/>

 然后在scope（范围中就可以看见刚刚所添加的地址了）<img alt="" height="668" src="https://img-blog.csdnimg.cn/4c6639875e054f5db006e3a0463eae61.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>
 点击二级栏目下面的Filter showing all items（过滤器）------&gt;勾选show only in-scope items（仅在范围内显示项目）------&gt;设置完成后点击空白地方，就能显示出筛选结果


 <img alt="" height="670" src="https://img-blog.csdnimg.cn/4468b7d473224220a15ac1a1aad3ccb3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


### scope（范围）

#### 将指定URL添加/删除scope（范围）的方法？

> 
选项1：添加方法
①直接在Target（目标）的site map或代理的URL中添加到范围

②直接手动添加URL地址 




选项2：Exclude from scope（从范围中删除）
即不爬取指定页面的内容（这个不能直接点击网站URL后选择从范围中删除，因为都已经爬出来了）

所以就直接添加即可




 

<br/>  

## Scanner（扫描）

(自我的拙见：burpsuite2.x版本的好像，就把scanner和spider合在一起了)

#### 在哪开始scanner（扫描）/spider（爬取）？

> 
 点击scanner（扫描）后可以看见爬行和审计
在仪表盘（dash board）上左上角框框就是添加scanner（扫描）



#### 怎么开始相关scanner（扫描）或者spider（爬取）？

> 
  可以选择扫描类型，可以指定URL



如果有的需要登录的话，就可以自己先提前注册，然后填在这里 

这个视情况而定把


设定好后，它就会在任务栏开始扫描了 



#### 在哪查看扫描和爬取的相关信息？

> 
然后点击每个任务的最右上角的详细表示（即斜向上的箭头）
就可以看见更多详细的扫描情况
详细、审核项目、问题活动、事件日志





而且相关内容也会被爬取到Target（目标）下的site map（网站地图）里 



 

 

## Proxy（代理）

### intercept（截断）

### 对于截取信息的分析和处理

> 
<h4>选项1：Raw</h4>
文本形式的消息:，文本窗口底部有搜索（快速地定位出想要的字符串）和加亮功能。

点击+号，可以选择区分大小写，正则表现，以及在文本更改是自动滚动到匹配位置



<h4>选项2：params（参数）</h4>
会自动把数据包中的参数分析成名称：值一一对应，
方便查看和修改相关参数<br/><img alt="" height="671" src="https://img-blog.csdnimg.cn/201e43c1748245af93b5bcfa8e2ab971.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/><br/>  

<h4>选项3：headers</h4>
名称：值一一对应显示 HTTP 的消息头（以原始形式显示消息体）


<h4>选项4：hex</h4>
能够对原始二进制数据进行编辑（不会发生损毁）
如果在Raw（文本编辑）修改，（MIME 编码的浏览器请求的部分）等一些传输类型的二进制数据有损毁的可能。应在Hex中修改这些类型的消息的十六进制值，达到修改的目的。
 <img alt="" height="668" src="https://img-blog.csdnimg.cn/b8593a685b0b468298fadef4e6751c9e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>


#### 选项2：params（参数）

#### 选项4：hex

### 对于数据包的执行处理

> 
<h3> 选项1：Forward（放包）</h3>
抓包修改后，再将其发送到服务器或浏览器
<h4><br/>选项2：Drop（废包）</h4>
点击drop就会不拦截这个当先这个信息，即放弃
<h4><br/>选项3：Interceptionis on/off（拦截  请求/关闭）</h4>
如果显示Interceptionis On（拦截请求），根据配置的拦截规则进行相应的拦截和转发
如果显示Interception is off（拦截关闭），拦截之后自动转发
<h4><br/>选项4：Action（行动）</h4>
这个就可以将拦截的数据发送到其他模块
 <img alt="" height="238" src="https://img-blog.csdnimg.cn/5795c26973284c8baf9ee4d3a1621ddc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>
<h4>选项5：评论和染色</h4>
在最右边，把项目评论和染色后，方便以后筛选出来


#### <br/>选项3：Interceptionis on/off（拦截  请求/关闭）

#### 选项5：评论和染色

 

### 数据包的更多执行模块使用：

> 
<h4>英语基础： </h4>
发送到相关模块、工具：<br/> Send to Intruder（发送到入侵者）、Send to Repeater（发送到中继器）、Send to Sequencer（发送到序列发生器）、Send to Comparer（发送到比较器）、Send to Decoder（发送到解码器）、Request in browser（通过浏览器的请求）、Engagement tools（参与工具）

<h4>相关处理操作：</h4>
<h4>选项1.Change request method（变更请求方法）：</h4>
可以自动地把POST 和 GET请求方法相互切换。（使用变更请求方法来发送恶意请求，测试程序的极限参数）
<h4>选项2.Change body encoding（身体编码改变）：</h4>
在程序、X-WWW格式的 URL 编码和多重表单、数据之间切换消息体的编码方式
<h4>选项3.Copy URL （复制网址）</h4>
<h4>选项4.Cope as curl command（复制curl命令）</h4>
<h4>选项5.Cope to file（复制到文件）：</h4>
把消息的内容复制到选择你选择的文件（避免复制粘贴出错）
<h4>选项6.Pase form file（从文件粘贴）：</h4>
把你所选择的文件里的内容粘贴到消息（避免覆盖或插入错用）
<h4>选项7.Save item（保存项目）：</h4>
把选中的请求和响应以XML的格式保存到指定的文件中（数据可以是响应的长度、HTTP 状态码、MIME等）

<h4>拦截：</h4>
<h4>选项1.Don't intercept requests（请求不要拦截）：</h4>
顾名思义，不拦截，通过将其添加到拦截规则中来阻止拦截和当前的消息有着相同的特征(主机，类型，编码)的消息。
<h4>选项2.Do intercept（拦截执行）：</h4>
顾名思义，对当前请求和响应强制拦截操作（有效的请求）
<h4>选项3.Convert seiection（转换）：</h4>
有很多方案对选择的文本进行编码和解码等操作。
<h4>选项4.URL-encode as you type（URL编码输入）：</h4>
打开这项功能后，如&amp;=等这样的符号会被URL编码

<h3>基操：</h3>
Cut（剪切）、Copy（复制）、Paste（粘贴）、Message edit help（消息编辑）、Proxy interception help（代理拦截）


#### 相关处理操作：

#### 选项2.Change body encoding（身体编码改变）：

#### 选项4.Cope as curl command（复制curl命令）

#### 选项6.Pase form file（从文件粘贴）：

#### 拦截：

#### 选项2.Do intercept（拦截执行）：

#### 选项4.URL-encode as you type（URL编码输入）：

 

### HTTP History

#### 如何处理相关HTTP History信息？

> 
显示请求产生的所以信息：
目标服务器和端口、HTTP 方法、URL、是否包含参数、是否被修改、HTTP 的响应状态码、响应字节大小、响应的 MIME类型、请求资源的文件类型、HTML 页面的标题、是否使用 SSL、远程 IP 地址、服务器设置的 cookies、请求的时间




在历史记录里面双击某个URL可详情查看
Previous/next（前一个/后一个）可切换请求
Action可将请求发到其他模块或执行其他操作



点击每个URL的编号，会出现一个下拉菜单，可以染色来标记，方便以后筛选找到


选中相关网址后右键，可执行action的相关操作
<img alt="" height="497" src="https://img-blog.csdnimg.cn/9c83897ab4604932a29bc27994d06f87.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="703"/><br/>  


### WebSockets history（WebSockets历史记录）

#### 简单介绍下WebSockets history 喽

> 
顾名思义，记录了WebSockets数据包
是HTML5中最强大的通信功能，定义了一个全双工的通信信道，只需Web上的一个 Socket即可进行通信（减少无用网络流量来降低延迟）



### Options（选项）

#### 英语基础：

> 
Proxy Listeners（设置代理监听）、Intercept Client Requests（拦截客户端请求）、Intercept Server Responses（拦截服务器响应）、Intercept WebSockets Messages（拦截WebSockets消息）、Response Modification（响应修改）、Match and replace（匹配和替换）、SSL Pass Through（SSL通过）、Miscellaneous（各种各样的）


### OPtions大全介绍

> 
<h4>选项1、Proxy Listeners（代理监听器）</h4>


默认代理侦听器是侦听  连接本地HTTP代理服务器的浏览器的数据。
可以监视和拦截所有的请求和响应（Bp核心）。
默认情况下，Bp默认监听12.0.0.1地址，端口8080。使用默认监听器，需要配置本地浏览器代理服务器为127.0.0.1:8080。能测试基于浏览器的所有Web程序。



add（添加）：添加新的代理
binding（捆绑）：bind to port（绑定端口号 ）、bind to address （绑定IP地址）


 Request processing（请求处理）
控制是否重定向通过此侦听器接收到的请求

Redirect to host（重定向到目标主机）：
Bp会请求转发到指定的主机（不需要再修改浏览器代理）。
经过代理器匹配/替换等规则后重定向请求，与浏览器直接发送可能有区别
<br/> Redirect to port（重定向到目标端口）：Bp将请求转发到指定的端口（不需要再改浏览器代理）<br/>  
Force use of SSL（强制使用SSL）：
Bp在所有向外的连接将使用HTTPS（无论传入的是HTTP/HTTPS）。与SSL相关的响应修改选项结合，开展sslstrip般的攻击使用Bp，强制执行HTTPS的应用程序可以降级为HTTP的受害用户的流量在不知不觉中通过BurpProxy代理。
   



Certificate（证书）
控制提交给SSL客户端的SSL服务器证书
Generate CA-signed per-host certificate（生成每次主机证书的CA签名）：
默认选项，Bp安装后，自动产生自签名的证书颁发机构（CA）证书，Bp运行时将在计算机上使用。当浏览器发出SSL连接到指定的主机，该主机使用CA证书签名的SSL证书。（要将Bp的CA证书安装到浏览器中，避免安全警告）
<br/> Generate a CA-signed certificate with a specific hostname（使用特定主机名生成CA签名证书）：对于指定的主机名，Bp产生一个主机证书与每一个SSL连接使用。
（当客户端没有发送连接请求时，Bp不能确定SSL所需的主机名。可以安装Bp的CA证书作为信任根）
<br/> Use a custom certificate（使用自定义证书）：
当应用程序使用它需要特定的服务器证书的客户端，就需要使用一个特定的证书提交给浏览器。




<h4>选项2：Intercept Client Requests（拦截客户端请求）</h4>
配置拦截的匹配规则。 当勾选Intercept request based on the following rules（基于以下规则拦截请求）后，Bp基于下列列表中的规则进行拦截或转发，规则按顺序处理，并且使用布尔运算符And和Or组合
（注：若拦截客户端复选框未被勾选，那么Intercept is on也截取不到数据包）
可以勾选/取消勾选Enabled（启用）列中的复选框进行规则的开启/关闭
写入的规则：域名， IP地址，协议， HTTP方法， URL，文件扩展名，参数，cookie ，头/主体内容，状态代码，MIME类型， 页面标题等等。




<h4>选项3：Intercept Server Responses（拦截服务器响应）</h4>
配置拦截的匹配规则，基于服务端拦截，勾选Intercept request based on the following rules时，bp会基于匹配规则拦截相应响应包



<h4>选项4：Intercept WebSockets Messages（拦截WebSockets消息）</h4>
分为拦截客户端、拦截服务器





<h4>选项5：Response Modification（响应修改操作）</h4>
勾选的相关自动更改操作



<h4>选项6：Match and replace（匹配和替换）</h4>
用于自动替换请求和响应通过代理的部分（勾选的匹配和替换规则依次执行）

每个规则可规定一个文字字符串/正则表达式来匹配，并来替换它。
对于邮件头，匹配条件满足的话，整个头和替换字符串匹配留空，然后头被删除。（可使用标准的正则表达式语法匹配邮件正文的多行区域。）
默认为禁用：空的匹配表达式，替换字符串被添加为一个新的头，协助常见任务的缺省规则




<h4>选项7：SSL Pass Through（SSL通过）</h4>




<h4>选项8：Miscellaneous</h4>
这就是一个各种各样的默认设置了，可以进行修改




#### 选项2：Intercept Client Requests（拦截客户端请求）

#### 选项4：Intercept WebSockets Messages（拦截WebSockets消息）

#### 选项6：Match and replace（匹配和替换）

#### 选项8：Miscellaneous

 

## Intruder（测试器）

### Target（目标）

> 
Host（主机）：目标服务器的IP地址/主机名<br/> Port（端口）：http/https服务的端口号<br/> Use HTTPS（使用HTTPS）：勾选是否使用SSL
在代理或目标模块，选中URL，右键上下文菜单中点击Send to Intruder（发送到入侵者）将会有一个新的选项卡（就像这上面的1,2，……），然后主机和端口会自动填上。



### Positions（位置）

> 

<h4>选项1、Payload Positions（有效载荷位置）</h4>
配置攻击的请求模板、有效负载标记（可以手动添加，也可自动添加）和攻击类型

每对 ‘ § ’标记的内容是一个Payload位置。有效载荷位置被分配了Payload时，标记和任何包含的文本都将被Payload替换，当有效载荷位置没有指定的Payload时，标记§将被移除。<br/> (每对有效负载标记以及它们之间的文本会被凸显）

Add § （添加§） 
光标在字符间位置：插入一个有效载荷标记
选择的文本：则插入一对标记，并将选的内容括起来

Clear § （清除§）
清除所有§ ；清除选定部分的§

Auto §（自动§）   
在整个文本中自动添加；在选中部分自动添加
顾名思义，自动的放置有效载荷标记，快速标记适合模糊化的位置。（会将有效负载自动放置到各类型的请求参数的值中，如URL查询字符串参数、Body parameters、Cookies、参数属性，XML数据、元素属性、JSON参数等）
一般可能会有针对性的攻击，那么久需要手动定位添加了。
Refresh（刷新）：刷新模板编辑器中的语法着色
Clear（清屏）：删除整个模板的内容



<h4>选项2、Attack type（攻击类型）：</h4>
Bp Intruder模块支持各种攻击类型，决定分配到有效载荷位置的方式
攻击类型有：
Sniper（狙击手）：以每个位置为目标，依次将Payload放到该位置，每个标记依次测试。（一组Payload）
Battering ram（破城缒）：同时将Payload（相同的）放入所有被定义的位置进行测试，即多管齐下的意思。（一组Payload）
Pitchfork（音叉）    每个定义的位置都能用不同的Payload继续测试（最多20个）即一对一，且可重复，视情况而定。（多个Payload集）
Clusterbomb（集束炸弹）    每个定义的位置有一个不同的有效负载集（最多20），即在多个位置遍历不同的payload集继续攻击。（多个Payload集）



#### 选项2、Attack type（攻击类型）：

### Payloads（有效载荷）

> 

<h4> 选项1、Payload Sets（设置）</h4>
能够进行一个或多个负载集的配置，但是Payload集的数量取决于攻击所需要选择的Attack type（攻击类型），即在Positions（位置）选项卡中选择的Attack type（攻击类型）
一般常见的，如模糊参数、强制猜测用户密码等只需要一个有效负载集。
Payload set : 配置的数量<br/> Payload type ： 类型


 Simple list（简单字典）、Runtime file（运行文件）、Custom iterator（自定义迭代器）、Character substitution（字符替换）、Recursive grep（递归查找）、illegal Unicode（非法字典）、Character blocks（字符块）、Numbers（数组组合）、Dates（日期组合）、Brute forcer（暴力破解）、Null payloads（空Payload）、Username generator（用户名生成）、Copy other payload（复制其他Payload）


<h4>选项2、Payload Options（有效载荷选项）</h4>
有效载荷选择的类型的不同的话，配置有效载荷的选项也会有差异（也就是大同小异把）
这个看着来（太多了不能一一讲解）





<h4>选项3、Payload Processing（有效载荷处理）</h4>
可以定义在使用有效载荷之前，对每个有效载荷执行处理的规则（按顺序执行的，可打开或关闭），即将有效载荷加工后再使用它。


有效负载相关处理规则：
Add prefix（添加一个文本前缀）



Add suffix（添加一个文本后缀）


Match/replace（搜索/替换）


Substring（部分文字列），即提取
 <img alt="" height="204" src="https://img-blog.csdnimg.cn/d7cb3de5ad604ffc865bb2f6fee5ba79.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_12,color_FFFFFF,t_70,g_se,x_16" width="492"/>

Reverse substring（翻转字符串）从指定有效负载的末尾向后计数结束偏移量，并从结束偏移量向后计数长度


Modify case（转换大小写）


Encode（编码）对负载进行编码：url、html、base64、ascii hex、各种平台构建的字符串


Decode（解码）各种方法解码负载：url、html、base64、ASCII hex


 Hash（哈希函数）对负载进行散列

Add raw payload（添加原始的有效负载），即以原始形式提交的负载



Skip if matches regex（正则匹配），即满足正则匹配就跳过它，好比要收集最长不超过5字符数据，如果超过5字符了就不要了


Invoke burp extension（调用Bp扩展）顾名思义，调用bp扩展来处理有效负载（扩展注册了入侵者有效负载处理器，或者选择处理器）





<h4>选项4、Payload Encoding（有效载荷编码）</h4>

 可以配置将有效负载中指定的字符进行url编码并应用（安全传输）
（一般编码设置用于最终URL，非有效负载处理规则）


#### 选项2、Payload Options（有效载荷选项）

#### 选项4、Payload Encoding（有效载荷编码）

### Options（选项）

> 

<h4>选项1、Request Headers（请求标头）</h4>
控制Intruder是否在攻击期间更新配置的请求标头
Update Content-Length header （更新Content-Length标头）：
使Intruder在每个请求中添加/更新内容长度头，并使用该特定请求的http正文长度的正确值。（主要就是面向于请求头的攻击）

Set Sconnection: close（设置连接为：关闭） ：
使Intruder添加/更新值为“close”的连接头。（主要用于服务器未返回有效头时，以达到更快的展开攻势）。




<h4>选项2、Request Engine（请求引擎）</h4>
用于攻击执行期间对引擎的设置（注意对被攻击者产生的影响，以及自身的带宽和处理能力合理配置）

Number of threads（线程数）：即攻击时候能够同时并发请求数
Number of retries on network failure（网络错误的重试次数）：当连接错误或发生其他网络相关问题的时候，Bp会放弃当前的错误，然后重新按之前配置的次数重新请求
Pause before retry（重试前暂停）：顾名思义，停指定时间再请求（战略性撤退）
Throttle between requests（请求之前限制）：即重量，在每个请求之前等待指定的时延（ms）
Start time（开始时间）：顾名思义，设置攻击开始的时间（偷袭是吧，来呀，展翅）





<h4>选项3、Attack Results（攻击结果）</h4>
即是在攻击的结果中进行捕获信息
Store requests / responses（保留请求/响应）
简而言之，就是将单个的请求记录保存起来，每一个都保存，就都在一起能进行更多的分析了（但是会占用内存）
Make unmodified baseline request（生成未修改的基本请求）
配置的攻击请求+Bp发出的模板请求（结果中能够比较攻击响应），所有有效负载位置将被设为其基本值。
Use denial-of-service mode（使用拒绝服务模式）：
顾名思义，攻击时候将正常发出请求，无结果即不会等待从服务器处理后的任何响应（就是重复发送，发出就关闭TCP连接，保持打开套接字等待服务器响应，为了避免锁定本地资源）
Store full payloads（保存所有有效载荷）：
Bp保存所有结果的全部有效载荷值（会占用内存），保存后可以修改负载或模板再进行发送




<h4>选项4、Grep - Match</h4>
为结果设置一个标志，包括指定的正则表达式，并能将匹配的结果组合在一起。<br/> 这个分析能力不是一点的强大，可以很大程度上的帮助我们去分析大量结果集，便于我们找到能够利用的参数或其他注入点等。

匹配外的其他选项：
**Match type（匹配类型）**：表达式是简单字符串/正则表达式
**Case sensitive match（区分大小写匹配）：**表达式的检查是否区分大小写字母
**exclude http headers（排除HTTP标头）**：是否从检查中排除HTTP响应头





<h4>选项5、Grep - Extract（提取物）</h4>
从响应中提取有用信息并将其保存在攻击结果列表中（会添加一个新的results列，然后将提取的信息放在里面，单击标题可以对标题进行排序）
较多的用于数据挖掘，然后找到有用的信息
可以多次添加同一匹配项，然后查找到多个匹配项，就可以挖掘到更多的有用信息
能够自定义从哪后面开始，并以什么分隔符结束




<h4>选项6、Grep - Payloads（Grep有效载荷）</h4>
可以在结果项上设置标记，反应传输的有效载荷。（检测跨站点脚本和其他响应注入漏洞）
Bp将添加一个新的results列，包含一个复选框，是否在每个响应中找到了当前负载值。（如果有多个有效载荷，则添加多个对应的列）

有效载荷的设置标记处理匹配规则：
Search response to payload strings（搜索有效载荷字符串的响应）、Case sensitive match（区分大小写字母）、exclude http headers（排除HTTP标头）
Match against pre-URL-encoded payloads（在URL编码之前匹配有效载荷）：将入侵者配置为url编码请求中的有效载荷是正常的。然后由应用程序解码并以其原始形式回显，此项将以预编码形式对有效载荷进行burp check响应




<h4>选项7、Redirections（重定向）</h4>
控制执行攻击时如何处理重定向（一般为了达到攻击目的，需要遵循重定向）
Follow redirections （跟随重定向）：
Never （不遵循）<br/> On-site only（只在同一个网站，即只重定向到同一个网站） <br/> In-scope only（仅限范围，即重定向到规定的URL范围内）<br/> Always（总是，这个注意使用，可能会误伤别人其他无辜的）



#### 选项2、Request Engine（请求引擎）

#### 选项4、Grep - Match

#### 选项6、Grep - Payloads（Grep有效载荷）

 

## Repeater（重发器）

### Repeater介绍一下吧

> 
 在Proxy.intercept(代理截断)、HTTP.history(HTTP历史记录)、site map(网站地图)中的URL发送到Repeater(重发器）
对于抓取的数据包发送到Repeater（重发器）模块（发送成功Repeater会亮）
右键点击数据包，然后点击send to repeater
Ctrl+r，使用快捷键发送到Repeater（重发器）模块
点击右边的Action（行动），然后再点击send to repeater


<h4>英语基础：</h4>
Repeater（重发器）
send（把数据包发送出去）、cancel（取消发送)
Request(请求包)、Response（响应包）
Raw（数据包文本）、Render（数据包回显的界面，就是网页正常的样子）



左右箭头：(顾图思义，前进或后退，就是修改后数据包发送了，这个箭头可以返回上一个数据包，也可以再回到下一个数据包)
下箭头，查看修改记录 



 

## Sequencer模块(定序器)

根据一个样本用于分析数据项（反弹CSRF、密码重置tokens）随机性的工具，就是分析不可预测的数据，像测试应用程序的session（会话）tokens或其他重要数据项。

Sequencer（定序器）模块：

Live capture 信息截取

Manual load 手动加载

Analysis options 选项分析

### Live capture 信息截取

> 
<h4> 选项1：Select Live Capture Request（选择实时捕获请求）</h4>
实时捕捉太清楚不过了





<h4>选项2：Token Location Within Response  （响应中的令牌位置）</h4>
这个就是一个指定位置了



<h4>选项3：Live Capture Options （实时捕获选项）</h4>
 这个就是执行捕获和收集令牌时，生成HTTP请求<img alt="" height="241" src="https://img-blog.csdnimg.cn/1f4b1d4609dd49568e61ac5fd01bef8c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_18,color_FFFFFF,t_70,g_se,x_16" width="751"/>


#### 选项2：Token Location Within Response  （响应中的令牌位置）

### Manual load 手动加载

> 
<h4>选项1：Manual Load（手动阅读）</h4>
标记的样本（或者复制粘贴）---------&gt;统计分析




### Analysis options 选项分析

> 
<h4> 选项1：Token Handling  (令牌处理)</h4>
**对正在分析的令牌进行处理的规则的配置（填充、解码）**



<h4>选项2：Token Analysis  （令牌分析)</h4>




#### 选项2：Token Analysis  （令牌分析)

 

 

## Decoder(编码器)

> 
 既可以编码也可以解码的工具，并且还有智能解码的功能（启发式技术）

右键菜单中点击编码下拉菜单选择编码方法，即可进行相应编码，解码与此类似，或者可以直接点击Smart decoding(智能解码)

还有一个特别方便的功能，那就是在Decoder（编码器）的界面的时候，能够进行叠加多次编码或者解码



 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/c56a5337fec7df006d54d9dd06842f4a.gif"/>

 

## Comparer（对比器）

### Comparer基操：

> 
 可以用来详细的比较不同的HTTP请求的各个不同的地方（能够详细的通过颜色反应出来）
可以针对两个不同或者多个不同的HTTP请求进行详细的比较，然后发现不同点

可以选择截取的URL，或在site map（网站地图中的URL）然后点击右键，再点击发送到compare进行对比



发送到comparer（对比器）之后
可以再点击加载本地的数据包进行对比，也可以再去找到一个或多个URL数据包发送到comparer再进行对比（比较一个字/字节）

可以在第一个项目里面选择一个，在第二个选项当里，再选择不同的选项
比较后，就会出现比较的结果


 <img alt="" height="646" src="https://img-blog.csdnimg.cn/c8a7ebf41b6f46bb8414b7902d79f259.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>



标记为亮色的都是不同的选项，通过这种方式可以快速比较不同用户请求相同页面的差别


 

## Extender(扩展器)

### 扩展是万能的，没扩展是万万不能的

> 
支持第三方拓展插件的功能，使用者可以编写自己的插件或者从插件商店中安装拓展插件（能够根更好的自定义处理操作）

Extender（扩展器）组成模块：
Extensions(扩展)、BApp Store(应用程序商店)、APIS（Bp扩展API）、Options(选项)


### Extensions  扩展

> 
可以从本地选择文件进行加载


日志信息的输出方式：
输出到系统控制台、保存到指定的文件、默认选择Bp界面输出


### BApp Store(应用程序商店)

> 
 在BApp Store中有各种插件的应用列表，当点击某个插件后，右侧会显示次插件的相关一些介绍等信息。 可以点击左下方的install(安装)按钮，进行安装



安装按钮置为灰色，installing（正在安装），右下角也显示安装中
安装成功的话
instal------&gt;Reinstall,并且能对插件进行评分，Submit rating（评分）
在Extender 的Extension的页面中，会显示已安装的插件列表（方便后期插件管理）



我们也可以下载插件，然后进行手工安装（自我感觉多此一举，但是这样必定是有它的用处的，有待发现，或许就是换个位置安装吧，醉了，挺人性化的）



 

### 3.APIS

> 
使用扩展的API，可以创建自己的扩展来自定义Bp的功能



### 4.Options  选项

> 
 对于扩展的一个环境配置



 

## Project Options

该模块主要用来对Project的做设置的，它拥有五个小的模块组成，下面将一一介绍这些模块

### connect（连接）

> 
<h4> 选项1、**Platform Authentication（**平台验证**）**</h4>
<h4>选项2、Upstream Proxy Servers（顶级代理服务器）</h4>
<h4>选项3、SOCKS代理</h4>
<h4>选项4、Timeout（超时）</h4>


<h4>选项5、Hostname Resolution（主机名解析，可添加）</h4>
<h4>选项6、Out-of-Scope Requests（超出范围的请求）</h4>
防止Bp发出超出范围外的所有请求



#### 选项2、Upstream Proxy Servers（顶级代理服务器）

#### 选项4、Timeout（超时）

#### 选项6、Out-of-Scope Requests（超出范围的请求）

### HTTP

> 
<h4>选项1、Redirections（重定向）</h4>
<h4>选项2、Streaming Responses（流式响应）<br/>  </h4>

<h4>选项3、Status 100 Responses（状态100响应）</h4>
处理状态为100的HTTP请求




#### 选项2、Streaming Responses（流式响应）<br/>  

### SSL

> 
<h4>选项1、SSL Negotiation（SSL协商）</h4>
<h4>选项2、Client SSL Certificates（客户端SSL证书）</h4>
<h4>选项3、SSL Certificates（服务器SSL证书）</h4>





<h4>选项4、Sessions（会话）</h4>
<h4>**选项5、Session Handing Rules（**会话处理规则**）**</h4>
可以自定义规则
<h4>选项6、Cookie Jar（饼干罐）</h4>


<h4>选项7、Macros（宏）</h4>
是一个或多个请求的序列，可以在会话处理规则中使用宏来执行任务（登录、获取CSRF令牌）



#### 选项2、Client SSL Certificates（客户端SSL证书）

#### 选项4、Sessions（会话）

#### 选项6、Cookie Jar（饼干罐）

 

### Misc（杂项）

> 
<h4> 选项1、Scheduled Tasks（预定任务）</h4>
可自行设置什么时候开启什么任务
<h4>选项2、Collaborator Server（协作服务器）<br/><img alt="" height="716" src="https://img-blog.csdnimg.cn/94b50e14e4994fa6af52244ce92bce84.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/></h4>

<h4>选项3、Logging（日志记录）</h4>
选中选项就会在进行该项活动的时候记录下来



#### 选项2、Collaborator Server（协作服务器）<br/><img alt="" height="716" src="https://img-blog.csdnimg.cn/94b50e14e4994fa6af52244ce92bce84.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>

 

 

## User options（用户选项）

用来配置一些常用的选项。

User options（用户选项）的组成模块：

Connections（连接）、SSL、Display（表示）、Misc（杂项）

### Connections 连接

> 
<h4>选项1：Platform Authentication（平台认证）</h4>
<h4>选项2：Upstream Proxy Servers（顶级代理服务器）</h4>
<h4>选项3：Socks Proxy（SOCKS代理）</h4>




#### 选项2：Upstream Proxy Servers（顶级代理服务器）

 

### SSL

> 
<h4>选项1：Java SSL Options（JAVA SSL选项）</h4>
<h4>选项2：Client SSL Certificates（客户端SSL证书）</h4>



#### 选项2：Client SSL Certificates（客户端SSL证书）

### 3.Display（表示）

> 
<h4>选项1：User Interface（用户界面）</h4>
<h4>选项2：Http Message Display（HTTP消息显示）</h4>
<h4>选项3：Character Sets（字符集）</h4>
<h4>选项4：HTML呈现</h4>




#### 选项2：Http Message Display（HTTP消息显示）

#### 选项4：HTML呈现

 

### 4.Misc  杂项

> 
<h4> 选项1：Hotkeys（热键）</h4>
<h4>选项2：Project automatic backup（项目自动备份）</h4>
<h4>选项3：Temporary Files Location（临时文件位置）<br/><img alt="" height="802" src="https://img-blog.csdnimg.cn/aa8ccbf0d75a411ab47f65b374317fec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/></h4>

<h4>选项4、REST API（API）</h4>
<h4>选项5、Proxy Interception（代理拦截）</h4>


<h4>选项6、Agent history（代理历史记录）<br/> 选项7、Performance Feedback（表现反馈）</h4>



#### 选项2：Project automatic backup（项目自动备份）

#### 选项4、REST API（API）

#### 选项6、Agent history（代理历史记录）<br/> 选项7、Performance Feedback（表现反馈）

<img alt="" src="https://img-blog.csdnimg.cn/613878b325714441aba8e330550b25aa.png"/> 
