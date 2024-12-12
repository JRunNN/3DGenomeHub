
// const http = require('http');
// const handler = require('serve-handler');

// const server = http.createServer((request, response) => {
//   // 服务 Vite 应用的构建目录，默认是 'dist'
//   return handler(request, response, {
//     "public": "dist",
//     "directoryListing": false
//   });
// })

// const PORT = 5173; // 你希望服务器监听的端口号

// server.listen(PORT, () => {
//   console.log(`Running at http://localhost:${PORT}`);
// });


const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 9999; // Port you wish server to listen on

const server = http.createServer((req, res) => {
  // Determine the file path based on the requested URL
  let filePath = '.' + req.url;
  if (filePath === './') {
    filePath = './dist/index.html'; // Serve index.html for root
  } else {
    filePath = './dist' + req.url; // Serve other static files
  }

  // Determine the content type by file extension
  const extname = String(path.extname(filePath)).toLowerCase();
  const mimeTypes = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.wav': 'audio/wav',
    '.mp4': 'video/mp4',
    '.woff': 'application/font-woff',
    '.ttf': 'application/font-ttf',
    '.eot': 'application/vnd.ms-fontobject',
    '.otf': 'application/font-otf',
    '.wasm': 'application/wasm'
  };

  const contentType = mimeTypes[extname] || 'application/octet-stream';

  // Read and serve the file over response
  fs.readFile(filePath, function(error, content) {
    if (error) {
      if(error.code == 'ENOENT'){ // If the file is not found
        fs.readFile('./dist/404.html', function(error, content) { // Serve a custom 404 page
          res.writeHead(404, { 'Content-Type': 'text/html' });
          res.end(content, 'utf-8');
        });
      } else { // For any other server error
        res.writeHead(500);
        res.end('Sorry, check with the site admin for error: '+error.code+' ..\n');
      }
    } else { // If the file is found, serve it with the right content type
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});