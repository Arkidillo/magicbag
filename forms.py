from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField, DateField
from wtforms.validators import DataRequired

class DataCollect(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    income = IntegerField('Income')
    submit = SubmitField('Submit')

class QueryForm(FlaskForm):
    name = StringField('Name')
    income = IntegerField('Income')
    last_visit_date = DateField('Last visited date')
    submit = SubmitField('Submit')
