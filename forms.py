from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class DataCollect(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    income = IntegerField('Income')
    submit = SubmitField('Submit')
