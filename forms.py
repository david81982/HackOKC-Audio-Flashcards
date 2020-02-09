from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class KeyWordForm(FlaskForm):
    body = TextField('Message', [
        DataRequired(),
        Length(min=1, message=('I need more than one keyowrd'))])
    submit = SubmitField('Submit')