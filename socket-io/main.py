from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from process_input import calculate_score

APP = Flask(__name__)
socketio = SocketIO(APP, logger=True, engineio_logger=True)
# socketio = SocketIO(APP)

all_users = []
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
    user_details = {"name": user_name, "score": 0}
    if user_name not in all_users:
        all_users.append(user_details)
    emit("new_user_on_scoreboard", user_details, broadcast=True)  

@socketio.event
def list_all_users():
    return all_users

@socketio.event
def exit_user(user_name):
    print("User left: ", user_name)
    if user_name in all_users:
        all_users.remove(user_name)
    emit("refresh_scoreboard", {"data": all_users})

@socketio.event
def user_input(data):
    score = calculate_score(expected_user_input.strip(), data["input"])
    print("Score for {0} is {1}".format(data["user"], score))
    return score


if __name__ == "__main__":
    socketio.run(APP, host="0.0.0.0", port=8000)

