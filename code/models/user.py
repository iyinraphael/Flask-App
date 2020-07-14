from db import db

# A model is an internal representation of an entity
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # Unique ID:
    username = db.Column(db.String(80)) # creates username column and limits character to 80
    password = db.Column(db.String(80)) # creates password column and limits character to 80

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
