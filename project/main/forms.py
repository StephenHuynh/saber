from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, NumberRange


class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[Length(min=3, max=254)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=254)])
    mobile = IntegerField('Mobile', validators=[DataRequired(), NumberRange(min=5)])    
    note = TextAreaField('Comment', validators=[DataRequired(), Length(min=6, max=254)])
    

