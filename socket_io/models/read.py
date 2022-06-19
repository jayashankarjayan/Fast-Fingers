from models.entity import Users
from flask import jsonify

def get_all_users():
    records = Users.query.order_by(Users.score.desc()).all()
    records = [record.serialize for record in records]
    return records

def get_user_by_name(name):
    record = Users.query.filter(Users.name == name).first()
    return record