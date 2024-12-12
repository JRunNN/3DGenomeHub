import express from 'express';
import cors from  'cors'
import fs from 'fs'
import http from 'http'
import path from 'path'

import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
// import WebSocket, { WebSocketServer } from 'ws';
// const WebSocket = require('ws');

const app = express();
app.use(cors())

// const server = http.createServer(app);
// const wss = new WebSocket.Server({ server });

// app.use(express.static(path.join(__dirname, 'dist')))
app.use('/static',express.static(path.join(__dirname, 'static')))


const port = 8002;

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
