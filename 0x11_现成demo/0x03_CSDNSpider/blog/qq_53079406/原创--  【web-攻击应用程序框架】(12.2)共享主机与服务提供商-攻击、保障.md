# 原创
：  【web-攻击应用程序框架】(12.2)共享主机与服务提供商：攻击、保障

# 【web-攻击应用程序框架】(12.2)共享主机与服务提供商：攻击、保障

**目录**

[共享主机与应用程序服务提供商](#%E5%85%B1%E4%BA%AB%E4%B8%BB%E6%9C%BA%E4%B8%8E%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E6%9C%8D%E5%8A%A1%E6%8F%90%E4%BE%9B%E5%95%86)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、虚拟主机](#1.2%E3%80%81%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BA)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.3、共享的应用程序服务](#1.3%E3%80%81%E5%85%B1%E4%BA%AB%E7%9A%84%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E6%9C%8D%E5%8A%A1)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.4、攻击共享环境](#1.4%E3%80%81%E6%94%BB%E5%87%BB%E5%85%B1%E4%BA%AB%E7%8E%AF%E5%A2%83)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[针对访问机制的攻击](#%E9%92%88%E5%AF%B9%E8%AE%BF%E9%97%AE%E6%9C%BA%E5%88%B6%E7%9A%84%E6%94%BB%E5%87%BB)

[应用程序间的攻击](#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%97%B4%E7%9A%84%E6%94%BB%E5%87%BB)

[ASP应用程序组件间的攻击](#ASP%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%BB%84%E4%BB%B6%E9%97%B4%E7%9A%84%E6%94%BB%E5%87%BB)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[攻击云](#%E6%94%BB%E5%87%BB%E4%BA%91)

[1.5、保障共享环境的安全](#1.5%E3%80%81%E4%BF%9D%E9%9A%9C%E5%85%B1%E4%BA%AB%E7%8E%AF%E5%A2%83%E7%9A%84%E5%AE%89%E5%85%A8)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[保障客户访问的安全](#%E4%BF%9D%E9%9A%9C%E5%AE%A2%E6%88%B7%E8%AE%BF%E9%97%AE%E7%9A%84%E5%AE%89%E5%85%A8)

[隔离客户功能](#%E9%9A%94%E7%A6%BB%E5%AE%A2%E6%88%B7%E5%8A%9F%E8%83%BD)

[隔离共享应用程序中的组件](#%E9%9A%94%E7%A6%BB%E5%85%B1%E4%BA%AB%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E4%B8%AD%E7%9A%84%E7%BB%84%E4%BB%B6)

---


## 共享主机与应用程序服务提供商

> 
<h3>1.1、简介：</h3>
1、许多组织通过外部提供商向公众提供他们的Web应用程序，这些服务包括组织通过其访问Web与数据库服务器的简单主机服务，以及代表组织主动维护应用程序的成熟应用程序服务提供商(ASP)，缺乏能力与资源部署自己的应用程序的小型企业常常采用这种服务，但一些知名公司有时也使用这些服务来部署特殊的应用程序

2、大多数Web与应用程序主机服务提供商拥有众多客户，且常常使用相同的基础架构或者紧密相连的基础架构支持许多客户的应用程序。
选择使用其中一种服务的组织必须考虑怎相关威胁：
A、服务提供商的一名恶意客户可能试图破坏该组织的应用程序及其数据
B、一名不知情的客户可能部署一个易受攻击的应用程序，使得恶意客户能够攻破共享的基<br/> 础架构，从而攻击组织的应用程序及其数据。
……

3、在共享系统中运行的Web站点是企图丑化尽可能多的Web站点的＂脚本小子” 的主要攻击目标， 因为只要攻破一台共享主机，就能在短期内向数百台明显自治的Web站点实施攻击


> 
<h3>1.2、虚拟主机</h3>
<h4>简述：</h4>
简单的共享主机配置中，一台Web服务器只需要支持几个域名各不相同的虚拟Web站点。它通过Host消息头达到这个目的，在HTTP 1.1中，请求中必须包含该消息头。当浏览器提出一个HTTP请求时，请求中即包含一个Host请息头，该请息头中含有相关URL中的域名， 然后请求被传送到与域名关联的IP地址中，如果解析几个域名得到相同的IP地址，在这个地址上的服务器仍然能够确定请求希望访问哪一个Web站点。例如可以配置Apache使用以下配置支持几个Web站点，这个配置为每个虚拟主机站点设定各不相同的Web根目录


> 
<h3>1.3、共享的应用程序服务</h3>
<h4>简述：</h4>
1、许多ASP提供现成的应用程序，可由客户修改与定制后使用，对于拥有大量业务、需要部署功能强大复杂、能为终端用户提供基本相同功能的应用程序的行业，使用这种模型可以节省大量成本。使用ASP提供的这种服务，商家可迅速获得一个知名品牌的应用程序，而且不必投入大量的安装与维护成本
2、在金融服务行业，ASP应用程序市场特别成熟。例如，在某个国家，可能有数千家小型零售商希望向顾客提供店内支付卡与信贷服务，这些零售商将这项服务外包给若干不同的信用卡提供商， 其中许多提供商为新创办的企业，而非历史悠久的知名银行。这些信用卡提供商提供一种商品化服务，而成本是其中一个关键的竞争因索。因此许多提供商使用一家ASP为终端用户提供Web应用程序。因此每一家ASP都对相同的应用程序进行定制处理，以满足大量不同零售商的需求
3、这种服务的典型组织结构与责任划分，从不同代理商与相关任务的角度看， 这种服务存在与共享主机基本摸型相同的安全问题，但这些问题可能更复杂。且这种服务还存在其他特殊的问题




> 
<h3>1.4、攻击共享环境</h3>
<h4>简述：</h4>
共享主机与ASP环境引入一系列新的潜在漏洞，攻击者可利用它们针对共享基础架构中的一个或几个应用程序进行攻击
<hr/>
<h4>针对访问机制的攻击</h4>
因为各种外部组织需要更新与定制共享环境中的不同应用程序，提供商必须执行实现这种远程访问的机制。在最简单的虚拟主机Web站点中，FTP或SCP之类的上传工具即可达到这种目的，客户通过它们在自己的Web根目录中写入文件。
如果主机服务提供一个数据库，客户可能需要直接访问数据库，以配置数据库设置，获取应用程序保存的数据。这时提供商可执行一个实现某些数据库管理功能的接口，或通过因特网提供数据库服务，允许客户直接建立连接，并使用他们自己的工具

在成熟的ASP环境中，各种类型的客户需要对共享应用程序的组件进行不同程度的定制，这时提供商通常会运行功能强大的应用程序，帮助客户完成这些任务。通常通过一个VPN(虚拟专用网络）或一个连接ASP基础架构的专用连接，就可以访问这些应用程序

根据远程访问机制所涵盖的范围，攻击者可针对共享环境实施各种不同的攻击：
A、远程访问机制本身并不安全。如FTP协议未加密，使得处在适当位置（如在客户自己的ISP内）的攻击者能够截获登录证书，访问机制中还可能包含未打补丁的软件漏洞或配置缺陷，使得匿名攻击者能够避开访问机制，破坏客户的应用程序和数据
B、远程访问机置许可的访问可能过于宽泛，或未能对客户进行适当的隔离。如当用户只需要文件访问时，访问机制可能会为用户提供一个命令shell，另外访问机制可能并没有限制客户只能访问自己的目录，相反却允许他们更新其他客户的内容，或访问服务器操作系统中的敏感文件
C、在文件系统访问方面，同样的注意事项也适用于数据库，访问机制可能没有对数据库进行适当的隔离，为每名客户提供不同权限的账户，扛、直接数据库连接可能使用标准ODBC之类的非加密渠过来实现
D、如果部署一个定制应用程序实现远程访问（如通过一家ASP)，这个应用程序必须负责控制不同客户对共享应用程序的访问，管理应用程序中存在的任何漏洞都可能会导致恶意客户， 甚至是匿名用户破坏其他客户的应用程序，还会使拥有有限权限的客户能够更新应用程序的皮肤，从而提升其权限，或者修改应用程序核心功能组件，以实现他们的目的。如果部署了这种类型的管理应用程序，那么该应用程序中存在的任何漏洞都可能会导致针对终端用户访问的共享应用程序的攻击
<hr/>
<h4>应用程序间的攻击</h4>
在一个共享主机环境中，不同的客户通常需要向服务器合法上传并执行任意脚本。这会导致单主机应用程序中并不存在的问题
1、预留后门
在最明显的攻击中，恶意客户可能会上传攻击服务器自身或其他客户应用程序的内容（如Perl脚本在服务器上运行一个远程命令工具，从因特网上访问脚本，客户就能够在服务器上执行任意操作系统命令）
由于恶意客户的命令以Apachc用户的身份执行，这很可能使得该客户能够访问属于共享主机服务其他客户的脚本和数据。
ASP管理的共享应用程序中也存在这种威胁，虽然核心应用程序功能由ASP控制并更新，但个体用户还是能够以某种确定的方式修改这项功能，恶意客户可以在他们控制的代码中引入其他人难以察觉的后门，从而攻破共享应用程序，访问其他客户的数据

2、易受攻击的应用程序间的攻击
即使共享环境中的所有客户全都并无恶意，且仅上传经过环境所有者确认的合法脚本，但如果个别用户对存在于应用程序中的漏洞并不知情，应用程序之间的攻击仍有可能发生。在这种情况下，恶意用户可以利用某个应用程序中的漏洞攻破该应用程序以及共享环境中的所有其他应用程序。
许多常见的漏洞都属于这种类型：
A、攻击者可以利用某个应用程序中的SQL注人漏洞在共享数据库中执行任意SQL查询。如果<br/> 没有完全隔离访问数据库的不同客户，攻击者就可以读取并修改所有应用程序使用的数据。
B、攻击者可以利用某个应用程序中的路径遍历漏洞读取或写入服务器文件系统中的任意文件，包括那些属于其他应用程序的文件
C、攻击者可以采用与前面描述的恶意客户使用的方法类似的方法，利用某个应用程序中的命令注入漏洞攻破服务器以及服务器上运行的其他应用程序
<hr/>
<h4>ASP应用程序组件间的攻击</h4>
各种攻击可能会在共享ASP应用程序中发生，由于客户可以按照自己的需求对核心应用程序功能进行定制，因此定制应用程序的用户可以利用某名客户引入的漏洞攻击主共享应用程序，从而窃取所有ASP客户的数据。
除这些攻击以外，由于共享应用程序的各种组件必须彼此交互，因而恶意客户或用户能够攻破其他共享的应用程序
A、由不同应用程序生成的数据通常被分配到一个公共的位置，可以被共享应用程序中拥有较高权限的ASP级用户查看，这意味着攻击者可以利用定制应用程序中存在的XSS漏洞攻破共享应用程序。如果攻击者能够在日志文件条目、支付记录或者个人联系信息中注入JmScript代码，就可以劫持一名ASP级用户的会话，从而访问敏感的管理功能
B、ASP通常使用一个共享数据库保存所有客户的数据，应用程序与数据库层面是否对数据访问实施了严格的隔离，这一点无法确定。但无论是哪一种情况，都会存在一些共享组件，如数据库存储过程，它们负责处理属于多名客户的数据，恶意客户或用户可以利用这些组件中存在的有缺陷的信任关系或漏洞访问其他应用程序中的数据。如一个定义者权限共享存储过程中的SQL注入漏洞可能会导致整个共享数据库被攻破
<hr/>
<h4>过程：</h4>
1、检查为共享环境中的客户提供的、便于更新和管理内容与功能的访问机制
A、远程访问机制是否使用一个安全的协议与经过适当强化的基础架构
B、客户是否能够访问他们正常情况下不能访问的文件、数据及其他资源
C、客户是否能够在主机环境中获得一个交互式的shell，并执行任意命令

2、如果使用一个所有权应用程序，以方便客户配置和定制共享环境，考虑是否能够以这个应用程序为攻击目标，攻破该环境本身及其中运行的所有应用程序

3、如果能够在某个应用程序中执行命令、注入SQL脚本或访问任意文件，仔细研究看是否能够以此扩大攻击范围，攻破其他应用程序

4、如果正在攻击一个使用ASP主机的应用程序，且该应用程序由许多共享与定制组件构成， 确定其中的任何共享组件，如日志机制、管理功能以及数据库代码组件，尝试利用这些组件攻破应用程序的共享部分，进而攻破其他应用程序

5、如果所有共享环境使用一个常用的数据库，使用NGSSquirrel之类的数据库扫描工具，对数据库配置、补丁级别、表结构以及许可进行全面审查。数据库安全模页中存在的任何缺陷都可以被加以利用，将攻击范图由一个应用程序扩大到另一个应用程序。
<hr/>
<h4>攻击云</h4>
1、“云” 是指越来越多地将应用程序、服务器、数据库和硬件外包给外部服务提供商。它也指目前共享托管环境的环度虚拟化。云服务是指提供API、应用程序或用于客户交互的Web界面的基于因特网的按需服务。通常云计算提供商会存储用户数据或处理业务逻绢来提供相关服务。从终端用户的角度看，传统的桌面应用程序将升级为基于云的应用程序，各种企业可能会用按需服务来替代所有服务器

2、在迁移到云服务的过程中，缺乏控制是一个经常被提及的安全问题，与传统的服务器或桌面软件不同，用户没有办法提前评估特定云服务的安全性，而需要将管理服务和数据的所有责任交给第三方。对企业而言，他们需要将更多控制托付给某个环境，而该环境包含的风险却无法完全定性或量化，由于基于Web的平台并不像传统的客户端／服务器可下载的产品那样经过严格的测试， 因此在支持云服务的Web应用程序中发现的漏洞也往往不为人们所了解

3、这种对缺乏控制的担心，与当前企业在选择托管服务提供商、或用户在选择Web邮件服务商时的担忧类似。但仅仅这种担忧并不能反映云计算带来的日益严重的安全风险。攻破一个传统的Web应用程序可能会影响到成千上万名个体用户，但攻破云服务却可能影响到成千上万名云订阅用户及其用户群体。虽然存在缺陷的访问控制会使攻击者能够未授权访问工作流程应用程序中的敏感文档，但在云自助服务应用程序中，这种缺陷可能会导致攻击者能够未授权访问服务器或服务器集群。利用管理后端门户云服务中的同一漏洞，攻击者甚至能够访问整个企业基础架构

**Web应用程序角度的云安全**
由于定义不明确，每个云服务提供商的实施方式各不相同，因此并没有适用于所有云体系架构的漏洞列表。但我们仍然可以确定一些专门针对云计算体系架构的主要漏洞区域

**克隆系统**
在使用熵生成随机数字时，许多应用程序依赖操作系统的功能来执行这一操作，常用的熵源大多与系统本身的功能有关，如系统正常运行时间或有关系统硬件的信息，如果系统被克隆，拥有其中一个克隆系统的攻击者就可以确定用于生成随机数字的熵源，这些信息又可用于更准确地预测随机数字发生器的状态

**将管理工具迁移到云中**
用于配置和监视服务器的界面是企业云计算服务的核心应用。对用户而言，该界面是一个自助环境，通常是最初用于内部服务器管理的工具的Web版本，以前连接到网络的独立工具往往缺乏可靠的会话管理和访问控制机制，在没有预先采用基于角色的隔离的情况下更是如此。一些将令牌或GUID用于服务器访问的情况，在其他情况下，应用程序仅仅通过序列化接口来调用任何管理方法

**功能优先的方法**
和大多数新技术一样，云服务提供商采用功能优先的方法来吸引新用户，从企业的角度来看，云环境几乎总是通过自助Web应用程序管理，用户获得一系列用户友好的方法，并通过这些方法来访问数据，云服务通常并不提供功能"退出"机制

**基于今牌的访问**
用户需要定期调用大量云资源， 为此用户需要在客户端上存储一个永久身份验证令牌，以免输入密码，并用于标识设备（相对于用户）。如果攻击者能够访问该令牌，就可以借此访问用户的云资源

**Web存储**
Web存储是云计算吸引终端用户的优势之一，为发挥效率，Web存储必须支持某种标准的浏览器或浏览器扩展、一系列技术和HTTP扩展（如WebDAV)，并且通常需要支持存入缓存或基于令牌的证书<br/> 此外域上的Web服务器通常可以通过因特网访问，如果某个用户可以上传HTML文件并诱使其他用户访问其上传的文件，就可以攻破这些使用同一服务的用户。与此类似，攻击若可以利用Java同源策略并上传一个JAR文件，从而在该文件被因特网上的其他位置调用时实现完全的双向交互


#### 针对访问机制的攻击

---


#### ASP应用程序组件间的攻击

---


#### 攻击云

> 
<h3>1.5、保障共享环境的安全</h3>
<h4>简述：</h4>
由于使用相同工具的客户可能怀有恶意企图，以及不知情的客户可能无意中在环境中引入漏洞，因此共享环境给应用程序安全带来了新的威胁，为解决这种双重威胁，设计共享环境时必须仔细处理客户访问、隔离与信任关系，并实施并不直接适用于单主机应用程序的控制
<hr/>
<h4>保障客户访问的安全</h4>
无论向客户，提供何种机制来帮助他们维护自己控制的内容，都应防止这种机制被第三方和恶意客户未授权访问

1、远程访问机制应实施严格的身份确认，使用难以窃听的加密技术，并进行充分的安全强化。
2、仅准予个体用户最低的访问权限。如果一名客户需要向一台虚拟主机服务器上传脚本就应仅向他分配读取与写入他自己的文档根目录的访问权限。如果需要访问一个共享数据库，就应使用一个无法访问属于其他客户的数据或其他组件的低权限账户进行访问。
3、如果使用一个定制的应用程序提供客户访问，该应用程序必须满足严格的安全需求，并根据它在保护共享环境安全中发挥的作用进行测试。
<hr/>
<h4>隔离客户功能</h4>
不能信任共享环境中的客户，认为他们仅建立没有漏洞的无害功能。因此稳定可靠的解决方案是应使用架构控制来保护共享环境及其客户，避免受到通过不当内容实施的攻击。这要求隔离给予每名客户的功能，确保将任何有意或无意攻击的影响限制在局部，使其不会伤害其他客户

1、每名客户的应用程序应使用一个独立的操作系统账户访问文件系统，该账户仅拥有读取与写入应用程序文件路径的权限
2、强大系统功能与命令的访问权限应仅限于操作系统等级，且应只分配所需的最低权限
3、应在任何共享数据库中实施相同的保护措施，应为每名客户使用一个单独的数据库实例，仅向客户分配低权限的账户，只允许他们访问自己的数据
<hr/>
<h4>隔离共享应用程序中的组件</h4>
在ASP环境中，应用程序包含各种共享与定制的组件，这时应在各方控制的组件之间实施信任边界，如果一个数据库存储过程之类的共享组件接收从某一名客户的定制组件发出的数据，那么就不应信任这些数据，就好像它们是由终端用户送出的一样，每个组件都应对它的信任边界以外的相邻组件进行严格的安全测试，确定其中存在的、攻击者可以利用易受攻击的组件或恶意组件攻破其他应用程序的漏洞，应特别注意共享日志与管理功能


#### 保障客户访问的安全

---


#### 隔离共享应用程序中的组件
