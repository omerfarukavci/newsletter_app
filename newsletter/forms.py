from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm): #TODO
    pass


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('News Text', validators=[DataRequired()])
    submit = SubmitField('Add News')