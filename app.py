from flask import Flask
from flask import render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
