from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class FirstFerm(FlaskForm):
    ident = StringField('ID', validators=[Length(max=10)])
    startdate = StringField('Date Started', validators=[Length(max=10)])
    notes = TextAreaField('Notes', validators=[Length(max=150)])
    alertemail = StringField('Email')
    submit = SubmitField('Post')
