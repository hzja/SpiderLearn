# 原创
：  32-5 XXE漏洞 - xml数据格式

# 32-5 XXE漏洞 - xml数据格式

#### 一、前置基础知识

**OWASP Top 10**：

OWASP是一个致力于提升网络应用安全的组织，其Top 10是指网络应用安全风险中最紧迫的十种。这些风险包括各种注入、身份验证问题、敏感数据泄露等。

**外部实体（External Entities）**：

1.  **DTD（Document Type Definition，文档类型定义）**：DTD是一种定义XML文档结构的规范。它可以包含实体声明，允许将外部实体引用包含在XML文档中。攻击者可以利用DTD中定义的实体来执行恶意操作，如读取敏感文件或执行任意代码。 
1.  **XML（eXtensible Markup Language，可扩展标记语言）**：XML是一种用于存储和传输数据的标记语言。XML文档可以包含外部实体引用，从而使得外部实体攻击成为可能。 
1.  **HTML（HyperText Markup Language，超文本标记语言）**：HTML是用于创建网页的标记语言。虽然HTML本身并不支持实体声明，但某些环境中（如浏览器）可能允许使用外部实体，从而导致类似的攻击。 

**注入**

注入攻击是一种常见的安全漏洞，其中SQL注入是其中一种形式。SQL注入攻击通常发生在以下情况下：

1.  **输入点**：攻击者利用应用程序的用户输入点，如表单、URL参数等，将恶意的SQL代码注入到输入中。 &lt;
