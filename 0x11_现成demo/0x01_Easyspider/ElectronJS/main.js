// Modules to control application life and create native browser window
const {app, BrowserWindow, dialog, ipcMain, screen, session} = require('electron');
// 这段代码中的`require('electron')`是从全局模块缓存中加载Electron模块。Electron是一个跨平台的JavaScript库，用于开发桌面应用程序，如浏览器窗口、菜单、工具栏等。Electron通常位于Node.js的安装路径中，例如在Node.js的`node_modules`文件夹中。
// 在Windows上，Electron的默认安装路径可能是`C:\Users\{username}\AppData\Roaming\npm\node_modules\electron\dist\electron.js`。在macOS和Linux上，Electron的默认安装路径可能是`/usr/local/lib/node_modules/electron/dist/electron.js`或`/usr/lib/node_modules/electron/dist/electron.js`。
// 需要注意的是，Electron的安装路径可能会因用户安装Node.js的方式而有所不同。此外，如果用户使用的是npm全局安装的Electron，那么Electron的路径可能位于`/usr/local/lib/node_modules/electron`或`/usr/lib/node_modules/electron`。

app.commandLine.appendSwitch("--disable-http-cache");
const {Builder, By, Key, until} = require("selenium-webdriver");
const chrome = require('selenium-webdriver/chrome');
const {ServiceBuilder} = require('selenium-webdriver/chrome');
const {rootCertificates} = require('tls');
const {exit} = require('process');
const path = require('path');
const fs = require('fs');
const {exec, spawn} = require('child_process');
const iconPath = path.join(__dirname, 'favicon.ico');
const task_server = require(path.join(__dirname, 'server.js'));
const util = require('util');
// 这段代码是用JavaScript编写的，主要用于开发Electron应用程序。以下是代码的逐行解释：
// 1. 导入所需的模块和库：`const {app, BrowserWindow, dialog, ipcMain, screen, session} = require('electron');` 这些模块是Electron提供的，用于创建和控制应用程序的各个组件。
// 2. 添加一个命令行选项以禁用HTTP缓存：`app.commandLine.appendSwitch("--disable-http-cache");` 禁用HTTP缓存可以提高页面加载速度。
// 3. 导入所需的模块和库：`const {Builder, By, Key, until} = require("selenium-webdriver");` 这些模块是用于自动化Web浏览器操作的Selenium WebDriver的一部分。
// 4. 导入所需的模块和库：`const chrome = require('selenium-webdriver/chrome');` 该模块提供了一种与Chrome浏览器进行交互的方法。
// 5. 导入所需的模块和库：`const {ServiceBuilder} = require('selenium-webdriver/chrome');` 该模块提供了一种创建Chrome浏览器服务的方法。
// 6. 导入所需的模块和库：`const {rootCertificates} = require('tls');` 该模块提供了一种访问根证书的方法。
// 7. 导入所需的模块和库：`const {exit} = require('process');` 该模块提供了一种退出进程的方法。
// 8. 导入所需的模块和库：`const path = require('path');` 该模块提供了一种操作路径的方法。
// 9. 导入所需的模块和库：`const fs = require('fs');` 该模块提供了一种操作文件系统的方法。
// 10. 导入所需的模块和库：`const {exec, spawn} = require('child_process');` 该模块提供了一种执行子进程和创建子进程的方法。
// 11. 导入所需的模块和库：`const iconPath = path.join(__dirname, 'favicon.ico');` 该模块将当前目录和文件名连接在一起，创建一个图标文件的路径。
// 12. 导入所需的模块和库：`const task_server = require(path.join(__dirname, 'server.js'));` 该模块从指定路径加载一个名为server.js的文件。
// 13. 导入所需的模块和库：`const util = require('util');` 该模块提供了一些实用功能。

let config = fs.readFileSync(path.join(task_server.getDir(), `config.json`), 'utf8');
config = JSON.parse(config);
// 这段代码的主要功能是读取一个名为`config.json`的文件，该文件位于`task_server.getDir()`目录下，并将其内容解析为JavaScript对象。
// 1. 首先，使用`fs.readFileSync()`方法读取`config.json`文件的内容，该方法会阻塞代码执行，直到文件读取完成。
// `readFileSync()`方法的第一个参数是文件路径，第二个参数是文件编码（这里是`utf8`），第三个参数是可选的回调函数。
// 2. 然后，使用`JSON.parse()`方法将文件内容解析为JavaScript对象。`parse()`方法将字符串参数解析为JavaScript对象，返回解析后的对象。
// 3. 将解析后的对象赋值给变量`config`
// 总之，这段代码的作用是读取一个名为`config.json`的文件，并将其内容解析为一个JavaScript对象。

if(config.debug){
    let logPath = 'info.log'
    let logFile = fs.createWriteStream(logPath, { flags: 'a' })
    console.log = function() {
        logFile.write(util.format.apply(null, arguments) + '\n')
        process.stdout.write(util.format.apply(null, arguments) + '\n')
        // 这段代码是用于将一些参数格式化为字符串并写入日志文件和标准输出流（通常是终端）。
        // 1. `logFile.write(util.format.apply(null, arguments) + '\n')`: 这里使用了 `util.format.apply()` 函数来格式化参数，并将结果附加一个换行符（`\n`）后写入到名为 `logFile` 的文件对象。
        // 2. `process.stdout.write(util.format.apply(null, arguments) + '\n')`: 这里也是同样地使用 `util.format.apply()` 函数来格式化参数，并将结果附加一个换行符（`\n`）后写入到标准输出流（通常是终端）。

    }
    console.error = function() {
        logFile.write(util.format.apply(null, arguments) + '\n')
        process.stderr.write(util.format.apply(null, arguments) + '\n')
        // 这段代码是用JavaScript编写的，用于将格式化后的日志信息写入日志文件和输出到控制台。
        // 1. `logFile.write(util.format.apply(null, arguments) + '\n')`：这里使用了`util.format.apply()`方法来格式化日志信息，并将结果与换行符（`\n`）一起写入日志文件。`null`作为第一个参数传递给`apply()`方法，因为它需要一个上下文对象。`arguments`是一个包含日志信息的可变参数数组，`apply()`方法会将这些参数作为数组传递给格式化函数。最后，格式化后的日志信息将被写入日志文件。
        // 2. `process.stderr.write(util.format.apply(null, arguments) + '\n')`：这里也是同样的操作，`util.format.apply()`方法用于格式化日志信息，并将结果与换行符（`\n`）一起写入控制台。`process.stderr`是一个全局对象，表示进程的错误流，即输出错误信息的地方。这个代码片段将格式化后的日志信息写入控制台。

    }
}
// 这段代码是在JavaScript中定义的，主要用于在调试模式下记录控制台输出到日志文件。当`config.debug`的值为`true`时，将会执行以下操作：
// 1. 定义一个日志文件的路径`logPath`，默认为`info.log`。
// 2. 使用`fs.createWriteStream`方法创建一个可追加写入的文件流对象`logFile`，参数`{ flags: 'a' }`表示以追加模式打开文件。
// 3. 重写`console.log`和`console.error`函数，使其在调用时记录输出到日志文件和控制台。
// 具体来说，当调用`console.log()`或`console.error()`时，代码会将原始参数（包括格式化后的字符串）写入日志文件和控制台。日志文件以追加模式打开，每次调用都会将输出追加到文件末尾。

let allWindowSockets = [];
let allWindowScoketNames = [];
task_server.start(config.webserver_port); //start local server
let server_address = `${config.webserver_address}:${config.webserver_port}`;
const websocket_port = 8084; //目前只支持8084端口，写死，因为扩展里面写死了
console.log("server_address: " + server_address);
let driverPath = "";
let chromeBinaryPath = "";
let execute_path = "";
console.log(process.arch);
// 这段代码是用JavaScript编写的，主要功能如下：
// 1. 定义三个变量：`allWindowSockets`、`allWindowScoketNames`和`server_address`。
// 2. 调用`task_server.start(config.webserver_port)`函数，启动本地服务器。
// 3. 定义一个变量`server_address`，其值为`config.webserver_address`和`config.webserver_port`的组合，其中`config.webserver_address`是配置文件中的地址，`config.webserver_port`是配置文件中的端口。
// 4. 定义一个常量`websocket_port`，目前只支持8084端口，写死，因为扩展里面写死了。
// 5. 输出`server_address`的值。
// 6. 定义三个空字符串：`driverPath`、`chromeBinaryPath`和`execute_path`。
// 7. 输出`process.arch`的值，`process.arch`表示当前运行的计算机架构。

exec(`wmic os get Caption`, function(error, stdout, stderr) {
    if (error) {
        console.error(`执行的错误: ${error}`);
        return;
    }

    if (stdout.includes('Windows 7')) {
        console.log('Windows 7');
        let sys_arch = config.sys_arch;
        if (sys_arch === 'x64') {
            dialog.showMessageBoxSync({
                type: 'error',
                title: 'Error',
                message: 'Windows 7系统请下载使用x32版本的软件，不论Win 7系统为x64还是x32版本。\nFor Windows 7, please download and use the x32 version of the software, regardless of whether the Win 7 system is x64 or x32 version.',
            });
        }
    } else {
        console.log('Not Windows 7');
    }
});
// 这段代码是用JavaScript编写的，用于检查当前操作系统是否为Windows 7。如果当前操作系统是Windows 7，它会显示一个错误消息，要求用户下载使用32位版本的软件。如果当前操作系统不是Windows 7，它会输出“Not Windows 7”。
// 1. 首先，使用`exec()`函数执行一个命令，该命令使用`wmic os get Caption`获取操作系统的名称。`exec()`函数的回调函数将在命令执行完成后被调用。
// 2. 在回调函数中，首先检查是否有错误。如果有错误，它会输出一个包含错误信息的错误消息，并返回。
// 3. 如果没有错误，它会检查`stdout`是否包含“Windows 7”字符串。如果包含，说明当前操作系统是Windows 7。
// 4. 如果当前操作系统是Windows 7，它会从`config`对象中读取`sys_arch`属性，并检查它是否为'x64'。如果是，它会显示一个包含错误消息的对话框，要求用户下载使用32位版本的软件。
// 5. 如果当前操作系统不是Windows 7，它会输出“Not Windows 7”。


if (process.platform === 'win32' && process.arch === 'ia32') {
    driverPath = path.join(__dirname, "chrome_win32/chromedriver_win32.exe");
    chromeBinaryPath = path.join(__dirname, "chrome_win32/chrome.exe");
    execute_path = path.join(__dirname, "chrome_win32/execute.bat");
} else if (process.platform === 'win32' && process.arch === 'x64') {
    driverPath = path.join(__dirname, "chrome_win64/chromedriver_win64.exe");
    chromeBinaryPath = path.join(__dirname, "chrome_win64/chrome.exe");
    execute_path = path.join(__dirname, "chrome_win64/execute.bat");
} else if (process.platform === 'darwin') {
    driverPath = path.join(__dirname, "chromedriver_mac64");
    chromeBinaryPath = path.join(__dirname, "chrome_mac64.app/Contents/MacOS/Google Chrome");
    execute_path = path.join(__dirname, "");
} else if (process.platform === 'linux') {
    driverPath = path.join(__dirname, "chrome_linux64/chromedriver_linux64");
    chromeBinaryPath = path.join(__dirname, "chrome_linux64/chrome");
    execute_path = path.join(__dirname, "chrome_linux64/execute.sh");
}
// console.log(driverPath, chromeBinaryPath, execute_path);
// 这段代码是用JavaScript编写的，用于根据操作系统的不同，设置chromedriver和Google Chrome的路径。
// 首先，它检查当前操作系统的平台和架构。如果系统是Windows，并且架构是32位，那么它将设置Windows 32位版本的chromedriver和Google Chrome的路径。如果系统是Windows，并且架构是64位，那么它将设置Windows 64位版本的chromedriver和Google Chrome的路径。
// 如果系统是macOS，那么它将设置macOS 64位版本的chromedriver和Google Chrome的路径。
// 如果系统是Linux，那么它将设置Linux 64位版本的chromedriver和Google Chrome的路径。
// 最后，它将driverPath、chromeBinaryPath和execute_path分别输出到控制台。

let language = "en";
let driver = null;
let mainWindow = null;
let flowchart_window = null;
let current_handle = null;
let old_handles = [];
let handle_pairs = {};
let socket_window = null;
let socket_start = null;
let socket_flowchart = null;
let invoke_window = null;
// 这段代码是用JavaScript编写的，定义了9个变量。它们的作用如下：
// 1. `language`:这是一个字符串变量，表示当前语言设置为英文（en）。
// 2. `driver`:这是一个变量，表示驱动程序的引用。
// 3. `mainWindow`:这是一个变量，表示主窗口的引用。
// 4. `flowchart_window`:这是一个变量，表示流程图窗口的引用。
// 5. `current_handle`:这是一个变量，表示当前窗口句柄。
// 6. `old_handles`:这是一个数组变量，用于存储旧的窗口句柄。
// 7. `handle_pairs`:这是一个对象变量，用于存储窗口句柄及其对应的名称。
// 8. `socket_window`:这是一个变量，表示套接字窗口的引用。
// 9. `socket_start`:这是一个变量，表示套接字启动的引用。
// 10. `socket_flowchart`:这是一个变量，表示套接字流程图的引用。
// 11. `invoke_window`:这是一个变量，表示调用窗口的引用。

// var ffi = require('ffi-napi');
// var libm = ffi.Library('libm', {
//   'ceil': [ 'double', [ 'double' ] ]
// });
// libm.ceil(1.5); // 2
// const {user32FindWindowEx,
//   winspoolGetDefaultPrinter,} = require('win32-api/fun');
// async function testt(){
//   // 获取当前电脑当前用户默认打印机名
//   const printerName = await winspoolGetDefaultPrinter()
//   console.log(printerName);
// }

// testt();

function createWindow() {
    // Create the browser window.
    mainWindow = new BrowserWindow({
        width: 550,
        height: 750,
        webPreferences: {
            preload: path.join(__dirname, 'src/js/preload.js')
        },
        icon: iconPath,
        // frame: false, //取消window自带的关闭最小化等
        resizable: false //禁止改变主窗口尺寸
    })

    // and load the index.html of the app.
    // mainWindow.loadFile('src/index.html');
    mainWindow.loadURL(server_address + '/index.html?user_data_folder=' + config.user_data_folder+"&copyright=" + config.copyright, { extraHeaders: 'pragma: no-cache\n' });
    // 隐藏菜单栏
    const {Menu} = require('electron');
    Menu.setApplicationMenu(null);
    mainWindow.on('close', function (e) {
        if (process.platform !== 'darwin') {
            app.quit();
        }
    });
    // mainWindow.webContents.openDevTools();
    // Open the DevTools.
    // mainWindow.webContents.openDevTools()
}
// 这段代码是用JavaScript编写的，定义了一个名为`createWindow`的函数。这个函数的主要目的是创建一个浏览器窗口，并加载应用程序的`index.html`文件。以下是代码的详细解释：
// 1. 首先，创建了一个名为`mainWindow`的`BrowserWindow`对象。这个对象表示应用程序的主窗口。
// 2. 接下来，为`mainWindow`对象设置了一些属性，包括宽度、高度、预加载脚本路径、图标路径和是否允许窗口缩放等。
// 3. 然后，使用`loadURL`方法加载应用程序的`index.html`文件。这个方法接受两个参数：服务器地址和请求头。请求头包括一个`Pragma`头，用于防止浏览器缓存。
// 4. 接着，使用`require`方法引入了一个名为`Menu`的模块。这个模块可能是用于设置应用程序的菜单。
// 5. 然后，使用`Menu.setApplicationMenu`方法将菜单设置为`null`，这意味着禁用了应用程序的菜单。
// 6. 最后，定义了一个名为`close`的事件处理程序，当用户关闭窗口时触发。在这个处理程序中，首先检查用户操作系统是否为`darwin`（macOS），如果不是，则使用`app.quit()`方法关闭应用程序。
// 总之，这段代码定义了一个函数，用于创建一个浏览器窗口并加载应用程序的`index.html`文件。同时，它还隐藏了菜单栏，并定义了一个关闭窗口的事件处理程序。

async function beginInvoke(msg, ws) {
    if (msg.type == 1) {
        if (msg.message.id != -1) {
            let url = "";
            if (language == "zh") {
                url = server_address + `/taskGrid/FlowChart_CN.html?id=${msg.message.id}&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address;
            } else if (language == "en") {
                url = server_address + `/taskGrid/FlowChart.html?id=${msg.message.id}&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address;
            }
            console.log(url);
            flowchart_window.loadURL(url, { extraHeaders: 'pragma: no-cache\n' });
        }
        // 这段代码是在JavaScript中判断一个名为`msg`的对象是否具有有效的消息ID，并根据语言环境（`language`）生成不同的URL。
        // 1. 首先，检查`msg.message.id`是否不等于-1，如果是，则继续执行以下操作。
        // 2. 定义一个空字符串`url`。
        // 3. 然后，根据`language`的值，分别生成两个URL：
        //     a. 如果`language`等于"zh"，那么URL的格式为`server_address + "/taskGrid/FlowChart_CN.html?id=${msg.message.id}&wsport=${websocket_port}&backEndAddressServiceWrapper=" + server_address`。
        //     b. 如果`language`等于"en"，那么URL的格式为`server_address + "/taskGrid/FlowChart.html?id=${msg.message.id}&wsport=${websocket_port}&backEndAddressServiceWrapper=" + server_address`。
        // 4. 使用`console.log(url)`输出生成的URL。
        // 5. 使用`flowchart_window.loadURL(url, { extraHeaders: 'pragma: no-cache\n' })`加载URL到`flowchart_window`。
        
        mainWindow.hide();
        // 这段代码是用于隐藏主窗口的。它是Qt GUI应用程序中的一个常见操作，当用户点击关闭按钮或按快捷键（如Ctrl+Q）时，应用程序将隐藏主窗口，但仍然可以在后台运行。当用户再次打开应用程序时，主窗口将重新显示出来。
        
        if(process.platform != "linux" && process.platform != "darwin"){
            const {windowManager} = require("node-window-manager");
            const window = windowManager.getActiveWindow();
            console.log(window);
            windowManager.requestAccessibility();
            // Sets the active window's bounds.
            let size = screen.getPrimaryDisplay().workAreaSize
            let width = parseInt(size.width)
            let height = parseInt(size.height * 0.6)
            window.setBounds({x: 0, y: size.height * 0.4, height: height, width: width});
        }
        // 这段代码是用JavaScript编写的，主要用于在Linux和macOS操作系统上获取当前活动窗口的信息，并调整其大小。以下是代码的详细解释：
        // 1. 首先，使用`process.platform`变量检查当前操作系统是否为Linux或macOS。如果不是，则执行以下操作。
        // 2. 导入`node-window-manager`库，该库提供了与操作系统窗口管理器交互的方法。
        // 3. 使用`require("node-window-manager")`获取`windowManager`对象。
        // 4. 使用`windowManager.getActiveWindow()`获取当前活动窗口。
        // 5. 打印当前活动窗口的信息。
        // 6. 调用`windowManager.requestAccessibility()`请求访问权限，以访问操作系统窗口管理器。
        // 7. 获取屏幕的主要显示器的工作区域大小。
        // 8. 将宽度设置为工作区域大小的整数部分，高度设置为工作区域高度的60%。
        // 9. 使用`window.setBounds({x: 0, y: size.height * 0.4, height: height, width: width})`设置活动窗口的大小和位置。

        flowchart_window.show();
        // 这段代码是在使用JavaScript的`flowchart_window.show()`方法来显示一个名为`flowchart_window`的窗口。
        // 具体来说，`flowchart_window`是一个预先定义好的窗口对象，现在调用`show()`方法来显示该窗口。
        
    } else if (msg.type == 2) {
        // 键盘输入事件
        // const robot = require("@jitsi/robotjs");
        let keyInfo = msg.message.keyboardStr;
        let handles = await driver.getAllWindowHandles();
        console.log("handles", handles);
        let exit = false;
        let content_handle = handle_pairs[msg.message.id];
        console.log(msg.message.id,  content_handle);
        let order = [...handles.filter(handle => handle != current_handle && handle != content_handle), current_handle, content_handle]; //搜索顺序
        let len = order.length;
        // 这段代码是用JavaScript编写的，主要用于处理键盘消息。以下是代码的详细解释：
        // 1. 首先，从传入的`msg`对象中提取`keyboardStr`属性，将其存储在`keyInfo`变量中。
        // 2. 使用`await`关键字等待`driver.getAllWindowHandles()`方法执行，获取所有窗口的句柄，并将结果存储在`handles`变量中。
        // 3. 输出`handles`变量，用于调试。
        // 4. 定义一个名为`exit`的布尔变量，初始值为`false`。
        // 5. 获取与`msg.message.id`关联的句柄，存储在`content_handle`变量中。
        // 6. 输出`msg.message.id`和`content_handle`，用于调试。
        // 7. 创建一个名为`order`的新数组，使用`...`运算符将`handles.filter()`的结果展开，并将其添加到`order`数组中。同时，将当前窗口的句柄`current_handle`和`content_handle`分别添加到`order`数组中。
        // 8. 获取`order`数组的长度，存储在`len`变量中。
        // 这段代码主要用于处理键盘消息，包括获取所有窗口的句柄、提取与`msg.message.id`关联的句柄以及搜索顺序的创建。

        while (true) {
            // console.log("handles");
            try{
                let iframe = msg.message.iframe;
                let enter = false;
                // 这段代码的主要功能是设置一个变量`iframe`的值，以及一个布尔变量`enter`的值为`false`。
                //     1. `let iframe = msg.message.iframe;`：这一行代码首先定义了一个变量`iframe`，并将`msg.message.iframe`的值赋给它。`msg.message`可能是一个包含消息的对象，其中`iframe`是一个属性，表示消息中的iframe内容。
                //     2. `let enter = false;`：这一行代码定义了一个名为`enter`的布尔变量，并将其值设置为`false`。这意味着在当前情况下，变量`enter`的值将被视为`false`。
                
                if (/<enter>/i.test(keyInfo)) {
                    keyInfo = keyInfo.replace(/<enter>/gi, '');
                    enter = true;
                }
                // 这段代码是用JavaScript编写的，用于处理键盘输入。它的功能是检查用户输入的键盘信息（keyInfo），并判断是否包含"<enter>"字符串。如果是，则将"<enter>"替换为空字符串，并将变量enter设置为true。
                // 具体来说，代码首先使用正则表达式/<enter>/i来检查keyInfo是否包含"<enter>"字符串。其中，i表示不区分大小写。如果包含，则执行以下操作：
                // 1. 使用replace方法将keyInfo中的所有"<enter>"字符串替换为空字符串。这里使用了全局匹配（gi）选项，因此会替换所有匹配的字符串，而不是只替换第一个。
                // 2. 将变量enter设置为true，表示已经找到了"<enter>"字符串。
                // 这段代码主要用于处理用户输入的键盘信息，例如在输入文本时，用户可能会输入"<enter>"来表示换行符。这时，这段代码可以将其替换为空字符串，从而实现换行的功能。
                
                let h = order[len - 1];
                console.log("current_handle", current_handle);
                if(h != null && handles.includes(h)){
                    await driver.switchTo().window(h);
                    current_handle = h;
                    console.log("switch to handle: ", h);
                }
                // 这段代码是用JavaScript编写的，主要用于处理浏览器窗口的切换。以下是代码的详细解释：
                // 1. 首先，创建一个变量`h`，将其初始化为`order[len - 1]`。这里的`order`是一个数组，`len`也是一个变量，表示数组的长度。通过这种方法，`h`变量将存储数组的最后一个元素。
                // 2. 然后，使用`console.log`函数打印当前窗口的句柄`current_handle`。
                // 3. 接下来，使用`if`语句检查`h`是否不为`null`且`handles`数组包含`h`。如果条件为真，则执行以下操作：
                // a. 使用`await`关键字等待驱动程序切换到窗口`h`。
                // b. 将`current_handle`变量更新为`h`。
                // c. 使用`console.log`函数打印切换到的新窗口句柄`h`。
                // 这段代码的主要目的是在处理浏览器窗口时切换到指定的窗口，并在控制台中记录当前和切换后的窗口句柄。

                // await driver.executeScript("window.stop();");
                // console.log("executeScript");
                if(!iframe){
                    let element = await driver.findElement(By.xpath(msg.message.xpath));
                    console.log("Find Element at handle: ", current_handle);
                    // 使用正则表达式匹配 '<enter>'，不论大小写
                    await element.sendKeys(Key.HOME, Key.chord(Key.SHIFT, Key.END), keyInfo);
                    if(enter){
                        await element.sendKeys(Key.ENTER);
                    }
                    console.log("send key");
                    break;
                } 
                // 这段代码是用JavaScript编写的，主要用于在自动化测试中操作浏览器。它首先检查一个名为`iframe`的变量是否为`undefined`，如果是，则执行以下操作：
                // 1. 使用`driver.findElement()`方法在浏览器中查找与给定XPath匹配的元素。`msg.message.xpath`是一个变量，表示要查找的元素的XPath。
                // 2. 在找到元素后，将元素的句柄（handle）打印到控制台。
                // 3. 使用正则表达式匹配`<enter>`，不论大小写。`keyInfo`是一个变量，表示要发送到元素的键。
                // 4. 向元素发送键盘按键组合，包括`Key.HOME`、`Key.chord()`和`Key.END`。
                // 5. 如果`enter`为`true`，则向元素发送`Key.ENTER`键。
                // 6. 打印"send key"。
                // 7. 跳出循环

                else {
                    let iframes = await driver.findElements(By.tagName('iframe'));
                    // 遍历所有的 iframe 并点击里面的元素
                    for(let i = 0; i < iframes.length; i++) {
                        let iframe = iframes[i];
                        // 切换到 iframe
                        await driver.switchTo().frame(iframe);
                        // 在 iframe 中查找并点击元素
                        let element;
                        try {
                            element = await driver.findElement(By.xpath(msg.message.xpath));
                        } catch (error) {
                            console.log('No such element found in the iframe');
                        }
                        if (element) {
                            await element.sendKeys(Key.HOME, Key.chord(Key.SHIFT, Key.END), keyInfo);
                            if(enter){
                                await element.sendKeys(Key.ENTER);
                            }
                        }
                        // 完成操作后切回主文档
                        await driver.switchTo().defaultContent();
                    }
                    break;
                }
                // 这段代码是用JavaScript编写的，主要用于自动化浏览器操作。它主要用于在网页上查找并点击特定的元素，这些元素可能在不同的iframe中。以下是代码的详细解释：
                //     1. `else {`：表示如果条件语句中的条件为false，则执行该代码块。
                //     2. `let iframes = await driver.findElements(By.tagName('iframe'));`：使用`driver`对象查找页面中所有的`iframe`元素，并将它们存储在`iframes`变量中。`await`关键字用于等待异步操作完成。
                //     3. `for(let i = 0; i < iframes.length; i++) {`：使用`for`循环遍历`iframes`数组中的所有`iframe`元素。
                    // 4. `let iframe = iframes[i];`：在每次循环中，将`iframes`数组中的当前`iframe`元素存储在`iframe`变量中。
                    // 5. `await driver.switchTo().frame(iframe);`：使用`switchTo()`方法将浏览器切换到当前`iframe`元素。
                    // 6. `let element;`：声明一个变量`element`，用于存储在`iframe`中找到的元素。
                    // 7. `try {`：使用`try`语句捕获可能发生的异常。
                    // 8. `element = await driver.findElement(By.xpath(msg.message.xpath));`：使用`findElement()`方法在`iframe`中查找与给定XPath匹配的元素，并将找到的元素存储在`element`变量中。`await`关键字用于等待异步操作完成。
                    // 9. `if (element) {`：如果找到了元素，则执行以下操作：
                    // a. `await element.sendKeys(Key.HOME, Key.chord(Key.SHIFT, Key.END), keyInfo);`：使用`sendKeys()`方法向找到的元素发送键盘按键。`Key.HOME`表示按下Home键，`Key.chord(Key.SHIFT, Key.END)`表示按下Shift + End键，`keyInfo`表示要发送的键盘按键。
                    // b. `if(enter){`：条件语句，判断是否需要按下Enter键。
                    // c. `await element.sendKeys(Key.ENTER);`：如果需要，则使用`sendKeys()`方法向找到的元素发送Enter键。
                    // 10. `}`：条件语句的结束。
                    // 11. `await driver.switchTo().defaultContent();`：完成操作后，使用`switchTo()`方法将浏览器切换回主文档。
                    // 12. `}`：循环的结束。
                    // 13. `break;`：跳出循环。
            } catch (error) {
                console.log("len", len);
                len = len - 1;
                if (len == 0) {
                    break;
                }
            }
            // 这段代码是在JavaScript的`try`和`catch`语句中使用的`catch`语句。当`try`语句中的代码发生错误时，`catch`语句将被执行。
            //     在`catch`语句中，首先将错误对象`error`赋值给`console.log`的参数，这样就可以在控制台中打印出错误信息。
            //     接着，将`len`的值减1，然后再次检查`len`是否等于0。如果是，则使用`break`语句跳出循环。这样就可以确保在循环结束后，`len`的值始终为正数。
        }
    } else if (msg.type == 3) {
        try {
            
            if (msg.from == 0) {

                socket_flowchart.send(msg.message.pipe); //直接把消息转接
                let message = JSON.parse(msg.message.pipe);
                let type = message.type;
                console.log("FROM Browser: ", message);
                console.log("Iframe:", message.iframe);
                // 这段代码是用JavaScript编写的，主要用于处理socket通信。以下是代码的详细解释：
                // 1. `socket_flowchart.send(msg.message.pipe);`：这行代码将消息（`msg.message.pipe`）直接发送给socket。`socket_flowchart`是一个socket对象，`send`方法用于发送消息。
                // 2. `let message = JSON.parse(msg.message.pipe);`：这行代码将消息（`msg.message.pipe`）解析为JSON格式，并将结果存储在变量`message`中。`JSON.parse()`方法用于将JSON字符串解析为JavaScript对象。
                // 3. `let type = message.type;`：这行代码从解析后的消息对象（`message`）中提取`type`属性，并将结果存储在变量`type`中。
                // 4. `console.log("FROM Browser: ", message);`：这行代码将解析后的消息对象（`message`）输出到控制台，并在输出内容前添加"FROM Browser: "字符串。`console.log()`方法用于在控制台中输出信息。
                // 5. `console.log("Iframe:", message.iframe);`：这行代码将解析后的消息对象（`message`）中的`iframe`属性输出到控制台。`console.log()`方法用于在控制台中输出信息。

                if(type.indexOf("Click")>=0){
                    // 鼠标点击事件
                    let iframe = message.iframe;
                    let handles = await driver.getAllWindowHandles();
                    console.log("handles", handles);
                    let exit = false;
                    let content_handle = handle_pairs[message.id];
                    console.log(message.id,  content_handle);
                    let order = [...handles.filter(handle => handle != current_handle && handle != content_handle), current_handle, content_handle]; //搜索顺序
                    let len = order.length;
                    // 这段代码是用JavaScript编写的，主要用于处理浏览器窗口和iframe。以下是代码的详细解释：
                    // 1. 首先，从传入的`message`对象中获取`iframe`属性，赋值给变量`iframe`。
                    // 2. 使用`await`关键字等待`driver.getAllWindowHandles()`方法执行，获取所有窗口的句柄，并将结果赋值给变量`handles`。
                    // 3. 输出`handles`变量，用于调试。
                    // 4. 定义一个变量`exit`，初始值为`false`。
                    // 5. 获取与`message.id`关联的`content_handle`，赋值给变量`content_handle`。
                    // 6. 输出`message.id`和`content_handle`，用于调试。
                    // 7. 创建一个`order`数组，用于存储窗口句柄的搜索顺序。通过`...`运算符将`handles.filter()`的结果转换为数组，然后分别检查当前句柄（`current_handle`）和内容句柄（`content_handle`）是否在数组中，如果不在，则将其添加到`order`数组中。最后，`order`数组将包含一个按指定顺序排列的窗口句柄数组。
                    // 8. 获取`order`数组的长度，赋值给变量`len`。

                    while(true) {
                        try{
                            let h = order[len - 1];
                            console.log("current_handle", current_handle);
                            if(h != null && handles.includes(h)){
                                await driver.switchTo().window(h); //执行失败会抛出异常
                                current_handle = h;
                                console.log("switch to handle: ", h);
                            }
                            // 这段代码是用JavaScript编写的，用于处理浏览器窗口的操作。以下是代码的解释：
                            // 1. 首先，创建一个变量`h`，将其设置为`order[len - 1]`的值。`order`是一个数组，`len`是一个变量，表示数组的长度。`len - 1`表示数组的最后一个元素。
                            // 2. 然后，使用`console.log`输出变量`current_handle`的值。
                            // 3. 接下来，使用`if`语句检查`h`是否不为`null`且`handles`数组包含`h`。如果条件为真，执行以下操作：
                            //   a. 使用`await`关键字等待驱动程序切换到窗口`h`。如果操作失败，将抛出异常。
                            //   b. 将`current_handle`变量设置为`h`。
                            //   c. 使用`console.log`输出“switch to handle：”，然后输出`h`的值。
                            // 总之，这段代码的作用是检查数组的最后一个元素是否有效，如果有效，则切换到相应的浏览器窗口。
                            
                            //下面是找到窗口的情况下
                            if(!iframe){
                                let element = await driver.findElement(By.xpath(message.xpath));
                                await element.click();
                                break;
                            } 
                            // 这段代码是在JavaScript中使用的，用于检查一个名为`iframe`的变量是否为`false`或`undefined`。如果是，则执行以下操作：
                            // 1. 使用`driver.findElement()`方法，通过给定的`xpath`参数查找元素。`message.xpath`是一个包含XPath表达式的变量。
                            // 2. 等待找到的元素被加载，然后执行`await element.click()`，使其被点击。
                            // 3. 跳出循环（`break`）。

                            else {
                                let iframes = await driver.findElements(By.tagName('iframe'));
                                // 遍历所有的 iframe 并点击里面的元素
                                for(let i = 0; i < iframes.length; i++) {
                                    let iframe = iframes[i];
                                    // 切换到 iframe
                                    await driver.switchTo().frame(iframe);
                                    // 在 iframe 中查找并点击元素
                                    let element;
                                    try {
                                        element = await driver.findElement(By.xpath(message.xpath));
                                    } catch (error) {
                                        console.log('No such element found in the iframe');
                                    }
                                    if (element) {
                                        await element.click();
                                    }
                                    // 完成操作后切回主文档
                                    await driver.switchTo().defaultContent();
                                }
                                break;
                            }
                            // 这段代码是在使用Selenium WebDriver进行自动化测试时，处理页面中包含iframe的情况。当页面中包含iframe时，需要先遍历所有的iframe，然后在每一个iframe中查找并点击特定的元素。以下是代码的详细解释：
                            // 1. `else {`：表示当条件语句`if (message.iframe)`不满足时，执行这部分代码。即当页面中不包含iframe时，执行这部分代码。
                            // 2. `let iframes = await driver.findElements(By.tagName('iframe'));`：使用WebDriver的`findElements`方法查找页面中的所有iframe元素，并将结果存储在`iframes`变量中。`By.tagName('iframe')`表示通过元素的标签名查找iframe元素。`await`关键字表示等待异步操作完成。
                            // 3. `for(let i = 0; i < iframes.length; i++) {`：使用for循环遍历`iframes`数组中的所有iframe元素。
                            // 4. `let iframe = iframes[i];`：在循环内部，将当前遍历到的iframe元素存储在`iframe`变量中。
                            // 5. `await driver.switchTo().frame(iframe);`：使用WebDriver的`switchTo`方法切换到当前遍历到的iframe元素。
                            // 6. `let element;`：在循环内部，定义一个变量`element`来存储找到的元素。
                            // 7. `try {`：使用try-catch语句捕获可能发生的异常。
                            // 8. `element = await driver.findElement(By.xpath(message.xpath));`：使用WebDriver的`findElement`方法在当前iframe中查找符合给定XPath表达式的元素，并将结果存储在`element`变量中。`await`关键字表示等待异步操作完成。
                            // 9. `} catch (error) {`：如果查找元素时发生异常，则执行这部分代码。
                            // 10. `console.log('No such element found in the iframe');`：在catch块中，输出一条错误信息，表示在当前iframe中找不到符合条件的元素。
                            // 11. `if (element) {`：如果找到了符合条件的元素，则执行这部分代码。
                            // 12. `await element.click();`：点击找到的元素。`await`关键字表示等待异步操作完成。
                            // 13. `}`：表示if语句的内部结束。
                            // 14. `await driver.switchTo().defaultContent();`：完成操作后，使用WebDriver的`switchTo`方法切换回主文档。
                            // 15. `break;`：跳出循环，表示处理完成。
                        } catch (error) {
                            console.log("len", len); //如果没有找到元素，就切换到下一个窗口
                            len = len - 1;
                            if (len == 0) {
                                break;
                            }
                        }
                        // 这段代码是在JavaScript中捕获一个错误，并在找到元素之前切换到下一个窗口。以下是代码的详细解释：
                        // 1. `catch (error)`：使用`catch`语句捕获一个错误。当程序运行时，如果发生错误，这个代码块将被执行。
                        // 2. `console.log("len", len);`：在控制台中打印`len`的值。如果没有找到元素，就打印`len`的值，表示当前正在尝试的窗口索引。
                        // 3. `len = len - 1;`：将`len`的值减1。这意味着当前窗口的搜索失败，需要尝试下一个窗口。
                        // 4. `if (len == 0) {`：如果`len`的值为0，表示已经尝试了所有窗口，没有找到元素。
                        // 5. `break;`：执行`break`语句，跳出循环，停止搜索。
                        // 这段代码的目的是在找到元素之前切换到下一个窗口，直到找到元素或尝试所有窗口为止。
                    }
                }
            } else {
                socket_window.send(msg.message.pipe);
                for(let i in allWindowSockets){
                    try{
                        allWindowSockets[i].send(msg.message.pipe);
                    } catch {
                        console.log("Cannot send to socket with id: ", allWindowScoketNames[i]);
                    }
                }
                console.log("FROM Flowchart: ", JSON.parse(msg.message.pipe));
                // 这段代码是用JavaScript编写的，主要用于处理WebSocket通信。以下是代码的详细解释：
                // 1. `socket_window.send(msg.message.pipe);`：这行代码将`msg.message.pipe`发送给当前WebSocket连接的窗口（`socket_window`）。`pipe`是一个数据流，用于在WebSocket连接之间传递数据。
                // 2. `for(let i in allWindowSockets){`：这行代码开始一个`for`循环，用于遍历`allWindowSockets`对象中的所有键（即窗口ID）。
                // 3. `try{`：这行代码表示接下来将尝试执行一段代码。如果这段代码执行失败，将跳转到`catch`语句。
                // 4. `allWindowSockets[i].send(msg.message.pipe);`：这行代码将`msg.message.pipe`发送给`allWindowSockets`对象中对应于当前循环索引的窗口ID的WebSocket连接。
                // 5. `} catch {`：这行代码表示`try`语句中的代码执行失败时，将执行`catch`语句中的代码。
                // 6. `console.log("Cannot send to socket with id: ", allWindowScoketNames[i]);`：这行代码在`catch`语句中输出一个错误信息，表示无法向某个窗口的WebSocket发送数据。同时，它会打印出对应窗口的ID。
                // 7. `console.log("FROM Flowchart: ", JSON.parse(msg.message.pipe));`：这行代码在循环结束后输出一个日志信息，表示从流程图接收到的数据。同时，它会将`msg.message.pipe`解析为JSON格式，并打印出来。
            }
        } 
        
        catch (e) {
            console.log(e);
        }
        // 这段代码是一个JavaScript的`try-catch`语句，用于捕获代码块中可能发生的异常。`catch`语句后面跟一个括号，括号中定义了一个变量`e`，用于接收异常对象。
        // 当代码块中的代码发生异常时，`catch`语句将被执行，并将异常对象`e`传递给`console.log()`函数，将其输出到控制台。

    } 
    
    else if (msg.type == 5) {
        let child = require('child_process').execFile;
        // 参数顺序： 1. task id 2. server address 3. saved_file_name 4. "remote" or "local" 5. user_data_folder
        // var parameters = [msg.message.id, server_address];
        let parameters = [];
        console.log(msg.message)
        if (msg.message.user_data_folder == null || msg.message.user_data_folder == undefined || msg.message.user_data_folder == "") {
            parameters = ["--ids", "[" + msg.message.id + "]", "--server_address", server_address, "--user_data", 0];
        } else {
            let user_data_folder_path = path.join(task_server.getDir(), msg.message.user_data_folder);
            parameters = ["--ids", "[" + msg.message.id + "]", "--server_address", server_address, "--user_data", 1];
            config.user_data_folder = msg.message.user_data_folder;
            config.absolute_user_data_folder = user_data_folder_path;
            fs.writeFileSync(path.join(task_server.getDir(), "config.json"), JSON.stringify(config));
        }
        if(msg.message.mysql_config_path != "-1"){
            config.mysql_config_path = msg.message.mysql_config_path;
        }
        fs.writeFileSync(path.join(task_server.getDir(), "config.json"), JSON.stringify(config));
        // child('Chrome/easyspider_executestage.exe', parameters, function(err,stdout, stderr) {
        //    console.log(stdout);
        // });

        let spawn = require("child_process").spawn;
        if (process.platform != "darwin" && msg.message.execute_type == 1 && msg.message.id != -1) {
            let child_process = spawn(execute_path, parameters);
            child_process.stdout.on('data', function (data) {
                console.log(data.toString());
            });
        }
        ws.send(JSON.stringify({"config_folder": task_server.getDir() + "/", "easyspider_location": task_server.getEasySpiderLocation()}));
    } 
    // 这段代码是用JavaScript编写的，主要用于处理任务服务器接收到的消息。主要功能如下：
        // 1. 导入`child_process`模块的`execFile`函数。
        // 2. 定义一个名为`child`的变量，其值为`require('child_process').execFile`。
        // 3. 定义一个名为`parameters`的数组，并将其初始化为空数组。
        // 4. 打印`msg.message`的内容。
        // 5. 判断`msg.message.user_data_folder`是否为空或未定义，如果是，则将参数添加到`parameters`数组中；否则，将用户数据文件夹的路径添加到`parameters`数组中，并更新`config.user_data_folder`和`config.absolute_user_data_folder`，并将`config.json`文件写入任务服务器目录。
        // 6. 判断`msg.message.mysql_config_path`是否不等于`-1`，如果是，则更新`config.mysql_config_path`。
        // 7. 将`config.json`文件写入任务服务器目录。
        // 8. 导入`require("child_process").spawn`函数。
        // 9. 判断平台是否不是macOS且`msg.message.execute_type`为1且`msg.message.id`不等于-1，如果是，则使用`spawn`函数创建一个子进程，并传入执行路径和参数。
        // 10. 监听子进程的输出，并在接收到数据时将其打印到控制台。
        // 11. 发送一个包含任务服务器目录和EasySpider位置的JSON对象给WebSocket。

    else if (msg.type == 6) {
        try{
            flowchart_window.openDevTools();
        } catch {
            console.log("open devtools error");
        }
        try{
            invoke_window.openDevTools();
        } catch {
            console.log("open devtools error");
        }
    } 
    // 这段代码是使用JavaScript编写的，用于尝试打开浏览器的开发者工具。
        // 1. 首先，代码尝试调用`flowchart_window.openDevTools()`函数。如果该函数调用失败，将触发`catch`块中的错误处理程序。
        // 2. `catch`块中的代码打印了一条消息"open devtools error"，表示调用`openDevTools()`函数时发生错误。
        // 3. 然后，代码尝试调用`invoke_window.openDevTools()`函数。如果该函数调用失败，将再次触发`catch`块中的错误处理程序。
        // 4. `catch`块中的代码打印了一条消息"open devtools error"，表示调用`openDevTools()`函数时发生错误。
    
    else if (msg.type == 7) {
        // 获得当前页面Cookies
        try{
            let cookies = await driver.manage().getCookies();
            console.log("Cookies: ", cookies);
            let cookiesText = cookies.map(cookie => `${cookie.name}=${cookie.value}`).join('\n');
            socket_flowchart.send(JSON.stringify({"type": "GetCookies", "message": cookiesText}));
        } catch {
            console.log("Cannot get Cookies");
        }
    }
    // 这段代码是用JavaScript编写的，用于获取浏览器驱动程序的Cookies并将其发送到WebSocket服务器。以下是代码的详细解释：
        // 1. 使用`try`和`catch`语句捕获可能发生的异常。
        // 2. 使用`await`关键字等待浏览器驱动程序获取Cookies，并将结果存储在变量`cookies`中。
        // 3. 调用`console.log`打印Cookies，格式为"Cookies:  [Object]"。
        // 4. 使用`map`和`join`方法将Cookies数组转换为字符串数组，每个字符串的格式为`name=value`。
        // 5. 将转换后的Cookies字符串数组连接成一个字符串，存储在变量`cookiesText`中。
        // 6. 使用`JSON.stringify`方法将`cookiesText`转换为JSON字符串，并将其发送到WebSocket服务器，发送的数据包含一个对象，其中包含两个属性：`type`为"GetCookies"，`message`为`cookiesText`。

}

const WebSocket = require('ws');
const {all} = require("express/lib/application");
let wss = new WebSocket.Server({port: websocket_port});
// 这段代码是用JavaScript编写的，使用了Node.js的WebSocket库和Express库。
// 1. 首先，导入了WebSocket库，它是WebSocket协议的实现，用于在浏览器和服务器之间建立双向通信。
// 2. 然后，导入了express/lib/application模块中的all方法。这个模块应该是一个Express相关的库，但具体的用途和功能还不太清楚。
// 3. 创建了一个名为wss的新WebSocket服务器实例，并将其端口设置为websocket_port（这个变量在代码中没有定义，可能需要根据实际情况进行配置）。
// 总之，这段代码的主要目的是创建一个WebSocket服务器，用于在浏览器和服务器之间建立双向通信。

wss.on('connection', function (ws) {
    ws.on('message', async function (message, isBinary) {
        // 这段代码是用于处理WebSocket消息的JavaScript代码。WebSocket是一种网络通信协议，可以在单个TCP连接上提供全双工通信。在JavaScript中，可以使用WebSocket对象来创建和处理WebSocket连接。
        // 在这段代码中，`ws`是一个WebSocket对象，它代表了与WebSocket服务器之间的连接。`on`方法是WebSocket对象的一个事件处理器，用于注册一个事件处理函数，当WebSocket接收到消息时会触发该函数。
        // `'message'`参数表示要处理的消息类型。在这个例子中，当WebSocket接收到消息时，会触发这个事件。
        // `async`关键字表示这是一个异步函数，意味着在处理消息时，可以执行其他异步操作，例如发送消息到服务器。
        // `function (message, isBinary) {`是事件处理函数的主体，它接受两个参数：`message`和`isBinary`。`message`参数表示接收到的消息，`isBinary`参数是一个布尔值，表示消息是否是二进制格式。
        // 总之，这段代码表示当WebSocket接收到消息时，会触发一个异步函数来处理消息。
        
        let msg = JSON.parse(message.toString());
        console.log("\n\nGET A MESSAGE: ", msg);
        // 这段代码是用JavaScript编写的，用于解析一个名为`message`的变量，并将其转换为JSON格式的数据。
        //     1. `let msg = JSON.parse(message.toString());`：这行代码首先定义了一个名为`msg`的变量，然后使用`JSON.parse()`函数将`message.toString()`转换为JSON格式的数据，并将结果赋值给`msg`。`toString()`函数将对象转换为字符串，以便可以解析为JSON格式。
        //     2. `console.log("\n\nGET A MESSAGE: ", msg);`：这行代码使用`console.log()`函数将`msg`的值输出到控制台，并在输出值之前添加一些额外的文本。`\n\n`表示换行符，用于在输出值之间添加空白行。

        // console.log(msg, msg.type, msg.message);
        if (msg.type == 0) {
            if (msg.message.id == 0) {
                socket_window = ws;
                console.log("set socket_window")
            } else if (msg.message.id == 1) {
                socket_start = ws;
                console.log("set socket_start")
            } else if (msg.message.id == 2) {
                socket_flowchart = ws;
                console.log("set socket_flowchart");
            } else { //其他的ID是用来标识不同的浏览器标签页的
                await new Promise(resolve => setTimeout(resolve, 2300));
                let handles = await driver.getAllWindowHandles();
                if(arrayDifference(handles, old_handles).length > 0){
                    old_handles = handles;
                    current_handle = handles[handles.length - 1];
                    console.log("New tab opened, change current_handle to: ", current_handle);
                }
                handle_pairs[msg.message.id] = current_handle;
                console.log("Set handle_pair for id: ", msg.message.id, " to ", current_handle, ", title is: ", msg.message.title);
                socket_flowchart.send(JSON.stringify({"type": "title", "data": {"title":msg.message.title}}));
                allWindowSockets.push(ws);
                allWindowScoketNames.push(msg.message.id);
                // console.log("handle_pairs: ", handle_pairs);
            }
        }
        // 这段代码是用JavaScript编写的，主要用于处理WebSocket消息。当收到消息时，它会根据消息的类型和内容执行不同的操作。以下是代码的详细解释：
        // 1. 首先，它检查消息的类型是否为0。如果是，则继续执行以下操作。
        // 2. 然后，它检查消息中包含的ID是否为0。如果是，则将WebSocket对象赋值给`socket_window`变量，并输出一条日志。
        // 3. 接下来，它检查消息中包含的ID是否为1。如果是，则将WebSocket对象赋值给`socket_start`变量，并输出一条日志。
        // 4. 然后，它检查消息中包含的ID是否为2。如果是，则将WebSocket对象赋值给`socket_flowchart`变量，并输出一条日志。
        // 5. 如果没有匹配的消息类型或ID，它会等待2.3秒，然后获取浏览器窗口的句柄数组`handles`。
        // 6. 接下来，它检查`handles`与之前的句柄数组`old_handles`之间的差异。如果差异长度大于0，则更新`old_handles`，并将当前句柄设置为`handles`的最后一个元素。
        // 7. 然后，它将新的句柄存储在`handle_pairs`对象中，并输出一条日志，其中包含消息的ID和当前句柄。
        // 8. 最后，它将消息发送给`socket_flowchart`，并将其添加到`allWindowSockets`和`allWindowScoketNames`数组中。
        
        else if (msg.type == 10) {
            let leave_handle = handle_pairs[msg.message.id];
            if (leave_handle!=null && leave_handle!=undefined && leave_handle!="")
            {
                await driver.switchTo().window(leave_handle);
                console.log("Switch to handle: ", leave_handle);
                current_handle = leave_handle;
            }
        }
        // 这段代码是在处理一个消息（msg），根据消息的类型进行不同的处理。如果消息类型为10，那么它会执行以下操作：
        // 1. 从`handle_pairs`对象中获取与消息ID关联的窗口句柄（leave_handle）。
        // 2. 检查`leave_handle`是否为`null`、`undefined`或空字符串。如果是，则执行以下操作：
        //     1. 使用`driver.switchTo().window(leave_handle)`将浏览器切换到指定的窗口句柄。
        //     2. 输出一条日志，显示切换到的窗口句柄。
        //     3. 将当前窗口句柄（current_handle）更新为`leave_handle`。
        
        else {
            await beginInvoke(msg, ws);
        }
        // 这段代码是 JavaScript 中的一个异步操作，用于处理 WebSocket 连接的逻辑。当 WebSocket 连接成功时，会执行 await beginInvoke(msg, ws) 函数，而当连接失败时，则会执行 else 语句中的代码。
        
    });
});

console.log(process.platform);

async function runBrowser(lang = "en", user_data_folder = '', mobile = false) {
    // 这是一个使用JavaScript编写的异步函数，名为`runBrowser`。这个函数接受三个参数：`lang`（默认值为"en"）、`user_data_folder`（默认值为空字符串）和`mobile`（默认值为`false`）。
    // 这个函数的主要目的是在浏览器中运行一个程序。它可能涉及到使用指定的语言（`lang`参数）和用户数据文件夹（`user_data_folder`参数）来运行该程序。此外，它还可以根据需要是否为移动端（`mobile`参数）运行该程序。
    
    const serviceBuilder = new ServiceBuilder(driverPath);
    let options = new chrome.Options();
    options.addArguments('--disable-blink-features=AutomationControlled');
    language = lang;
    // 这段代码的主要功能是创建一个ServiceBuilder对象，用于构建Chrome浏览器实例，并设置一些选项，如禁用blinkfeatures和语言。
    // 1. 首先，创建一个ServiceBuilder对象，传入参数driverPath，这个参数可能是Chrome浏览器的驱动程序路径。
    // 2. 创建一个chrome.Options对象，用于设置浏览器的选项。
    // 3. 使用addArguments方法添加一个参数'--disable-blink-features=AutomationControlled'，这个参数用于禁用一些blinkfeatures，以防止自动化控制被滥用。
    // 4. 设置语言（language）变量为传入的参数lang。

    if (lang == "en") {
        options.addExtensions(path.join(__dirname, "EasySpider_en.crx"));
    } else if (lang == "zh") {
        options.addExtensions(path.join(__dirname, "EasySpider_zh.crx"));
    }
    // 这段代码是用JavaScript编写的，用于根据传入的参数`lang`来决定加载哪个扩展
    // 1. 首先，使用`if`语句检查传入的参数`lang`是否等于"en"。如果是，则执行下面的代码块。
    // 2. 使用`options.addExtensions()`方法，将`path.join(__dirname, "EasySpider_en.crx")`路径添加到扩展中。这里的`__dirname`是一个内置的JavaScript变量，表示当前脚本所在的目录。`path.join()`方法用于将多个路径组合成一个绝对路径。
    // 3. 如果`lang`不等于"en"，将执行`else if`语句。再次检查传入的参数`lang`是否等于"zh"。如果是，则执行下面的代码块。
    // 4. 使用`options.addExtensions()`方法，将`path.join(__dirname, "EasySpider_zh.crx")`路径添加到扩展中。这里的`__dirname`是一个内置的JavaScript变量，表示当前脚本所在的目录。`path.join()`方法用于将多个路径组合成一个绝对路径。
    // 总之，这段代码的作用是根据传入的参数`lang`来加载不同的扩展。如果`lang`等于"en"，则加载`EasySpider_en.crx`扩展；如果`lang`等于"zh"，则加载`EasySpider_zh.crx`扩展。

    options.addExtensions(path.join(__dirname, "XPathHelper.crx"));
    options.setChromeBinaryPath(chromeBinaryPath);
    // 这段代码是用JavaScript编写的，用于设置Chrome浏览器的一些选项，以便在浏览器中使用XPathHelper.crx扩展。以下是代码的详细解释：
    // 1. `options.addExtensions(path.join(__dirname, "XPathHelper.crx"));`：这行代码将XPathHelper.crx扩展添加到Chrome浏览器的扩展选项中。`options.addExtensions()`方法用于添加扩展，`path.join(__dirname, "XPathHelper.crx")`用于构建扩展文件的路径，`__dirname`是当前目录的路径，`XPathHelper.crx`是扩展文件名。
    // 2. `options.setChromeBinaryPath(chromeBinaryPath);`：这行代码设置了Chrome浏览器的二进制路径。`options.setChromeBinaryPath()`方法用于设置二进制路径，`chromeBinaryPath`是Chrome浏览器的二进制路径。

    if (user_data_folder != "") {
        let dir = path.join(task_server.getDir(), user_data_folder);
        console.log(dir);
        options.addArguments("--user-data-dir=" + dir);
        config.user_data_folder = user_data_folder;
        fs.writeFileSync(path.join(task_server.getDir(), "config.json"), JSON.stringify(config));
    }
    // 这段代码是在JavaScript中执行的，主要用于设置用户数据文件夹的路径，并将该路径添加到Chrome浏览器的启动参数中。以下是代码的详细解释：
    // 1. 首先，代码检查`user_data_folder`是否为空字符串。如果不为空，则继续执行以下操作。
    // 2. 使用`path.join()`函数将`task_server.getDir()`和`user_data_folder`连接在一起，以创建用户数据文件夹的完整路径。
    // 3. 使用`console.log()`函数输出创建的用户数据文件夹路径。
    // 4. 使用`options.addArguments()`函数将用户数据文件夹路径添加到Chrome浏览器的启动参数中。Chrome浏览器会自动将`--user-data-dir`参数传递给Chrome应用程序，以便在指定的目录中存储用户数据。
    // 5. 使用`config.user_data_folder`变量存储用户数据文件夹的路径。
    // 6. 使用`fs.writeFileSync()`函数将`config.json`文件写入`task_server.getDir()`目录，并将`config`对象转换为JSON字符串格式。

    if (mobile) {
        const mobileEmulation = {
            deviceName: 'iPhone XR'
        };
        options.addArguments(`--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"`);
        options.setMobileEmulation(mobileEmulation);
    }
    // 这段代码是在JavaScript中判断是否为移动端（mobile）环境，如果是移动端环境，则进行以下操作：
    // 1. 创建一个名为`mobileEmulation`的对象，其中包含一个属性`deviceName`，其值为`iPhone XR`。
    // 2. 向`options`对象中添加一个参数，用于设置User-Agent头，模拟移动端设备。
    // 3. 调用`options.setMobileEmulation(mobileEmulation)`，将创建的`mobileEmulation`对象设置为移动端设备模拟设置。

    driver = new Builder()
        .forBrowser('chrome')
        .setChromeOptions(options)
        .setChromeService(serviceBuilder)
        .build();
    await driver.manage().setTimeouts({implicit: 10000, pageLoad: 10000, script: 10000});
    await driver.executeScript("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})");
    // await driver.executeScript("localStorage.clear();"); //重置参数数量
    // 这段代码是用JavaScript编写的，用于设置和配置一个WebDriver驱动程序，以便与Chrome浏览器进行交互。以下是代码的详细解释：
    // 1. `driver = new Builder()`：创建一个新的Builder对象，用于配置WebDriver驱动程序。
    // 2. `.forBrowser('chrome')`：指定要使用的浏览器类型为Chrome。
    // 3. `.setChromeOptions(options)`：设置Chrome选项，包括禁用扩展程序、设置用户代理等。
    // 4. `.setChromeService(serviceBuilder)`：设置Chrome服务，用于在后台运行浏览器实例。
    // 5. `.build()`：根据配置创建并返回一个新的WebDriver驱动程序实例。
    // 6. `await driver.manage().setTimeouts({implicit: 10000, pageLoad: 10000, script: 10000});`：设置驱动程序的超时设置，包括隐式等待、页面加载等待和脚本等待。
    // 7. `await driver.executeScript("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})");`：向浏览器插入一个JavaScript代码，将`navigator.webdriver`属性设置为`undefined`。这可以防止浏览器检测到自动化测试工具。
    // 8. `// await driver.executeScript("localStorage.clear();"); //重置参数数量`：这行代码被注释掉了，因为它可能会重置一些测试参数。在实际使用中，可以根据需要决定是否执行这个操作。

    const cdpConnection = await driver.createCDPConnection("page");
    let stealth_path = path.join(__dirname, "stealth.min.js");
    let stealth = fs.readFileSync(stealth_path, 'utf8');
    await cdpConnection.execute('Page.addScriptToEvaluateOnNewDocument', {
        source: stealth,
    });
    // 这段代码的主要功能是创建一个CDP连接，并在新的页面加载时注入一个名为stealth.min.js的脚本。以下是代码的详细解释：
    // 1. `const cdpConnection = await driver.createCDPConnection("page");`：这行代码创建了一个新的CDP连接，并将其与页面对象关联。CDP（Chrome DevTools Protocol）是Chrome浏览器提供的一组API，用于与浏览器进行交互。`createCDPConnection`方法用于创建一个新的CDP连接，参数"page"表示连接将用于与页面对话。
    // 2. `let stealth_path = path.join(__dirname, "stealth.min.js");`：这行代码定义了一个变量`stealth_path`，它是一个包含stealth.min.js文件路径的字符串。`path.join`方法用于将两个路径字符串连接在一起，`__dirname`是一个内置的变量，表示当前脚本所在的目录。
    // 3. `let stealth = fs.readFileSync(stealth_path, 'utf8');`：这行代码使用`fs.readFileSync`方法读取`stealth_path`指向的文件内容，并将其存储在变量`stealth`中。`fs.readFileSync`是一个同步的文件读取方法，用于在Node.js中读取文件内容。
    // 4. `await cdpConnection.execute('Page.addScriptToEvaluateOnNewDocument', { source: stealth });`：这行代码向浏览器发送一个CDP命令，将`stealth`变量中的脚本添加到新的页面加载时执行的脚本列表中。`Page.addScriptToEvaluateOnNewDocument`命令表示将脚本添加到页面的`evaluateOnNewDocument`属性中，该属性表示在页面加载时执行的脚本。

    try {
        if(mobile){
            await driver.get(server_address + "/taskGrid/taskList.html?wsport=" + websocket_port + "&backEndAddressServiceWrapper=" + server_address + "&mobile=1&lang=" + lang);
        } else {
            await driver.get(server_address + "/taskGrid/taskList.html?wsport=" + websocket_port + "&backEndAddressServiceWrapper=" + server_address + "&lang=" + lang);
        }

        old_handles = await driver.getAllWindowHandles();
        current_handle = old_handles[old_handles.length - 1];
    } finally {
        // await driver.quit(); // 退出浏览器
    }
    // 这段代码是用JavaScript编写的，用于在尝试执行某些操作时捕获异常。它主要包含以下几个部分：
    // 1. `try`块：在这里定义了可能抛出异常的操作。
    // 2. `if(mobile)`：这是一个条件语句，如果`mobile`变量为`true`，则执行以下操作。
    // 3. `await driver.get(...)`：使用`await`关键字等待驱动程序执行`get`方法，即打开一个网页。它将服务器地址、WebSocket端口、后端服务地址、是否为移动端以及语言等信息添加到URL中。
    // 4. `old_handles = await driver.getAllWindowHandles();`：使用`await`关键字等待驱动程序执行`getAllWindowHandles`方法，获取当前浏览器中所有窗口的句柄。
    // 5. `current_handle = old_handles[old_handles.length - 1];`：从所有窗口句柄中选择最后一个，作为当前窗口的句柄。
    // 6. `finally`块：这是一个可选的块，用于在完成`try`块中的操作后执行的代码。在这里，没有执行任何操作，只是等待驱动程序退出。
    // 总之，这段代码的主要目的是在尝试打开一个网页时捕获异常，并在打开网页后获取当前窗口的句柄。

}

function handleOpenBrowser(event, lang = "en", user_data_folder = "", mobile = false) {
    // 这段代码定义了一个名为`handleOpenBrowser`的函数，它接受四个参数：`event`、`lang`、`user_data_folder`和`mobile`。函数的目的是处理浏览器打开的事件，并提供一些可选参数来设置语言、用户数据文件夹和是否为移动设备。
    //     1. `event`：这是一个事件对象，表示浏览器打开的原因。这可能包括用户点击打开按钮、通过URL打开页面等。
    //     2. `lang`：这是一个可选参数，默认为"en"（英语）。它表示用户希望使用的语言。
    //     3. `user_data_folder`：这也是一个可选参数，默认为空字符串。它表示用户数据文件夹的路径。
    //     4. `mobile`：这也是一个可选参数，默认为`false`。它表示当前设备是否为移动设备。
    
    const webContents = event.sender;
    const win = BrowserWindow.fromWebContents(webContents);
    runBrowser(lang, user_data_folder, mobile);
    let size = screen.getPrimaryDisplay().workAreaSize;
    let width = parseInt(size.width);
    let height = parseInt(size.height * 0.6);
    flowchart_window = new BrowserWindow({
        x: 0,
        y: 0,
        width: width,
        height: height,
        icon: iconPath,
    });
    let url = "";
    let id = -1;
    // 这段代码是用JavaScript编写的，主要用于创建一个新的浏览器窗口，并在其中打开一个流程图。以下是代码的详细解释：
    // 1. 首先，从事件对象中获取发送者（webContents），然后将其转换为BrowserWindow对象。
    // 2. 调用一个名为runBrowser的函数，该函数接受三个参数：lang（语言），user_data_folder（用户数据文件夹）和mobile（是否为移动端）。
    // 3. 获取屏幕上的主要显示器的工作区域大小，并将其存储在width和height变量中。
    // 4. 创建一个新的BrowserWindow对象，设置其位置（x=0, y=0）、宽度和高度（宽度和高度分别乘以0.6），并设置图标。
    // 5. 初始化url和id变量。
    // 总之，这段代码创建了一个新的浏览器窗口，并在其中打开了一个流程图。

    if (lang == "en") {
        url = server_address + `/taskGrid/FlowChart.html?id=${id}&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address + "&mobile=" + mobile.toString();
    } else if (lang == "zh") {
        url = server_address + `/taskGrid/FlowChart_CN.html?id=${id}&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address+ "&mobile=" + mobile.toString();
    }
    // and load the index.html of the app.
    flowchart_window.loadURL(url, { extraHeaders: 'pragma: no-cache\n' });
    if(process.platform != "darwin"){
        flowchart_window.hide();
    }
    flowchart_window.on('close', function (event) {
        mainWindow.show();
        driver.quit();
    });
    // 这段代码是用JavaScript编写的，主要用于设置和加载一个FlowChart窗口的URL。以下是代码的详细解释：
    // 1. 首先，代码通过比较`lang`变量的值来确定要加载的URL。如果`lang`等于"en"，那么将URL设置为包含英文版本的FlowChart.html文件。如果`lang`等于"zh"，则将URL设置为包含中文版本的FlowChart_CN.html文件。
    // 2. 然后，使用`server_address`、`id`、`websocket_port`和`mobile`变量来构建URL的动态部分。
    // 3. 接下来，使用`flowchart_window`对象加载构建好的URL。同时，通过传递`extraHeaders`选项来告诉浏览器不要缓存页面。
    // 4. 如果当前系统不是macOS，那么将隐藏FlowChart窗口。
    // 5. 最后，为`flowchart_window`对象的`close`事件添加一个事件处理程序。当FlowChart窗口被关闭时，将显示主窗口（`mainWindow`），并关闭与WebDriver的连接（`driver.quit()`）。

}

function handleOpenInvoke(event, lang = "en") {
    // 这段代码定义了一个名为`handleOpenInvoke`的函数，该函数接受两个参数：`event`和`lang`。`event`参数是事件对象，用于处理打开调用事件；`lang`参数是可选的，默认为"en"，表示语言设置。

    invoke_window = new BrowserWindow({icon: iconPath});
    let url = "";
    language = lang;
    if (lang == "en") {
        url = server_address + `/taskGrid/taskList.html?type=1&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address;
    } else if (lang == "zh") {
        url = server_address + `/taskGrid/taskList.html?type=1&wsport=${websocket_port}&backEndAddressServiceWrapper=` + server_address + "&lang=zh";
    }
    // 这段代码是用JavaScript编写的，用于创建一个新的浏览器窗口并设置其图标。同时，它还定义了一个变量`url`，并根据语言环境（`lang`）设置不同的URL。
    // 1. 首先，创建一个新的浏览器窗口，名为`invoke_window`，并设置其图标为`iconPath`。
    // 2. 定义一个空字符串变量`url`，用于存储URL。
    // 3. 定义一个变量`language`，值为`lang`。
    // 4. 如果`language`等于"en"，则将服务器地址（`server_address`）和WebSocket端口（`websocket_port`）拼接到URL中。同时，添加一个`backEndAddressServiceWrapper`参数，其值为服务器地址。
    // 5. 如果`language`等于"zh"，则将服务器地址（`server_address`）和WebSocket端口（`websocket_port`）拼接到URL中。此外，还需要添加一个名为`lang`的参数，其值为"zh"。

    // and load the index.html of the app.
    invoke_window.loadURL(url, { extraHeaders: 'pragma: no-cache\n' });
    invoke_window.maximize();
    mainWindow.hide();
    invoke_window.on('close', function (event) {
        mainWindow.show();
    });
    // 这段代码是用JavaScript编写的，用于控制一个名为`invoke_window`的窗口的显示和关闭。以下是代码的逐行解释：
    // 1. `invoke_window.loadURL(url, { extraHeaders: 'pragma: no-cache\n' });`：加载指定的URL，并将额外的头部信息设置为`pragma: no-cache\n`。这通常用于防止浏览器缓存页面，从而实现实时的数据更新。
    // 2. `invoke_window.maximize();`：最大化`invoke_window`窗口。
    // 3. `mainWindow.hide();`：隐藏名为`mainWindow`的主窗口。
    // 4. `invoke_window.on('close', function (event) {`：为`invoke_window`窗口添加一个关闭事件监听器。当窗口被关闭时，会执行后面的函数。
    // 5. `mainWindow.show();`：当`invoke_window`窗口被关闭时，显示名为`mainWindow`的主窗口。
    // 总之，这段代码的作用是隐藏主窗口，加载指定的URL，最大化`invoke_window`窗口，并在`invoke_window`窗口被关闭时显示主窗口。

}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
    session.defaultSession.webRequest.onBeforeSendHeaders((details, callback) => {
        details.requestHeaders['Accept-Language'] = 'zh'
        callback({ cancel: false, requestHeaders: details.requestHeaders })
    })
    // 这段代码是用JavaScript编写的，用于设置浏览器请求头中的语言设置。
    // 1. `session.defaultSession.webRequest.onBeforeSendHeaders((details, callback) => { ... })`：这是JavaScript中的事件监听器，当浏览器发起请求时，会触发这个函数。事件监听器接受两个参数：`details`和`callback`。其中，`details`对象包含了请求的详细信息，例如请求的URL、请求方法、请求头等；`callback`是一个回调函数，当请求处理完成后，会调用这个函数，并将处理结果作为参数传递给回调函数。
    // 2. `details.requestHeaders['Accept-Language'] = 'zh'`：这行代码将请求头中的`Accept-Language`设置为`zh`。这意味着浏览器将优先使用中文作为语言。
    // 3. `callback({ cancel: false, requestHeaders: details.requestHeaders })`：这行代码是调用回调函数的代码。回调函数的参数是一个对象，其中包含两个键值对：`cancel`和`requestHeaders`。`cancel`的值为`false`，表示请求不会被取消；`requestHeaders`的值是`details.requestHeaders`，即请求头对象。这样，回调函数会将修改后的请求头传递给浏览器，以便浏览器在发送请求时使用新的请求头。

    ipcMain.on('start-design', handleOpenBrowser);
    ipcMain.on('start-invoke', handleOpenInvoke);
    ipcMain.on('accept-agreement', function (event, arg) {
        config.copyright = 1;
        fs.writeFileSync(path.join(task_server.getDir(), "config.json"), JSON.stringify(config));
    });
    createWindow();
    // 这段代码是用JavaScript编写的，用于处理来自主进程（main process）的事件。以下是代码的逐行解释：
    //     1. `ipcMain.on('start-design', handleOpenBrowser);`：当主进程发送“start-design”事件时，调用`handleOpenBrowser`函数处理该事件。
    //     2. `ipcMain.on('start-invoke', handleOpenInvoke);`：当主进程发送“start-invoke”事件时，调用`handleOpenInvoke`函数处理该事件。
    //     3. `ipcMain.on('accept-agreement', function (event, arg) {`：当主进程发送“accept-agreement”事件时，执行以下操作：
    //     a. `config.copyright = 1;`：将`config`对象的`copyright`属性设置为1。
    //     b. `fs.writeFileSync(path.join(task_server.getDir(), "config.json"), JSON.stringify(config));`：将`config`对象的字符串表示形式写入`config.json`文件。`path.join`函数用于将`task_server.getDir()`和文件名连接在一起，`fs.writeFileSync`函数用于将文件写入磁盘。
    //     4. `createWindow();`：创建一个窗口。

    app.on('activate', function () {
        // On macOS it's common to re-create a window in the app when the
        // dock icon is clicked and there are no other windows open.
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    })
    // 这段代码是用于处理应用程序在macOS操作系统下的窗口创建和激活事件。以下是代码的详细解释：
    // 1. `app.on('activate', function () { ... });`：这是JavaScript的语法，表示在应用程序的`activate`事件触发时，执行后面的代码块。`app`是一个应用程序对象，它是使用`require('electron')`模块创建的。`activate`事件在用户单击 dock 图标时触发，或在应用程序的其他窗口关闭时触发。
    // 2. `if (BrowserWindow.getAllWindows().length === 0) { ... }`：这是一个条件语句，用于检查应用程序当前是否没有打开的窗口。`BrowserWindow.getAllWindows()`是一个方法，它返回应用程序当前打开的所有窗口的数组。如果数组的长度为0，表示当前没有打开的窗口。
    // 3. `if (BrowserWindow.getAllWindows().length === 0) { ... }`：如果应用程序当前没有打开的窗口，那么执行`createWindow()`函数，用于创建一个新的窗口。`createWindow()`是一个应用程序中的函数，用于创建一个新的浏览器窗口。
    // 总之，这段代码的作用是在macOS操作系统下，当应用程序的 dock 图标被单击时，如果当前没有打开任何窗口，那么就创建一个新的窗口。

})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit();
    }
})
// 这段代码是用于处理应用程序在所有窗口都关闭时的行为。当用户在非macOS平台上（例如Windows或Linux）的浏览器中关闭所有窗口时，应用程序将退出。
// 1. `app.on('window-all-closed', function () { ... });`：这是使用`app`对象的`on`方法监听一个事件。当所有窗口都关闭时，将触发`window-all-closed`事件。
// 2. `if (process.platform !== 'darwin') { ... }`：这是一个条件语句，用于检查当前运行平台是否为macOS。如果不是，则执行`app.quit()`方法以退出应用程序。
// 3. `app.quit();`：这是调用`app`对象的`quit`方法以退出应用程序。

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.

function arrayDifference(arr1, arr2) {
    return arr1.filter(item => !arr2.includes(item));
}
// 这段代码定义了一个名为`arrayDifference`的函数，它接受两个参数`arr1`和`arr2`，并返回一个新的数组，其中包含了`arr1`中所有不在`arr2`中的元素。
// 具体来说，函数首先使用`filter`方法遍历`arr1`中的每个元素`item`，然后使用`includes`方法检查`arr2`中是否包含`item`。如果`arr2`中不包含`item`，那么`filter`方法会保留这个元素，否则会将其从结果数组中移除。最后，`filter`方法返回一个新的数组，其中包含了`arr1`中所有不在`arr2`中的元素。