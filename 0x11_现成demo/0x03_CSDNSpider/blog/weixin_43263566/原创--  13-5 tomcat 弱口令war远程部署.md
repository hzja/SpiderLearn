# 原创
：  13-5 tomcat 弱口令war远程部署

# 13-5 tomcat 弱口令war远程部署

#### 漏洞介绍 

Apache Tomcat 是一个开源的Web应用服务器，它主要用于部署和管理基于Java的Web应用程序。Tomcat 提供了一套完整的管理界面，允许管理员通过Web界面来部署、启动、停止和卸载Web应用程序。这些管理功能通过特定的角色和权限来控制访问。

在 Tomcat 中，权限是通过在`conf/tomcat-users.xml`文件中配置用户角色来管理的。不同的角色允许用户执行不同的操作。以下是Tomcat 7及以上版本中与管理相关的角色及其权限介绍：

1.  `manager`（后台管理）: 这是一个通用角色，通常不会直接赋予用户，而是作为其他管理角色的基础。 
1.  `manager-gui`（拥有html页面权限）: 允许用户通过HTML界面访问Tomcat管理界面。用户可以部署、撤销、启动、停止和重新加载Web应用，以及查看系统状态。 
1.  `manager-status`（拥有查看status的权限）: 允许用户查看Tomcat服务器的当前状态，包括JVM使用情况、会话数、以及各个Web应用的运行状态等。 
1.  `manager-script`（拥有text接口的权限,和status权限）: 允许用户通过文本接口（例如命令行工具或脚本）来执行管理操作，这些操作与`manager-gui`角色相同，但是不提供GUI界面。同时，这个角色也包含了查看服务器状态的权限。 
1.  `manager-jmx`（拥有jmx权限,和Status权限）: 允许用户通过Java管理扩展（Java Man
