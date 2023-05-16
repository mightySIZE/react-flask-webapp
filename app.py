from flask import Flask, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # this line will create the flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MS.db' # this line will connect flask with the database, also /// means relative path, //// means absolute path
db = SQLAlchemy(app) # this line will create the database object
migrate = Migrate(app, db) # this line will create the migration object

# this class will create the table in the database
class Great(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    birth = db.Column(db.String(80), unique=False, nullable=False)
    death = db.Column(db.String(80), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    url = db.Column(db.String(200), unique=True, nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    greats = [
        {'id': 1, 'name': 'Alexander the Great', 'origin': 'Macedonia', 'birth': '356 BC', 'death': '323 BC', 'age': '32', 'url': 'https://en.wikipedia.org/wiki/Alexander_the_Great'},
        {'id': 2, 'name': 'Julius Caesar', 'origin': 'Rome', 'birth': '100 BC', 'death': '44 BC', 'age': '56', 'url': 'https://en.wikipedia.org/wiki/Julius_Caesar'},
        {'id': 3, 'name': 'Napoleon Bonaparte', 'origin': 'France', 'birth': '1769 AD', 'death': '1821 AD', 'age': '51', 'url': 'https://en.wikipedia.org/wiki/Napoleon'},
        {'id': 4, 'name': 'Genghis Khan', 'origin': 'Mongolia', 'birth': '1162 AD', 'death': '1227 AD', 'age': '65', 'url': 'https://en.wikipedia.org/wiki/Genghis_Khan'},
        {'id': 5, 'name': 'Hannibal Barca', 'origin': 'Carthage', 'birth': '247 BC', 'death': '183 BC', 'age': '64', 'url': 'https://en.wikipedia.org/wiki/Hannibal'},
        {'id': 6, 'name': 'Attila the Hun', 'origin': 'Hungary', 'birth': '406 AD', 'death': '453 AD', 'age': '47', 'url': 'https://en.wikipedia.org/wiki/Attila'},
    ]

    return render_template('data.html', greats=greats)

@app.route('/integrations')
def integrations():
    return render_template('integrations.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    # if request.method == 'POST':
    #     # if valid_login(request.form['username'],
    #     #                request.form['password']):
    #     #     return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    # if request.method == 'POST':
    #     # if valid_login(request.form['username'],
    #     #                request.form['password']):
    #     #     return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    return render_template('signup.html', error=error)

# tests the functions, outside of the web server
#with app.test_request_context():
    #print(url_for('index'))
    #print(url_for('login'))
    #print(url_for('login', next='/'))
    #print(url_for('profile', username='John Doe'))
    #url_for('index', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True)