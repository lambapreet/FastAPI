from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI WebSocket Chat</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; display: flex; justify-content: center; padding: 40px; }
        #chat { width: 500px; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0,0,0,0.1); }
        #messages { height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        input { width: 80%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { width: 18%; padding: 10px; border: none; background: #007bff; color: white; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div id="chat">
        <h2>FastAPI WebSocket Chat 💬</h2>
        <div id="messages"></div>
        <input id="messageInput" type="text" placeholder="Type a message..." />
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onmessage = function(event) {
            let messages = document.getElementById('messages');
            let message = document.createElement('div');
            message.textContent = event.data;
            messages.appendChild(message);
            messages.scrollTop = messages.scrollHeight;
        };

        function sendMessage() {
            let input = document.getElementById("messageInput");
            ws.send(input.value);
            input.value = "";
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def home():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You wrote: {data}")
    except WebSocketDisconnect:
        print("Disconnect")
