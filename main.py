from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Dict
import json
import uvicorn
import json
from datetime import datetime

app = FastAPI(title="Live Chat Server")


class ConnectionManager:
    def __init__(self):
        # Maps username -> WebSocket
        self.active_connections: Dict[str, WebSocket] = {}

    @property
    def online_users(self):
        return list(self.active_connections.keys())

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[username] = websocket
        # Notify everyone about the new user
        await self.broadcast({
            "type": "system",
            "message": f"🟢 {username} joined the chat",
            "online_users": self.online_users
        })

    async def disconnect(self, username: str):
        if username in self.active_connections:
            del self.active_connections[username]
        # Notify everyone about the user leaving
        await self.broadcast({
            "type": "system",
            "message": f"🔴 {username} left the chat",
            "online_users": self.online_users
        })

    async def broadcast(self, data: dict):
        """Send a message to all connected clients."""
        disconnected = []
        for username, ws in self.active_connections.items():
            try:
                await ws.send_text(json.dumps(data))
            except Exception:
                disconnected.append(username)
        # Clean up any broken connections
        for username in disconnected:
            del self.active_connections[username]

    async def send_personal(self, username: str, data: dict):
        """Send a message to a specific user."""
        if username in self.active_connections:
            await self.active_connections[username].send_text(json.dumps(data))


manager = ConnectionManager()


@app.get("/")
async def get():
    """Serve the chat client HTML page."""
    with open("client.html", "r") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # Reject duplicate usernames
    if username in manager.active_connections:
        await websocket.accept()
        await websocket.send_text(json.dumps({
            "type": "error",
            "message": "Username already taken. Please choose another."
        }))
        await websocket.close()
        return

    await manager.connect(username, websocket)

    # Send the current online users list only to the new user
    await manager.send_personal(username, {
        "type": "welcome",
        "message": f"Welcome to the chat, {username}!",
        "online_users": manager.online_users
    })

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)

            if payload.get("type") == "message":
                await manager.broadcast({
                    "type": "message",
                    "sender": username,
                    "text": payload.get("text", ""),
                    "online_users": manager.online_users
                })

    except WebSocketDisconnect:
        await manager.disconnect(username)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
