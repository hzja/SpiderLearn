const https = require('https');
const fs = require("fs");
const path = require("path");

// 设置GitHub用户名和仓库名
const owner = 'NaiboWang';
const repo = 'EasySpider';
let config = fs.readFileSync(path.join(__dirname, `package.json`), 'utf8');
config = JSON.parse(config);
const version = config.version;
console.log(`Current version is ${version}`);
// 这段代码的主要功能是读取`package.json`文件中的版本信息，并将该版本信息输出到控制台。以下是代码的详细解释：
// 1. 定义两个变量`owner`和`repo`，分别赋值为`NaiboWang`和`EasySpider`。
// 2. 使用`fs.readFileSync`函数读取`package.json`文件，并将文件内容解析为字符串。
// 3. 使用`JSON.parse`函数将字符串解析为JSON对象。
// 4. 获取JSON对象中的`version`属性值，并将其赋值给变量`version`。
// 5. 使用`console.log`函数输出`version`变量的值，格式为`Current version is ${version}`。

// 发送GET请求获取GitHub的Release API响应
https.get(`https://api.github.com/repos/${owner}/${repo}/releases/latest`, {
    headers: {
        'User-Agent': 'Node.js'
    }
}, (res) => {
    let data = '';
    res.on('data', (chunk) => {
        data += chunk;
    });
    res.on('end', () => {
        // 解析响应JSON并输出最新版本号
        const release = JSON.parse(data);
        const latestVersion = release.tag_name.replace('v', '');
        console.log(`Latest version is ${latestVersion}`);
        // 如果当前版本不是最新版本，则提示最新版本号
        if(version !== latestVersion) {
            console.log('There is a new version of EasySpider, you can download it from github repo: https://github.com/NaiboWang/EasySpider/releases');
        }
    });
}).on('error', (err) => {
    console.error(`Error: ${err.message}`);
});
// 这段代码是用JavaScript编写的，用于获取GitHub仓库的最新版本号。以下是代码的详细解释：
// 1. 使用`https.get()`方法发起GET请求，请求的URL包含了`owner`和`repo`变量，这些变量在后续的请求中会被替换为实际的值。请求头中的`User-Agent`设置为`Node.js`。
// 2. 当收到响应时，会触发`res.on('data')`事件处理程序，将响应的数据存储在`data`变量中。
// 3. 当响应结束时，会触发`res.on('end')`事件处理程序，此时可以解析响应的JSON数据，获取最新版本号。然后，将最新版本号输出到控制台，并检查当前版本是否为最新版本。如果是，则输出一条提示信息，告诉用户可以从GitHub仓库下载最新版本。
// 4. 如果请求过程中发生错误，会触发`res.on('error')`事件处理程序，将错误信息输出到控制台。