from flask import Flask, render_template, flash, redirect, request
from forms import DataCollect
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def hello():
    return "Hello World!"

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
    app.run(debug=True)
