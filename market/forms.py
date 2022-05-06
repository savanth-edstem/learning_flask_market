from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, equal_to, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Conform Password', validators=[equal_to("password1"), DataRequired()])
    submit = SubmitField(label='Create Account')
