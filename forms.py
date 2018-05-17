from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name")])
    email = StringField('Email', validators=[DataRequired("Please enter your email"), Email('Please enter a valid email')])
    password = PasswordField('Password', validators=[
                        DataRequired("Please enter your password"),
                        Length(min=6, message="Password must be at least 6 characters"),
                        EqualTo("password", "Password does not match")
                    ])
    password_confirm = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')