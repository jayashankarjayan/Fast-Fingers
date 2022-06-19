from flask import render_template, request
from flask_socketio import SocketIO, emit

from __init__ import APP
from process_input import calculate_score
from models import read, create, update, delete
import constants

# socketio = SocketIO(APP, logger=True, engineio_logger=True)
socketio = SocketIO(APP)

expected_user_input = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

@APP.route("/")
def index_page():
    return render_template("index.html")
    
@APP.route("/scoreboard")
def scoreboard_page():
    return render_template("scoreboard.html")
    
@socketio.event
def new_user(user_name):
    user_details = {"name": user_name, "score": 0, "sock_id": request.sid}
    status = create.add_new_user(user_details)
    if status == constants.USER_ALREADY_EXISTS:
        user = read.get_user_by_name(user_name)
        update.user_rejoined(user.name, request.sid)
    elif status == constants.NEW_USER_ADDED:
        emit("new_user_on_scoreboard", user_details, broadcast=True)

@socketio.event
def list_all_users():
    all_users = read.get_all_users()
    return all_users

@socketio.event
def exit_user(user_name):
    print("User left: ", user_name)
    delete.delete_user(user_name)
    all_users = read.get_all_users()
    emit("list_all_users", all_users, broadcast=True)

@socketio.event
def user_input(data):
    score = calculate_score(expected_user_input.strip(), data["input"])
    print("Score for {0} is {1}".format(data["user"], score))
    sock_id = update.update_user_score(data["user"], score)
    details = {"sock_id": sock_id, "score": score}
    emit("update_user_score", details, broadcast=True)
    


if __name__ == "__main__":
    socketio.run(APP, host="0.0.0.0", port=8000)

