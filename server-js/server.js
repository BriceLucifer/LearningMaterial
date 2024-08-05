const http = require('http');
const url = require('url');

// Define a simple object to act as a database
const userDatabase = {
    1: { id: 1, name: 'Alice', age: 30 },
    2: { id: 2, name: 'Bob', age: 25 }
};

// Function to get user by ID
function getUserById(id) {
    return userDatabase[id] || null;
}

// Function to handle different routes
function handleRequest(req, res) {
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;
    const method = req.method;

    if (pathname.startsWith('/user')) {
        const userId = parseInt(pathname.split('/')[2], 10);

        if (method === 'GET' && !isNaN(userId)) {
            const user = getUserById(userId);
            if (user) {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(user));
            } else {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('User not found');
            }
        } else if (method === 'POST') {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });
            req.on('end', () => {
                const newUser = JSON.parse(body);
                if (userDatabase[newUser.id]) {
                    res.writeHead(400, { 'Content-Type': 'text/plain' });
                    res.end('User already exists');
                } else {
                    userDatabase[newUser.id] = newUser;
                    res.writeHead(201, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(newUser));
                }
            });
        } else if (method === 'PUT' && !isNaN(userId)) {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });
            req.on('end', () => {
                const updatedUser = JSON.parse(body);
                const user = userDatabase[userId];
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
        } else if (method === 'DELETE' && !isNaN(userId)) {
            if (userDatabase[userId]) {
                delete userDatabase[userId];
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

// Create and start the server
const server = http.createServer(handleRequest);

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
const [hello,world]= [1,2];
console.log(hello,world)