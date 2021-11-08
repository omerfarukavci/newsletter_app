from sqlalchemy.orm import backref
from newsletter import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User: {self.username}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(), nullable=False, unique=True)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, user):
        self.title = title
        self.content = content
        self.user = user

    def __repr__(self):
        return f'Title: {self.title}\nContent: {self.content}'

