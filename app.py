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

@app.route('/')
@app.route('/index')

def index():
    #user = {'username': 'Garrett'}
    return render_template('index.html', title='Home')

@app.route('/forms')
def forms():
    return render_template('forms.html', title='Forms')

@app.route('/query')
def query():
    return render_template('query.html', title='Query')

if __name__ == '__main__':
    app.run()
