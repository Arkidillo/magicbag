from forms import DataCollect
import datetime
from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///magicbag-form"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://zpxaecnydqxxhj:258722efa1e462c8c825f0e63f575b8d1c0c9e8535fdfda058b6b28ba05e01bf@ec2-107-20-211-10.compute-1.amazonaws.com:5432/d1p1mua37cs8ho"
db = SQLAlchemy(app)

#from models import Result

app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Garrett'}
    return render_template('index.html', title='Home', user=user)

@app.route('/forms')
def forms():
    return render_template('forms.html', title='Forms')

@app.route('/query')
def query():
    return render_template('query.html', title='Query')



@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = DataCollect()
    if form.validate_on_submit():
        lat = request.form['lat']
        long = request.form['long']
        flash('Info submitted for {} with income {} at time {} and {}, {}'.format(form.name.data, form.income.data, datetime.datetime.today().strftime('%Y-%m-%d'), lat, long))
        return redirect('/form')
    return render_template('form.html', title='Info Form', form=form)

if __name__ == '__main__':
    app.run()
