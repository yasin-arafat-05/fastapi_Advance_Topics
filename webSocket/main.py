from fastapi import FastAPI, WebSocket, WebSocketDisconnect,Request
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory='templates')
app = FastAPI()

@app.get('/')
async def homepage(req: Request):
    return template.TemplateResponse("general_pages/homepage.html", {"request": req})

# let we have multiple websockets
web_sockets_list = []

@app.websocket('/ws')
async def web_sockets(websocket: WebSocket):
    # accept the request of the client
    await websocket.accept()

    # If the current websocket request is not in web_sockets_list, add it to the list:
    if websocket not in web_sockets_list:
        web_sockets_list.append(websocket)

    # while connecting:
    try:
        while True:
            data = await websocket.receive_text()
            for web in web_sockets_list:
                # send message accept the current websocket
                if web != websocket:
                    await web.send_text(f"{data}")
    except WebSocketDisconnect:
        web_sockets_list.remove(websocket)
        await websocket.close()
