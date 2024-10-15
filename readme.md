# Push Notifications com WebSocket – Projeto de Estudo 📡

Este repositório contém um **exemplo educacional** de como implementar **notificações em tempo real** utilizando **WebSocket** e **FastAPI**, com uma interface frontend estilizada em HTML e CSS. O projeto é voltado para quem deseja aprender conceitos básicos de comunicação em tempo real e WebSocket.

⚠️ **Aviso:** Este projeto é apenas um **experimento educacional** e não deve ser utilizado em ambientes de produção.

---

## 💡 Visão Geral
O projeto consiste em:
- Um servidor WebSocket simples usando **FastAPI**.
- Um frontend em **HTML e CSS** que exibe notificações com animações e permite fechá-las.
- Comunicação **bidirecional** entre o cliente e o servidor via WebSocket.

---

## 📋 Pré-requisitos
Certifique-se de ter o seguinte instalado:
- Python 3.x
- pip (gerenciador de pacotes do Python)

---

## 🛠️ Configuração do Servidor (FastAPI)

1. **Instale as dependências**:
   ```bash
    pip install fastapi uvicorn
   ```
   ```bash
    pip install websockets
   ```
   
2. **Crie o arquivo do servidor (`main.py`)**:

   ```python
   from fastapi import FastAPI, WebSocket
   from fastapi.responses import HTMLResponse

   app = FastAPI()

   @app.get("/")
   async def get():
       with open("index.html", "r") as f:
           return HTMLResponse(content=f.read(), status_code=200)

   @app.websocket("/ws")
   async def websocket_endpoint(websocket: WebSocket):
       await websocket.accept()
       while True:
           data = await websocket.receive_text()
           await websocket.send_text(f"Mensagem recebida: {data}")
   ```

3. **Execute o servidor**:
   ```bash
   uvicorn main:app --reload
   ```

---

## 🌐 Interface Web (Frontend)

1. **Crie o arquivo `index.html`** com o seguinte conteúdo:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Push Notifications com WebSocket</title>
       <style>
           body {
               background-color: #f4f4f4;
               font-family: 'Arial', sans-serif;
               display: flex;
               justify-content: center;
               align-items: center;
               min-height: 100vh;
               margin: 0;
           }
           h1 {
               text-align: center;
               font-size: 2rem;
               color: #333;
           }
           #notifications {
               max-width: 400px;
               background-color: #fff;
               border-radius: 8px;
               box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
               padding: 20px;
               max-height: 500px;
               overflow-y: auto;
           }
           .notification {
               background-color: #e0f7fa;
               border-left: 5px solid #00838f;
               padding: 10px;
               margin-bottom: 10px;
               border-radius: 4px;
               display: flex;
               justify-content: space-between;
               align-items: center;
               animation: fadeIn 0.5s;
           }
           .close-btn {
               background-color: transparent;
               border: none;
               color: #00838f;
               font-size: 1.2rem;
               cursor: pointer;
               margin-left: 10px;
           }
           .close-btn:hover {
               color: #005662;
           }
           @keyframes fadeIn {
               from { opacity: 0; transform: translateY(10px); }
               to { opacity: 1; transform: translateY(0); }
           }
           @keyframes fadeOut {
               from { opacity: 1; transform: translateY(0); }
               to { opacity: 0; transform: translateY(10px); }
           }
       </style>
   </head>
   <body>
       <div>
           <h1>Notificações em Tempo Real</h1>
           <div id="notifications"></div>
       </div>

       <script>
           const notificationsDiv = document.getElementById('notifications');
           const ws = new WebSocket("ws://localhost:8000/ws");

           ws.onmessage = function (event) {
               const notification = document.createElement('div');
               notification.classList.add('notification');

               const message = document.createElement('p');
               message.textContent = `🔔 ${event.data}`;

               const closeButton = document.createElement('button');
               closeButton.classList.add('close-btn');
               closeButton.innerHTML = '&times;';
               closeButton.onclick = () => {
                   notification.style.animation = 'fadeOut 0.5s';
                   setTimeout(() => notification.remove(), 500);
               };

               notification.appendChild(message);
               notification.appendChild(closeButton);
               notificationsDiv.appendChild(notification);
               notificationsDiv.scrollTop = notificationsDiv.scrollHeight;
           };

           ws.onopen = () => console.log("Conectado ao WebSocket");
           ws.onclose = () => console.log("Desconectado do WebSocket");
       </script>
   </body>
   </html>
   ```

---

## 🎯 Como Testar

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

2. Acesse o frontend em [http://localhost:8000](http://localhost:8000).

3. Abra o console do navegador (F12) e envie mensagens para o WebSocket para ver as notificações em tempo real.

4. Para enviar as notificações faça assim usando o curl:
    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/send-notification/?message=oi notificacao' \
    -H 'accept: application/json' \
    -d ''
    ```
---

## 🚀 Recursos Explorados
- **WebSocket** para comunicação em tempo real.
- **FastAPI** como servidor backend.
- **HTML, CSS e JavaScript** para interface estilizada e interativa.
- **Animações CSS** para uma experiência mais fluida.
- **Auto-scroll** para visualizar as últimas notificações.

---

## 📚 Referências e Aprendizado Futuro
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [WebSocket API – MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [CSS Animations – MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)

---

Divirta-se aprendendo e experimentando com notificações em tempo real! 🎉