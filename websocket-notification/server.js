const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });

const clients = new Set();

server.on('connection', (socket) => {
    console.log('Client connected');
    clients.add(socket);

    // Send a welcome message when a client connects
    socket.send('Welcome to the WebSocket server!');

    // Handle incoming messages from clients and broadcast them
    socket.on('message', (message) => {
        console.log(`Received message: ${message}`);
        for (const client of clients) {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        }
    });

    // Handle client disconnection
    socket.on('close', () => {
        console.log('Client disconnected');
        clients.delete(socket);
    });

    // Handle errors
    socket.on('error', (error) => {
        console.error(`WebSocket error: ${error.message}`);
    });
});

console.log('WebSocket server is running on ws://localhost:8080');
