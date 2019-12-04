from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField(
        'Description', validators=[DataRequired(), Length(max=1400)])
