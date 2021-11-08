from newsletter import app, db
from newsletter.models import User

db.create_all()

user1 = User('admin', '123456')

db.session.add(user1)
db.session.commit()