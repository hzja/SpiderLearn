const http = require('http');
const querystring = require('querystring');
const url = require('url');
const fs = require('fs');
const path=require('path');
const {app, dialog} = require('electron');
const XLSX = require('xlsx');
const formidable = require('formidable');
const express = require('express');
const multer  = require('multer');
const cors = require('cors');
// 这段代码是用JavaScript编写的，用于导入所需的模块和库。以下是每个模块的功能解释：
// 1. `http`：提供与HTTP相关的功能，如创建HTTP服务器、发起HTTP请求等。
// 2. `querystring`：提供用于解析和处理URL查询字符串的函数。
// 3. `url`：提供URL处理相关的功能，如解析URL、构建URL等。
// 4. `fs`：提供与文件系统相关的功能，如读取、写入文件等。
// 5. `path`：提供处理文件路径相关的功能。
// 6. `{app, dialog}`：导入Electron应用程序的`app`和`dialog`对象。
// 7. `XLSX`：提供处理Excel文件的相关功能，如读取、写入Excel文件等。
// 8. `formidable`：提供处理HTTP请求中的文件上传功能。
// 9. `express`：提供创建和配置Express应用程序的功能。
// 10. `multer`：提供处理文件上传的辅助库。
// 11. `cors`：提供处理跨域资源共享（CORS）的功能。

function travel(dir,callback){
    fs.readdirSync(dir).forEach((file)=>{
        const pathname=path.join(dir,file)
        if(fs.statSync(pathname).isDirectory()){
            travel(pathname,callback)
        }else{
            callback(pathname)
        }
    })
}
// 这段代码定义了一个名为`travel`的函数，它接受两个参数：`dir`（用于遍历的目录）和`callback`（用于处理每个文件的回调函数）。
// 函数内部首先使用`fs.readdirSync(dir)`读取目录中的所有文件，然后使用`forEach`遍历每个文件。对于每个文件，它会将文件路径连接到目录路径，然后使用`fs.statSync(pathname)`检查文件是否为目录。如果是目录，则递归调用`travel`函数，传入相同的`dir`和`callback`参数；否则，将文件路径作为参数传入`callback`函数。
// 总之，这段代码定义了一个递归函数，用于遍历目录及其子目录中的所有文件，并将每个文件传递给指定的回调函数进行处理。

function compare(p){ //这是比较函数
    return function(m,n){
        let a = m[p];
        let b = n[p];
        return b - a; //降序
    }
}
// 这段代码定义了一个名为`compare`的函数，它接受一个参数`p`。`compare`函数返回一个新的函数，这个新函数接受两个参数`m`和`n`。
// 在新函数内部，我们分别获取`m`和`n`对象中属性值为`p`的值，并将它们存储在变量`a`和`b`中。然后，我们使用`b - a`来计算它们的差值，这将产生一个降序排序的结果。
// 最后，我们将计算差值的函数作为返回值，以便在排序时使用。

function getDir(){
    if(__dirname.indexOf("app") >= 0 && __dirname.indexOf("sources") >= 0){
        if(process.platform == "darwin"){
            return app.getPath("userData");
        } else {
            return path.join(__dirname,"../../..");
        }
    } else {
        return __dirname;
    }
}
// 这段代码定义了一个名为`getDir`的函数，用于获取当前目录的路径。以下是代码的逐行解释：
// 1. `function getDir(){}`：定义一个名为`getDir`的函数，没有参数，没有返回值。
// 2. `if(__dirname.indexOf("app") >= 0 && __dirname.indexOf("sources") >= 0){`：判断`__dirname`（当前目录的路径）是否包含"app"和"sources"字符串。如果满足条件，则继续执行下面的代码，否则跳过接下来的代码块。
// 3. `if(process.platform == "darwin"){`：判断当前操作系统是否为macOS。如果是，则继续执行下面的代码，否则跳过接下来的代码块。
// 4. `return app.getPath("userData");`：如果当前操作系统为macOS，则返回`app.getPath("userData")`，即用户数据目录的路径。
// 5. `} else {`：否则，如果是其他操作系统，则执行下面的代码。
// 6. `return path.join(__dirname,"../../..");`：如果是其他操作系统，则返回`path.join(__dirname,"../../..")`，即当前目录的父目录的父目录的路径。
// 7. `}`：结束`else`代码块。
// 8. `}`：结束`if`条件判断。
// 9. `return __dirname;`：如果`__dirname`不包含"app"和"sources"字符串，则返回`__dirname`，即当前目录的路径。
// 10. `}`：结束`getDir`函数。

function getEasySpiderLocation(){
    if(__dirname.indexOf("app") >= 0 && __dirname.indexOf("sources") >= 0){
        if(process.platform == "darwin"){
            return path.join(__dirname,"../../../");
        } else {
            return path.join(__dirname,"../../../");
        }
    } else {
        return __dirname;
    }
}
// 这段代码定义了一个名为`getEasySpiderLocation`的函数，用于获取一个名为`easySpider`的爬虫项目的位置。
// 1. 首先，使用`__dirname`变量获取当前函数所在的文件夹路径。
// 2. 然后，使用`indexOf`方法检查`__dirname`是否包含"app"和"sources"这两个子字符串。如果是，则执行以下操作：
//   a. 如果系统平台是"darwin"（macOS），则使用`path.join`方法将`__dirname`的父目录（即`../../../`）连接到返回值中。
//   b. 如果系统平台不是"darwin"，则也使用`path.join`方法将`__dirname`的父目录（即`../../../`）连接到返回值中。
// 3. 否则，直接返回当前函数所在的文件夹路径。
// 总之，这段代码的主要作用是获取`easySpider`项目在文件系统中的位置，以便在其他地方引用该项目的文件。

if(!fs.existsSync(path.join(getDir(), "tasks"))){
    fs.mkdirSync(path.join(getDir(), "tasks"));
}
if(!fs.existsSync(path.join(getDir(), "execution_instances"))){
    fs.mkdirSync(path.join(getDir(), "execution_instances"));
}
if(!fs.existsSync(path.join(getDir(), "config.json"))){
    // Generate config.json
    fs.writeFileSync(path.join(getDir(), "config.json"),
        JSON.stringify({
                "webserver_address": "http://localhost",
                "webserver_port": 8074,
                "user_data_folder": "./user_data",
                "debug": false,
                "copyright": 0,
                "sys_arch": require('os').arch(),
                "mysql_config_path": "./mysql_config.json",
                "absolute_user_data_folder": "D:\\Document\\Projects\\EasySpider\\ElectronJS\\user_data"
            }
        ));
}
// 这段代码是用JavaScript编写的，主要用于检查和创建一些目录和文件。以下是代码的详细解释：
// 1. 首先，使用`fs.existsSync()`方法检查`tasks`目录是否存在。如果不存在，则使用`fs.mkdirSync()`方法创建该目录。
// 2. 然后，使用`fs.existsSync()`方法检查`execution_instances`目录是否存在。如果不存在，则使用`fs.mkdirSync()`方法创建该目录。
// 3. 最后，使用`fs.existsSync()`方法检查`config.json`文件是否存在。如果不存在，则执行以下操作：
//   a. 生成`config.json`文件，将其内容设置为以下内容：
//      - "webserver_address": "http://localhost"
//      - "webserver_port": 8074
//      - "user_data_folder": "./user_data"
//      - "debug": false
//      - "copyright": 0
//      - "sys_arch": 系统架构（如 "x64" 或 "arm64" 等）
//      - "mysql_config_path": "./mysql_config.json"
//      - "absolute_user_data_folder": "D:\\Document\\Projects\\EasySpider\\ElectronJS\\user_data"
//   b. 使用`fs.writeFileSync()`方法将生成的`config.json`文件写入到`path.join(getDir(), "config.json")`路径下。

exports.getDir = getDir;
exports.getEasySpiderLocation = getEasySpiderLocation;
FileMimes = JSON.parse(fs.readFileSync(path.join(__dirname,'mime.json')).toString());
// 这段代码是用JavaScript编写的，用于导出两个函数和一个对象。以下是代码的逐行解释：
// 1. `exports.getDir = getDir;`：将名为`getDir`的函数导出，并将其作为`exports.getDir`。这意味着其他模块可以通过`require('./yourfile')`来导入`getDir`函数。
// 2. `exports.getEasySpiderLocation = getEasySpiderLocation;`：将名为`getEasySpiderLocation`的函数导出，并将其作为`exports.getEasySpiderLocation`。
// 3. `FileMimes = JSON.parse(fs.readFileSync(path.join(__dirname,'mime.json')).toString());`：从名为`mime.json`的文件中读取内容，将其转换为字符串，然后使用`JSON.parse()`将其解析为对象。最后，将解析后的对象赋值给名为`FileMimes`的变量。`path.join(__dirname,'mime.json')`用于构建文件的绝对路径。`__dirname`是一个内置变量，表示当前模块的目录。

const fileServer = express();
const upload = multer({ dest: path.join(getDir(), 'Data/') });
// 这段代码是用JavaScript编写的，用于设置一个文件服务器并配置文件上传功能。以下是代码的详细解释：
// 1. `const fileServer = express();`：这行代码创建了一个名为`fileServer`的Express应用程序实例。Express是一个流行的JavaScript Web框架，用于构建Web应用程序和API。
// 2. `const upload = multer({ dest: path.join(getDir(), 'Data/') });`：这行代码使用Multer库配置文件上传功能。Multer是一个处理文件上传的JavaScript中间件，通常与Express一起使用。在这里，它被配置为将上传的文件存储在`path.join(getDir(), 'Data/')`目录下。`getDir()`是一个未定义的函数，可能用于获取项目的根目录。
// 总之，这段代码设置了文件服务器并配置了文件上传功能，使得用户可以通过Express应用程序上传文件到指定的目录下。

fileServer.use(cors());
fileServer.post('/excelUpload', upload.single('file'), (req, res) => {
    let workbook = XLSX.readFile(req.file.path);
    let sheet_name_list = workbook.SheetNames;
    let data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]]);
    let result = data.reduce((acc, obj) => {
        Object.keys(obj).forEach(key => {
            if(!acc[key]) {
                acc[key] = [];
            }
            acc[key].push(obj[key]);
        });
        return acc;
    }, {});
    // console.log(data);
    // delete file after reading
    fs.unlink(req.file.path, (err) => {
        if (err) {
            console.error(err);
            return;
        }
        // file removed
    });
    res.send(JSON.stringify(result));
});
// 这段代码是用JavaScript编写的，用于处理文件上传和处理Excel文件。以下是代码的详细解释：
// 1. 首先，导入了所需的库和模块，包括`cors()`（用于处理跨域请求）、`upload`（用于处理文件上传）和`XLSX`（用于处理Excel文件）。
// 2. 使用`fileServer.use(cors())`将CORS中间件添加到文件服务器中，以便在处理文件上传时允许跨域请求。
// 3. 定义了一个处理`/excelUpload` POST请求的路由。当接收到Excel文件上传请求时，会执行以下操作：
//   a. 使用`XLSX.readFile()`函数读取上传的Excel文件，并将文件内容存储在`workbook`变量中。
//   b. 获取Excel文件中的所有工作表名称，并将它们存储在`sheet_name_list`变量中。
//   c. 使用`XLSX.utils.sheet_to_json()`函数将第一个工作表的内容转换为JSON格式，并将结果存储在`data`变量中。
//   d. 使用`reduce()`函数将`data`中的数据进行聚合，以便将相同键的值合并到一个数组中。这个函数会返回一个新的对象，其中包含聚合后的数据。
//   e. 在处理完数据后，使用`fs.unlink()`函数删除已读取的Excel文件。如果删除文件时发生错误，将错误信息输出到控制台。
//   f. 将聚合后的数据作为JSON字符串发送给客户端。
// 总之，这段代码实现了一个处理Excel文件上传的路由，将Excel文件中的数据进行聚合，并将结果发送给客户端。

fileServer.listen(8075, () => {
    console.log('Server listening on http://localhost:8075');
});
// 这段代码是用JavaScript编写的，用于启动一个HTTP服务器并监听8075端口。以下是代码的详细解释：
// 1. `fileServer.listen(8075, ...)`：这是`http.Server`对象的一个方法，用于启动服务器并监听指定的端口。在这里，我们调用`listen`方法并将端口号设置为8075。
// 2. `() => { ... }`：这是一个箭头函数，用于在服务器启动时执行一段代码。在这里，我们使用箭头函数打印一条消息，表示服务器正在监听8075端口。消息内容为`'Server listening on http://localhost:8075'`。
// 3. `console.log(...)`：这是JavaScript中的`console.log`方法，用于在控制台输出指定的内容。在这里，我们使用`console.log`打印出服务器正在监听8075端口的消息。

exports.start = function(port = 8074) {
    http.createServer(function(req, res) {
        let body = "";
        res.setHeader("Access-Control-Allow-Origin", "*"); // 设置可访问的源
        // 解析参数
        const pathName = url.parse(req.url).pathname;
        // 这段代码是用JavaScript编写的，用于设置响应头以允许跨域请求。以下是对代码的逐行解释：
        // 1. 创建一个空字符串变量`body`，用于存储响应内容。
        // 2. 使用`res.setHeader()`方法设置响应头，允许所有源（`"*"`）访问。这意味着响应头`Access-Control-Allow-Origin`的值将设置为`"*"`，允许所有来源的请求。
        // 3. 使用`url.parse()`方法解析请求的URL，并将其解析为路径部分（不包括查询参数和 fragments）。将解析结果存储在变量`pathName`中。
        // 这段代码主要用于设置响应头以允许跨域请求，允许所有源访问。

        if(pathName == "/excelUpload" && req.method.toLowerCase() === 'post'){
            // // parse a file upload
            // let form = new formidable.IncomingForm();
            // // Set the max file size
            // form.maxFileSize = 200 * 1024 * 1024; // 200MB
            // form.parse(req, function (err, fields, files) {
            //     console.log("excelUpload")
            //     console.log(err, fields, files);
            //     let oldpath = files.file.path;
            //     let workbook = XLSX.readFile(oldpath);
            //     let sheet_name_list = workbook.SheetNames;
            //     let data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]]);
            //     console.log(data);
            //     res.end('File uploaded and read successfully.');
            // });
        } else if(pathName.indexOf(".") < 0) { //如果没有后缀名, 则为后台请求
            res.writeHead(200, { 'Content-Type': 'application/json' });
        }
        // else if(pathName.indexOf("index.html") >= 0) {
        //     fs.readFile(path.join(__dirname,"src", pathName), async (err, data) => {
        //         if (err) {
        //             res.writeHead(404, { 'Content-Type': 'text/html;charset="utf-8"' })
        //             res.end(err.message)
        //             return;
        //         }
        //         if (!err) {
        //             // 3. 针对不同的文件返回不同的内容头
        //             let extname = path.extname(pathName);
        //             let mime = FileMimes[extname]
        //             res.writeHead(200, { 'Content-Type': mime + ';charset="utf-8"' })
        //             res.end(data);
        //             return;
        //         }
        //     })
        // }
        else { //如果有后缀名, 则为前端请求
            // console.log(path.join(__dirname,"src/taskGrid", pathName));
            fs.readFile(path.join(__dirname,"src", pathName), async (err, data) => {
                if (err) {
                    res.writeHead(404, { 'Content-Type': 'text/html;charset="utf-8"' })
                    res.end(err.message)
                    return;
                }
                if (!err) {
                    // 3. 针对不同的文件返回不同的内容头
                    let extname = path.extname(pathName);
                    let mime = FileMimes[extname]
                    res.writeHead(200, { 'Content-Type': mime + ';charset="utf-8"' })
                    res.end(data);
                    return;
                }
            })
        }
        // 这段代码是用JavaScript编写的，用于处理HTTP请求。它主要分为以下几个条件块：
        // 1. 如果请求的路径名（pathName）等于 "/excelUpload" 且请求方法（req.method）的小写形式等于 "post"，则执行以下操作：
        //   a. 解析一个文件上传（parse a file upload）。
        //   b. 设置最大文件大小（form.maxFileSize = 200 * 1024 * 1024）。
        //   c. 读取上传的文件（let oldpath = files.file.path）。
        //   d. 读取文件内容（let workbook = XLSX.readFile(oldpath)）。
        //   e. 获取工作表名称列表（let sheet_name_list = workbook.SheetNames）。
        //   f. 提取第一个工作表的数据（let data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]])）。
        //   g. 输出数据（console.log(data); res.end('File uploaded and read successfully.')）。
        // 2. 如果请求的路径名中没有后缀名（pathName.indexOf(".") < 0），则将其视为后台请求（res.writeHead(200, { 'Content-Type': 'application/json' })）。
        // 3. 如果请求的路径名中包含 "index.html"（// if(pathName.indexOf("index.html") >= 0)），则执行以下操作：
        //   a. 读取文件内容（fs.readFile(path.join(__dirname,"src", pathName), async (err, data) => {）。
        //   b. 如果读取文件失败，返回404错误（res.writeHead(404, { 'Content-Type': 'text/html;charset="utf-8"' })）。
        //   c. 如果读取文件成功，根据文件类型设置内容头（let extname = path.extname(pathName); let mime = FileMimes[extname]）并返回文件内容（res.end(data)）。
        // 4. 如果请求的路径名中有后缀名，则将其视为前端请求（// else if(pathName.indexOf(".") >= 0)）。
        //   a. 读取文件内容（fs.readFile(path.join(__dirname,"src", pathName), async (err, data) => {）。
        //   b. 如果读取文件失败，返回404错误（res.writeHead(404, { 'Content-Type': 'text/html;charset="utf-8"' })）。
        //   c. 如果读取文件成功，根据文件类型设置内容头（let extname = path.extname(pathName); let mime = FileMimes[extname]）并返回文件内容（res.end(data)）。

        req.on('data', function(chunk) {
            body += chunk;
        });
        // 这段代码是用于处理HTTP请求的响应数据。`req`是一个HTTP请求对象，`data`事件表示响应数据的到来。当收到响应数据时，会触发`data`事件，并将数据块（chunk）传递给事件处理函数。
        // 事件处理函数的实现是将数据块添加到`body`变量中。`body`变量用于存储HTTP响应的正文内容。在每次收到响应数据时，都将新数据块添加到`body`变量中，从而最终得到完整的响应正文。

        req.on('end', function() {
            // 设置响应头部信息及编码
            if (pathName == "/queryTasks") { //查询所有服务信息，只包括id和服务名称
                output = [];
                travel(path.join(getDir(), "tasks"),function(pathname){
                    const data = fs.readFileSync(pathname, 'utf8');
                    let stat = fs.statSync(pathname, 'utf8');
                    // parse JSON string to JSON object
                    const task = JSON.parse(data);
                    let item = {
                        "id": task.id,
                        "name": task.name,
                        "url": task.url,
                        "mtime": stat.mtime,
                    }
                    if(item.id!= -2) {
                        output.push(item);
                    }
                });
                output.sort(compare("mtime"));
                res.write(JSON.stringify(output));
                res.end();
            }
            // 这段代码是用JavaScript编写的，用于处理HTTP请求。当请求的路径为"/queryTasks"时，它会执行以下操作：
            // 1. 初始化一个空数组`output`，用于存储查询到的服务信息。
            // 2. 调用`travel`函数，传入两个参数：`path.join(getDir(), "tasks")`和`function(pathname){ ... }`。`travel`函数的作用是遍历指定目录下的所有文件，并将文件内容解析为JSON对象。
            // 3. 在遍历文件的过程中，将每个文件的ID、名称、URL和最后修改时间（`mtime`）存储在一个对象`item`中。如果`item`的ID不为-2，则将其添加到`output`数组中。
            // 4. 对`output`数组进行排序，根据`mtime`字段进行升序排序。
            // 5. 将`output`数组转换为JSON字符串，并将其写入HTTP响应（`res`）。
            // 6. 关闭HTTP响应。
            // 总之，这段代码的作用是查询指定目录下的所有服务信息，并将结果返回给客户端。
            else if(pathName == "/queryOSVersion") {
                res.write(JSON.stringify({"version":process.platform, "bit":process.arch}));
                res.end();
            } 
            // 这段代码是JavaScript中服务器端编程中的一种常见结构，用于处理HTTP请求。它表示在满足某个条件时，执行特定的操作。在这个例子中，当请求的路径名（pathName）等于"/queryOSVersion"时，将执行以下操作：
            // 1. 使用`JSON.stringify()`方法将一个对象转换为JSON字符串，该对象包含两个属性：`version`和`bit`，分别表示操作系统的版本和位数。
            // 2. 将转换后的JSON字符串写入`res`对象，`res`对象通常表示服务器端的响应。
            // 3. 调用`res.end()`方法，表示响应的结束
            // 总之，这段代码的作用是在请求路径名为"/queryOSVersion"时，返回一个包含操作系统版本和位数的JSON对象。
            else if (pathName == "/queryExecutionInstances") { //查询所有服务信息，只包括id和服务名称
                output = [];
                travel(path.join(getDir(), "execution_instances"),function(pathname){
                    const data = fs.readFileSync(pathname, 'utf8');
                    // parse JSON string to JSON object
                    const task = JSON.parse(data);
                    let item = {
                        "id": task.id,
                        "name": task.name,
                        "url": task.url,
                    }
                    if(item.id!= -2) {
                        output.push(item);
                    }
                });
                res.write(JSON.stringify(output));
                res.end();
            } 
            // 这段代码是JavaScript语言的，主要用于处理HTTP请求。它处理GET请求，请求的路径为"/queryExecutionInstances"。当请求路径与"/queryExecutionInstances"匹配时，它会执行以下操作：
            // 1. 初始化一个空数组`output`，用于存储查询到的服务信息。
            // 2. 调用`travel`函数，传入两个参数：`path.join(getDir(), "execution_instances")`和`function(pathname){...}`。`travel`函数的作用是遍历指定目录下的所有文件，并将文件内容解析为JSON对象。
            // 3. 在遍历文件的过程中，将每个JSON对象添加到`output`数组中，条件是该对象的`id`属性不等于-2。
            // 4. 将`output`数组转换为JSON字符串，并将其写入响应中。
            // 5. 关闭响应
            // 总之，这段代码的作用是查询所有服务信息，只包括id和服务名称，并将结果返回给请求方。
            
            else if (pathName == "/queryTask") {
                let params = url.parse(req.url, true).query;
                try {
                    let tid = parseInt(params.id);
                    const data = fs.readFileSync(path.join(getDir(), `tasks/${tid}.json`), 'utf8');
                    // parse JSON string to JSON object
                    res.write(data);
                    res.end();
                } catch (error) {
                    res.write(JSON.stringify({ "error": "Cannot find task based on specified task ID." }));
                    res.end();
                }
            }
            // 这段代码是用于处理HTTP请求的，主要处理两种情况：当请求的路径为"/queryTask"时，处理查询任务请求；否则，处理其他请求。
            // 1. 当请求的路径为"/queryTask"时，首先解析请求的URL，获取查询参数，然后尝试将查询参数中的ID解析为整数。
            // 2. 如果解析成功，使用ID从"tasks"文件夹中读取相应的JSON文件，并将其转换为JSON对象。
            // 3. 将JSON对象写入响应，然后结束响应。
            // 4. 如果解析失败，将错误信息（"Cannot find task based on specified task ID."）转换为JSON字符串，并将其写入响应。
            // 5. 结束响应。

             else if (pathName == "/queryExecutionInstance") {
                let params = url.parse(req.url, true).query;
                try {
                    let tid = parseInt(params.id);
                    const data = fs.readFileSync(path.join(getDir(), `execution_instances/${tid}.json`), 'utf8');
                    // parse JSON string to JSON object
                    res.write(data);
                    res.end();
                } catch (error) {
                    res.write(JSON.stringify({ "error": "Cannot find execution instance based on specified execution ID." }));
                    res.end();
                }
            }
            // 这段代码是用于处理HTTP请求的，主要处理请求路径为"/queryExecutionInstance"的请求。当收到此请求时，它会解析请求的URL并提取查询参数，然后尝试将查询参数解析为整数。接下来，它会根据提取的ID从"execution_instances"文件夹中读取相应的JSON文件，并将其写入响应中。如果解析ID时发生错误，它会将一个包含错误信息的JSON对象写入响应中。最后，它会关闭响应。
            
            else if(pathName == "/"){
                res.write("Hello World!", 'utf8');
                res.end();
            } 
            // 这段代码是用于处理HTTP请求的。它是服务器端的代码，用于响应来自客户端的请求。当请求的路径（pathName）等于"/"时，这段代码将会被执行。
            // `else if(pathName == "/")`：这是一个条件判断语句，用于检查请求的路径是否等于"/"。如果路径等于"/"，那么下面的代码将会被执行。
            // `res.write("Hello World!", 'utf8');`：这一行使用`res.write()`方法将字符串"Hello World!"写入到响应中。这里的`utf8`表示字符串的编码方式，这里是UTF-8编码。
            // `res.end();`：这一行使用`res.end()`方法表示响应的结束。在执行完`res.write()`之后，需要使用`res.end()`来告诉服务器已经完成了响应。
            
            else if(pathName == "/deleteTask"){
                let params = url.parse(req.url, true).query;
                try {
                    let tid = parseInt(params.id);
                    let data = fs.readFileSync(path.join(getDir(), `tasks/${tid}.json`), 'utf8');
                    data = JSON.parse(data);
                    data.id = -2;
                    data = JSON.stringify(data);
                    // write JSON string to a file
                    fs.writeFile(path.join(getDir(), `tasks/${tid}.json`), data, (err) => {
                        if (err) {
                            throw err;
                        }
                    });
                    res.write(JSON.stringify({ "success": "Task has been deleted successfully." }));
                    res.end();
                } catch (error) {
                    res.write(JSON.stringify({ "error": "Cannot find task based on specified task ID." }));
                    res.end();
                }
            } 
            // 这段代码是用于处理HTTP请求的，主要处理删除任务请求。当请求的路径为"/deleteTask"时，会执行以下操作：
            // 1. 解析请求的URL参数，获取任务ID（id）。
            // 2. 使用fs.readFileSync读取任务文件（tasks/${tid}.json），并将其解析为JSON格式。
            // 3. 将任务ID设置为-2，并将任务数据转换为JSON字符串。
            // 4. 使用fs.writeFile将修改后的任务数据写入到任务文件中。
            // 5. 向客户端返回一个JSON响应，表示任务已被删除成功。
            // 6. 如果发生错误，向客户端返回一个JSON响应，表示无法根据指定的任务ID找到任务。
            
            else if(pathName == "/manageTask"){
                body = querystring.parse(body);
                data = JSON.parse(body.paras);
                let id = data["id"];
                // 这段代码的主要功能是对请求的body部分进行解析和处理。
                // 1. 首先，使用`querystring.parse()`函数将请求的body部分解析为一个对象，并将结果存储在`body`变量中。`querystring.parse()`函数的作用是将URL编码的字符串解析为对象，以便我们可以轻松地访问其中的键和值。
                // 2. 然后，使用`JSON.parse()`函数将`body.paras`部分解析为一个对象，并将结果存储在`data`变量中。`body.paras`可能是一个包含JSON数据的字符串，我们将它解析为一个对象，以便我们可以访问其中的键和值。
                // 3. 接下来，从`data`对象中提取名为`id`的属性，并将结果存储在`id`变量中。这样，我们可以使用`id`变量来处理请求中的特定数据。
                // 总之，这段代码从请求的body部分提取数据，并将其解析为JSON对象，以便我们可以轻松地访问其中的键和值。

                if (data["id"] == -1) {
                    file_names = [];
                    fs.readdirSync(path.join(getDir(), "tasks")).forEach((file)=>{
                        try{
                            if(file.split(".")[1] == "json"){
                                file_names.push(parseInt(file.split(".")[0]));
                            }
                        } catch (error) {

                        }
                    })
                    if(file_names.length == 0){
                        id = 0;
                    } else {
                        id = Math.max(...file_names) + 1;
                    }
                    data["id"] = id;
                    // write JSON string to a fil
                }
                // 这段代码的主要功能是处理一个名为`data`的对象，该对象包含一个名为`id`的属性。如果`data["id"]`的值为-1，则执行以下操作：
                // 1. 创建一个名为`file_names`的空数组。
                // 2. 使用`fs.readdirSync`读取`path.join(getDir(), "tasks")`目录下的所有文件，并将它们添加到`file_names`数组中。
                // 3. 使用`forEach`遍历`file_names`数组中的每个文件。
                // 4. 对于数组中的每个文件，使用`try`捕获可能发生的错误。
                // 5. 如果文件名以`.json`结尾，将文件名的前半部分（即数字部分）转换为整数，并将其添加到`file_names`数组中。
                // 6. 如果`file_names`数组的长度为0，将`id`的值设置为0。否则，将`id`的值设置为`file_names`数组中的最大值加1。
                // 7. 将`data["id"]`的值设置为`id`。
                // 8. 使用`writeJSONStringToFile`将`data`对象转换为JSON字符串并写入文件。

                if(data["outputFormat"] == "mysql"){
                    let mysql_config_path = path.join(getDir(), 'mysql_config.json');
                    // 检测文件是否存在
                    fs.access(mysql_config_path, fs.F_OK, (err) => {
                        if (err) {
                            console.log("File does not exist. Creating...");
                            // 文件不存在，创建文件
                            const config = {
                                host: "localhost",
                                port: 3306,
                                username: "your_username",
                                password: "your_password",
                                database: "your_database"
                            };
                            fs.writeFile(mysql_config_path, JSON.stringify(config, null, 4), (err) => {
                                if (err) throw err;
                                console.log('File is created successfully.');
                            });
                        } else {
                            console.log("File exists.");
                        }
                    });
                }
                // 这段代码是用JavaScript编写的，用于处理MySQL数据库的配置文件。当`data["outputFormat"]`的值为"mysql"时，它会执行以下操作：
                // 1. 创建一个名为`mysql_config_path`的变量，其值为`path.join(getDir(), 'mysql_config.json')`。`path.join()`函数用于将两个或多个路径组合在一起，`getDir()`是一个未定义的函数，可能用于获取当前目录。
                // 2. 使用`fs.access()`函数检查文件`mysql_config_path`是否存在。`fs.access()`函数用于检查给定的文件是否可读、可写或可执行。
                // 3. 如果文件不存在，它会执行以下操作：
                //   a. 输出一条消息"File does not exist. Creating..."，表示文件不存在，正在创建。
                //   b. 创建一个名为`config`的对象，其中包含MySQL数据库的连接信息，如主机地址、端口、用户名、密码和数据库名称。
                //   c. 使用`fs.writeFile()`函数将`config`对象转换为JSON字符串并写入到`mysql_config_path`文件中。`fs.writeFile()`函数用于将数据写入文件。
                //   d. 如果写入文件时发生错误，将抛出错误。
                //   e. 输出一条消息"File is created successfully."，表示文件创建成功。
                // 4. 如果文件存在，它会输出一条消息"File exists."，表示文件已经存在。

                data = JSON.stringify(data);
                // write JSON string to a file
                fs.writeFile(path.join(getDir(), `tasks/${id}.json`), data, (err) => {});

                res.write(id.toString(), 'utf8');
                res.end();
                // 这段代码的主要功能是：
                // 1. 将`data`对象转换为JSON字符串（`JSON.stringify(data)`）。
                // 2. 将生成的JSON字符串写入一个文件（`fs.writeFile(path.join(getDir(), `tasks/${id}.json`), data, (err) => {})`）。这里的`getDir()`是一个函数，用于获取文件的目录。`tasks/${id}.json`是一个动态生成的文件名，其中`id`是当前任务的ID。
                // 3. 将任务ID写入响应对象（`res.write(id.toString(), 'utf8');`）。
                // 4. 结束响应（`res.end();`）。

            } 
            else if(pathName == "/invokeTask"){
                body = querystring.parse(body);
                let data = JSON.parse(body.paras);
                let id = body.id;
                let task = fs.readFileSync(path.join(getDir(), `tasks/${id}.json`), 'utf8');
                task = JSON.parse(task);
                // 这段代码的主要功能是对请求的body部分进行解析和处理。以下是代码的详细解释：
                // 1. `body = querystring.parse(body);`：将请求的body部分解析为一个对象，存储在变量`body`中。`querystring.parse()`函数用于解析URL中的查询参数，这里将其用于解析请求的body部分。
                // 2. `let data = JSON.parse(body.paras);`：从`body`对象中提取`paras`属性，将其转换为JSON对象，存储在变量`data`中。
                // 3. `let id = body.id;`：从`body`对象中提取`id`属性，将其存储在变量`id`中。
                // 4. `let task = fs.readFileSync(path.join(getDir(), `tasks/${id}.json`), 'utf8');`：使用`fs.readFileSync()`函数读取指定路径的文件，并将内容解析为UTF-8编码的字符串。这里将文件路径拼接为`tasks/${id}.json`，其中`id`是从`body`对象中提取的。
                // 5. `task = JSON.parse(task);`：将读取到的文件内容解析为JSON对象，存储在变量`task`中。

                try{
                    task["links"] = data["urlList_0"];
                    if (task["links"] == undefined) {
                        task["links"] = "about:blank";
                    }
                } catch(error) {
                    task["links"] = "about:blank";
                }
                // 这段代码是在尝试执行一个任务，将数据中的链接信息赋值给任务对象的一个属性。以下是代码的详细解释：
                // 1. `try`块：表示尝试执行下面的代码块，如果执行过程中发生异常，将跳转到`catch`块。
                // 2. `task["links"] = data["urlList_0"];`：将数据中的链接信息（urlList_0）赋值给任务对象（task）的链接属性（links）。
                // 3. `if (task["links"] == undefined) {`：判断任务对象的链接属性（links）是否为undefined。如果是，则执行下面的代码。
                // 4. `task["links"] = "about:blank";`：将任务对象的链接属性（links）设置为"about:blank"，表示链接信息缺失或未知。
                // 5. `}`：表示上面的条件判断结束。
                // 6. `catch(error) {`：表示如果执行上面的代码过程中发生异常，将跳转到这里的代码块。
                // 7. `task["links"] = "about:blank";`：将任务对象的链接属性（links）设置为"about:blank"，表示链接信息缺失或未知。
                // 8. `}`：表示上面的异常处理结束。

                for (const [key, value] of Object.entries(data)) {
                    for (let i = 0; i < task["inputParameters"].length; i++) {
                        if (key === task["inputParameters"][i]["name"]) {  // 能调用
                            const nodeId = parseInt(task["inputParameters"][i]["nodeId"]);
                            const node = task["graph"][nodeId];
                            if (node["option"] === 1) {
                                node["parameters"]["links"] = value;
                            } else if (node["option"] === 4) {
                                node["parameters"]["value"] = value;
                            } else if (node["option"] === 8 && node["parameters"]["loopType"] === 0) {
                                node["parameters"]["exitCount"] = parseInt(value);
                            } else if (node["option"] === 8) {
                                node["parameters"]["textList"] = value;
                            }
                            break;
                        }
                    }
                }
                // 这段代码是用JavaScript编写的，主要用于处理一个名为`data`的对象。`Object.entries()`方法用于将对象的所有键值对转换为一个可迭代的对象，其中每个元素都是一个包含键和值的数组。
                // 代码的目的是遍历`data`对象中的所有键值对，并检查每个键是否与`task["inputParameters"]`数组中的某个元素的`name`属性相等。如果相等，则根据`task["inputParameters"]`数组中对应的`nodeId`和`option`属性进行相应的操作。
                // 具体来说，代码首先使用`for...of`循环遍历`data`对象中的所有键值对。对于每个键值对，它会使用另一个`for`循环遍历`task["inputParameters"]`数组。在第二个`for`循环中，它会检查当前键是否与`task["inputParameters"]`数组中某个元素的`name`属性相等。
                // 如果相等，它会根据`task["inputParameters"]`数组中对应的`nodeId`和`option`属性进行相应的操作。具体操作包括：
                // 1. 获取`task["inputParameters"]`数组中对应的`nodeId`，并将其转换为整数类型。
                // 2. 根据获取到的`nodeId`从`task["graph"]`对象中获取相应的节点。
                // 3. 根据节点`option`属性的值进行不同的操作：
                //   a. 如果节点`option`为1，将`value`赋值给节点的`links`属性。
                //   b. 如果节点`option`为4，将`value`赋值给节点的`value`属性。
                //   c. 如果节点`option`为8且节点`parameters`的`loopType`为0，将`value`赋值给节点的`exitCount`属性。
                //   d. 如果节点`option`为8，将`value`赋值给节点的`textList`属性。
                // 4. 如果在完成所有操作后仍然没有找到匹配的键，则不会执行任何操作。

                let file_names = [];
                fs.readdirSync(path.join(getDir(), "execution_instances")).forEach((file)=>{
                    try{
                        if(file.split(".")[1] == "json"){
                            file_names.push(parseInt(file.split(".")[0]));
                        }
                        console.log(file);
                    } catch (error) {

                    }
                })
                // 这段代码的主要功能是读取指定目录下的所有文件名，并将它们添加到`file_names`数组中。具体解释如下：
                // 1. 首先，创建一个空数组`file_names`，用于存储文件名。
                // 2. 使用`fs.readdirSync()`方法读取指定目录下的所有文件名，并将它们存储在`file`变量中。`path.join()`方法用于将目录路径与文件名连接起来。
                // 3. 使用`forEach()`方法遍历文件名数组，对每个文件名执行以下操作：
                //   1. 使用`split()`方法将文件名拆分为文件名和扩展名两部分，存储在`file.split(".")`数组中。
                //   2. 如果文件扩展名为`json`，则将文件名的整数值（即文件名前的数字）添加到`file_names`数组中。
                //   3. 使用`console.log()`方法打印当前文件名。
                // 4. 使用`try...catch`语句捕获可能发生的错误，但这里没有处理任何错误，只是简单地跳过了错误。

                let eid = 0;
                if (file_names.length != 0) {
                    eid = Math.max(...file_names) + 1;
                }
                task["id"] = eid;
                task = JSON.stringify(task);
                fs.writeFile(path.join(getDir(), `execution_instances/${eid}.json`), task, (err) => {});
                res.write(eid.toString(), 'utf8');
                res.end();
                // 这段代码的主要功能是：
                // 1. 定义一个变量 `eid` 为 0。
                // 2. 检查 `file_names` 数组的长度是否为 0。如果不为 0，则计算 `file_names` 中的最大值，并将结果加 1，赋值给 `eid`。
                // 3. 将 `task` 对象转换为 JSON 字符串，并将其赋值给 `task` 变量。
                // 4. 使用 `fs.writeFile` 函数将 `task` 字符串写入到 `execution_instances` 文件夹中，文件名为 `${eid}.json`。
                // 5. 使用 `res.write` 函数将 `eid` 转换为字符串并写入到响应中。
                // 6. 使用 `res.end` 函数结束响应。

            } 
            else if(pathName == "/getConfig"){
                let config = fs.readFileSync(path.join(getDir(), `config.json`), 'utf8');
                config = JSON.parse(config);
                res.write(JSON.stringify(config));
                res.end();
            } 
            // 这段代码是用于处理服务器响应请求的代码。当请求的路径为"/getConfig"时，它会执行以下操作：
            // 1. 使用`fs.readFileSync`从`getDir()`目录下读取名为`config.json`的文件，并将其内容解析为`utf8`编码的字符串。
            // 2. 使用`JSON.parse`将字符串解析为对象（即JSON数据）。
            // 3. 使用`JSON.stringify`将对象转换为JSON字符串，并将其写入响应的发送缓冲区（`res`）。
            // 4. 关闭响应的发送缓冲区（`res.end()`）。
            // 总之，这段代码的作用是处理请求路径为"/getConfig"的请求，并返回一个JSON格式的配置文件。
            
            else if(pathName == "/setUserDataFolder"){
                let config = fs.readFileSync(path.join(getDir(), `config.json`), 'utf8');
                config = JSON.parse(config);
                body = querystring.parse(body);
                config["user_data_folder"] = body["user_data_folder"];
                config = JSON.stringify(config);
                fs.writeFile(path.join(getDir(), `config.json`), config, (err) => {});
                res.write(JSON.stringify({ "success": "User data folder has been set successfully." }));
                res.end();
            }
            // 这段代码是用于处理HTTP请求的响应。当请求的路径为"/setUserDataFolder"时，它会执行以下操作：
            // 1. 从文件系统中读取名为"config.json"的文件，并将其解析为JSON对象。
            // 2. 将请求的请求参数（通过body传递）解析为对象。
            // 3. 将请求参数中的"user_data_folder"字段值添加到JSON对象中。
            // 4. 将更新后的JSON对象重新序列化为字符串。
            // 5. 将更新后的配置文件写入文件系统中。
            // 6. 向请求方返回一个JSON响应，表示设置用户数据文件夹成功。
            // 总之，这段代码的作用是设置用户数据文件夹的路径，并将新的配置写入"config.json"文件中。

        });
    }).listen(port);
    // 这段代码是使用Node.js的HTTP模块创建一个HTTP服务器，监听指定端口的请求。以下是代码的详细解释：
    // 1. `http.createServer(function(req, res) {}`：创建一个HTTP服务器，传入一个回调函数作为参数。回调函数会在接收到客户端请求时被调用，参数`req`表示请求对象，参数`res`表示响应对象。
    // 2. `.listen(port)`：调用服务器对象的`listen`方法，传入一个端口号作为参数。这个方法表示服务器将会开始监听指定端口的请求，等待客户端发来请求。
    // 总之，这段代码的作用是创建一个HTTP服务器，监听指定端口的请求，等待客户端发来请求并处理。

    console.log("Server has started.");
    // 这段代码是用JavaScript编写的，用于在控制台中输出一条消息 "Server has started."。`console.log()` 函数用于在控制台中打印日志信息，其中 "Server has started." 是要打印的消息。
}
