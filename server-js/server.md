# 使用 Node.js 内置的 http 模块来构建一个简单的 HTTP 服务器

## 引入http模块和url模块
http 模块: 用于创建和处理 HTTP 服务器和请求
url 模块: 用于解析和处理 URL 字符串及其各部分
```
const http = require("http");
const url = require("url");
```

## 定义一个简单的对象为数据库
```
const data = {
    1: { id: 1, name: 'Alice', age: 30 },
    2: { id: 2, name: 'Bob', age: 25 }
}
```

## 定义获取的id的方法
```
function getUserById(data) {
    return data[id] || null;
}
```

## 处理请求的方法
```
function handleRequest(req, res) {
    // 用于将 URL 字符串解析成一个对象
    const parsedUrl = url.parse(rea.url, true);
    // 从解析后的 URL 对象中提取出路径名部分
    const pathname = parsedUrl.pathname;
    // 获取 HTTP 请求的方法
    const method = req.method;
    
    if (pathname.startsWith('/user')) {
        const userId = parseInt(pathname.split('/')[2], 10);
        // 如果请求方法是GET且用户ID是数字
        if (method === 'GET' && !isNaN(userId)) {
            const user = getUserById(userId);
            if (user) {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(user));
            } else {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('User not found');
            }
        }
        // 如果请求方法是POST
        else if (method === 'POST') {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });
            req.on('end', () => {
                const newUser = JSON.parse(body);
                if (data[newUser.id]) {
                    res.writeHead(400, { 'Content-Type': 'text/plain' });
                    res.end('User already exists');
                } else {
                    data[newUser.id] = newUser;
                    res.writeHead(201, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(newUser));
                }
            });
        } 
        // 如果请求方法是PUT且用户ID是数字
        else if (method === 'PUT' && !isNaN(userId)) {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });
            req.on('end', () => {
                const updatedUser = JSON.parse(body);
                const user = data[userId];
                if (user) {
                    user.name = updatedUser.name !== undefined ? updatedUser.name : user.name;
                    user.age = updatedUser.age !== undefined ? updatedUser.age : user.age;
                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(user));
                } else {
                    res.writeHead(404, { 'Content-Type': 'text/plain' });
                    res.end('User not found');
                }
            });
        } 
        // 如果请求方法是DELETE且用户ID是数字
        else if (method === 'DELETE' && !isNaN(userId)) {
            if (data[userId]) {
                delete data[userId];
                res.writeHead(204, { 'Content-Type': 'text/plain' });
                res.end();
            } else {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('User not found');
            }
        } else {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('Not found');
        }
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not found');
    }
}
```

## 创建服务器
```
const server = http.createServer(handleRequest);
```

## 启动服务
```
server.listen(3000, () => {
    console.log("Server is running");
})
```

## 测试
```
curl http://localhost:3000/user/1
```