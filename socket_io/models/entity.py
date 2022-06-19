from email.policy import default
from __init__ import database

class Users(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), unique=True, nullable=False)
    score = database.Column(database.Integer, nullable=False, default=0)
    sock_id = database.Column(database.String(100), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           "id": int(self.id),
           "name": str(self.name),
           "score": int(self.score),
           "sock_id": str(self.sock_id)
       }

if __name__ == "__main__":
    database.create_all()