from __init__ import database
from models.entity import Users

def reset_user_score(name):
    user = Users.query.filter(Users.name == name).first()
    user.score = 0
    database.session.commit()

def user_rejoined(name, socket_id):
    user = Users.query.filter(Users.name == name).first()
    user.score = 0
    user.sock_id = socket_id
    database.session.commit()

def update_user_score(name, score):
    user = Users.query.filter(Users.name == name).first()
    user.score = score
    sock_id = user.sock_id
    database.session.commit()
    return sock_id