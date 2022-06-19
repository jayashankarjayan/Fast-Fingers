from __init__ import database
from models.entity import Users

def delete_user(name):
    Users.query.filter(Users.name == name).delete()
    database.session.commit()