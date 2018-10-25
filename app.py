from forms import *
import datetime
from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///magicbag-form"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://zpxaecnydqxxhj:258722efa1e462c8c825f0e63f575b8d1c0c9e8535fdfda058b6b28ba05e01bf@ec2-107-20-211-10.compute-1.amazonaws.com:5432/d1p1mua37cs8ho"
database = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'], sslmode='allow')
db = SQLAlchemy(app)

from models import *
#from models import Result

app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
@app.route('/index')
def index():
    #user = {'username': 'Garrett'}
    return render_template('index.html', title='Home')


@app.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if request.method == 'POST':
        name = form.name.data
        income = form.income.data
        last_visit_date = form.last_visit_date.data

        cur = database.cursor()
        query = "SELECT * from form "
        if name is not '':
            query += "WHERE name = '{}'".format(name)
        elif income is not None:
            query += "WHERE income <= {}".format(income)
        elif last_visit_date is not None:
            query += "WHERE last_visit_date <= '{}'".format(last_visit_date)

        session['map_query'] = query
        cur.execute(query)
        lst = cur.fetchall()
        return render_template('table.html', title='Table', data=lst)


    return render_template('query.html', title='Query', form=form)

@app.route('/map')
def createMap():

    cur = database.cursor()
    query = session['map_query']
    cur.execute(query)
    lst = cur.fetchall()

    map = folium.Map(location=[47.916597, 106.903083],
                        tiles = "Stamen Terrain",
                        zoom_start = 12)


    #directions from headquarters(maybe)
    # https://www.google.com/maps/dir/?api=1&origin=<latitude>,<longitude>&destination=<latitude>,<longitude>
    # https://www.google.com/maps/dir/?api=1&origin=47.917723, 106.923855&destination=47.932931,106.864618

    # directions from cur location:
    # https://www.google.com/maps/dir/?api=1&destination=<latitude>,<longitude>
    # https://www.google.com/maps/dir/?api=1&destination=47.932931,106.864618
    mc = MarkerCluster()

    for kid in lst:
        name = kid[5]
        lat = kid[2]
        lon = kid[4]
        url = '<a href=https://www.google.com/maps/dir/?api=1&destination={},{} target="_blank">{}</a>'.format(lat, lon, name)
        mc.add_child(folium.Marker([lat, lon], popup=url))

    map.add_child(mc)
    map.save("./templates/map.html")
    return render_template('map.html', title='Map')

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = DataCollect()
    if form.validate_on_submit():
        lat = request.form['lat']
        long = request.form['long']
        name = form.name.data
        income = form.income.data
        last_visit_date = datetime.datetime.today()

        flash('Info submitted for {} with income {} at time {} and {}, {}'.format(form.name.data, form.income.data, datetime.datetime.today().strftime('%Y-%m-%d'), lat, long))

        form = Form(key=1, name=name, income=income, last_visit_date=last_visit_date, lat=lat, lon=long)

        db.session.add(form)
        db.session.commit()

        return redirect('/forms')
    return render_template('forms.html', title='Info Form', form=form)

if __name__ == '__main__':
    app.run(debug=True)
