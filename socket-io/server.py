from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit("my_message", "Ok, great")

if __name__ == '__main__':
    web.run_app(app)