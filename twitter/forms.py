from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from twitter.models import User 


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# custom validator for the username if it's taken
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError('Username Already Taken. Please Choose A New One.')


# custom validator for the email if it's taken
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError('Email Already Taken. Please Choose A New One.')




class LoginForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In ')

    

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Tweet')
