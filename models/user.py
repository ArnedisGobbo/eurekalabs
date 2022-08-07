from db.db import db
import uuid


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    user_key = db.Column(db.String(80))

    def __init__(self, username):
        self.username = username
        self.user_key = uuid.uuid4().hex

    def json(self):
        return {
            'username': self.username,
            'email': self.email,
            'user_key': self.user_key
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_key(cls, user_key):
        return cls.query.filter_by(user_key=user_key).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
