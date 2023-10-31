
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from twitter.models import User 




class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    image = FileField('Profile Picture',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
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

    # -------------------------------------------------------------

# profile pic, username, and email update 




class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    image = FileField('Profile Picture',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Update')

# custom validator for the username if it's taken
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError('Username Already Taken. Please Choose A New One.')

# custom validator for the email if it's taken
    def validate_email(self, email):
         if email.data != current_user.email:  #check if the user wanna change his email to a knew one then check if that new one is taken ashan mn gher el if statement de, his username is already in the database f lw geh y3ml update only to pic mn gher ma y8yr el username hyban fl database en el username da taken w mynf34
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError('Email Already Taken. Please Choose A New One.')

        