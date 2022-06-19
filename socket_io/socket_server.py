from aiohttp import web
import socketio

from process_input import calculate_score

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

@sio.event
def new_user(sid, user_name):
    print("New user joined: ", user_name)

@sio.event
def exit_user(sid, user_name):
    print("User left: ", user_name)

@sio.event
def user_input(sid, data):
    return calculate_score("hello world", data["input"])

if __name__ == '__main__':
    web.run_app(app)