from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField, DateField, TextAreaField, validators
from wtforms.validators import DataRequired

class DataCollect(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    school_length = IntegerField('How many winters or springs have you been in school?', [validators.optional()])
    school_name = TextAreaField('Do you know the name of your school?', [validators.optional(), validators.length(max=1000)])
    people_in_house = TextAreaField('Who do you live with? How many people sleep in the house? How many people do you eat your dinner with?', [validators.optional(), validators.length(max=1000)])
    why_not_in_school = TextAreaField('Can you tell me why do you stay at home not going to school?', [validators.optional(), validators.length(max=1000)])
    dreams = TextAreaField('Can you whisper 3 of your dreams to the Santa Claus?', [validators.optional(), validators.length(max=1000)])
    most_loved = TextAreaField('Who do you love the most in your family? ', [validators.optional(), validators.length(max=1000)])
    potential_abuser = TextAreaField('Can you please write down the person who always does bad things?', [validators.optional(), validators.length(max=1000)])
    what_abuse = TextAreaField('Can you tell me what kind of things does the angry person do? Let them know that they are completely okay and safe to tell anything to the Santa Claus.', [validators.optional(), validators.length(max=1000)])
    phone = TextAreaField('Where can Santa Claus find you next year? (phone number)', [validators.optional(), validators.length(max=1000)])
    address = TextAreaField('Where can Santa Claus find you next year? (address)', [validators.optional(), validators.length(max=1000)])
    submit = SubmitField('Submit')

class QueryForm(FlaskForm):
    name = StringField('Name')
    income = IntegerField('Income')
    last_visit_date = DateField('Last visited date')
    submit = SubmitField('Submit')
