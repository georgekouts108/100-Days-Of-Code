from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Please enter a valid email.")])
    password = PasswordField(label='Password', validators=[Length(min=8, max=30, message='Password must be at least 8 characters.'), DataRequired(message="Please enter your password.")])
    submit = SubmitField(label='Log In')
