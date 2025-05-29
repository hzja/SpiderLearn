# 原创
：  【APP 逆向百例】淘某热点 APP 逆向分析

# 【APP 逆向百例】淘某热点 APP 逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

### 抓包分析

打开 app，在首页进行刷新，charles 配合 SocksDroid 进行抓包，结果如下：

其中要逆向的参数为 sign 参数。

### 逆向分析

定位这个参数的方法有很多，可以直接搜索关键字 sign，也可以 frida 进行 hook，这里我们使用 frida 对 Java 的 `HashMap` 类进行 hook，`HashMap` 是 Java 中用于存储键值对的类，一般参数的组成都会通过这个方法，hook 代码如下：

```
function showStacks() {
    Java.perform(function () {
      console.log(Java.use("android.util.Log").getStackTraceString(
        Java.use("java.lang.Throwable").$new()
    ));
	})
}

// HashMap.put 方法
function hook_hashMap(){
    var hashMap = Java.use("java.util.HashMap");
    hashMap.put.implementation = function (a,b){
        if (a === "sign"){
            // 查看调用栈
            showStacks()
        }
     console.log('hook_hashMap输出--&gt;',a,b)
     return this.put(a,b)
    }
}
Java.perform(function() {
    hook_hashMap()
});

```

使用 `frida -UF -l demo.js -o 1.txt` 命令进行 frida 注入，注意捕获到的东西可能有点多，可以在输出一段时间后，在控制台输入 exit 回车关掉。

输出结果如下，直接输入 sign 的值，发现存在，并打印出了堆栈：

### java 层分析

把 apk 文件拖到 jadx 进行，根据堆栈信息进行搜索，最终定位到下图这个地方：

找到 a 函数：

其中 `TreUtil.sign` 函数就是我们生成处，可以使用 frida 代码验证位置是否正确，鼠标放到 sign 右键复制 frida 代码：

```
function hook1(){
    let TreUtil = Java.use("com.maihan.tredian.util.TreUtil");
    TreUtil["sign"].implementation = function (str) {
        console.log('sign is called' + ', ' + 'str: ' + str);
        let ret = this.sign(str);
        console.log('sign ret value is ' + ret);
        return ret;
    };

}
Java.perform(function () {
    hook1();
})


```

发现结果一致，我们继续向下分析，点进去这个函数，最后定位到 native 层加密，并加载 `tre.so` 文件：

我们把这个加密写成主动调用的方式，方便我们后续进行分析，代码如下：

```
// sign
function call_taozui(){
    let TreUtil = Java.use("com.maihan.tredian.util.TreUtil");
    // 主动调用sign方法
    let str = "android_id=9a8493c270cc2270&amp;app_ver=87&amp;channel=aliapp&amp;device_id=5e9bdbbc3bc779c18511c1bb26351dad&amp;device_udid=8f6e2b8cf3b2e3c36db8dea8368d7305&amp;first_time=1706003627&amp;from=app&amp;last_time=1695744000&amp;limit=8&amp;mac=0E:D8:C1:64:25:37&amp;nonce=4vlwb71740715028559&amp;os_ver_code=30&amp;system=1&amp;timestamp=1740715028&amp;with_super=0&amp;with_video=1";  // 假设你需要传递的字符串
    console.log('Before calling sign, str: ' + str);
    // 调用sign方法
    let result = TreUtil.sign(str);
    console.log('After calling sign, result: ' + result);
}

```

### so 层分析

我们从 apk 拿到 `pre.so` 文件，文件在 lib 目录下：

将该 so 文件放到 ida 进行分析，还是先在导出表里搜索 java，看是否是静态注册的，可以看到是的：

点进 sign 函数：<img alt="7cyDM7.png" src="https://i-blog.csdnimg.cn/img_convert/c5e478f944dca2c50e8fcaed8e07dfe9.png"/>

可以看到很明显的 sha1 算法字样，我们把前面主动调用的参数拿到 K 哥工具站：

> 
https://www.kgtools.cn/secret/sha


验证下是否为标准算法：

可以看到，计算结果不一致。这表明在 `SHA-1` 算法的执行过程中，可能有额外的处理步骤，我们需要进一步分析。继续向下分析，找到了一个关键函数：`j_base64_encode_new`。这个函数接受一个字符，该字符的长度以及 `v12` 作为参数，点进该函数：

看起来像是在做 base64 编码，并把第二个参数当作返回值返回，为了便于分析，我们使用 frida hook 该函数，按 tab 键，找到该函数的地址：

hook 代码如下：

```
var soAddr = Module.findBaseAddress("libtre.so");
// 32 位需要加 1 
var base64_encode_new = soAddr.add(0x13B4+1);
Interceptor.attach(base64_encode_new,{
    onEnter:function (args){
        console.log("参数1",args[0].readCString());
        console.log("参数2",hexdump(args[1]));
        console.log("参数3",args[2].toInt32());
    },
    onLeave:function (retval){
        console.log("返回值为:",retval.readCString())
    }
});

```

观察打印日志，可以看到在查询参数后面加上了一段字符，然后在进行 base64 编码，回到 sign 函数，该字符如下：

然后把编码好的变量 v12 进行标准的 sha1 算法加密：

经测试，为标准的加密算法。

对于这个参数加密流程，其实我们可以借助当下较火的 deepseek 分析一下这个函数，这里给出 deepseek 部分解释：

关键如下：

可以看到，deepseek 说的也很清楚明了，先进行加盐，然后 base64 编码，最后进行 sha1 算法进行加密。

至此，对该参数的加密分析到此结束。

相关代码文件，会分享到知识星球当中，需要的小伙伴自取，仅供学习交流。

### 结果验证
