from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Gerenciador de conexões WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Espera por mensagens do cliente (opcional)
            data = await websocket.receive_text()
            await manager.broadcast(f"Mensagem recebida: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.post("/send-notification/")
async def send_notification(message: str):
    """Endpoint para enviar notificações via WebSocket"""
    await manager.broadcast(message)
    return {"message": "Notificação enviada para todos os clientes!"}
