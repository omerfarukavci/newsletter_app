from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test123@localhost:5432/flask_test"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from newsletter import routes
