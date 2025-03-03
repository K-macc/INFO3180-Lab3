from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', render_kw={"style": "height: 40px; border-radius: 5px; border: 2px solid #333;"}, validators=[InputRequired()])
    email = StringField('Email', render_kw={"style": "height: 40px; border-radius: 5px; border: 2px solid #333;"}, validators=[InputRequired()])
    subject = StringField('Subject', render_kw={"style": "height: 40px; border-radius: 5px; border: 2px solid #333;"}, validators=[InputRequired()])
    message = TextAreaField('Message', render_kw={"style": "height: 120px; border-radius: 5px; resize: none; border: 2px solid #333;"}, validators=[InputRequired()])
    submit = SubmitField('Submit')