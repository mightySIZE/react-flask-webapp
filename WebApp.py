from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/integrations')
def integrations():
    return render_template('integrations.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return # do_the_login()
    else:
        return # show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# tests the functions, outside of the web server
#with app.test_request_context():
    #print(url_for('index'))
    #print(url_for('login'))
    #print(url_for('login', next='/'))
    #print(url_for('profile', username='John Doe'))
    #url_for('index', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True)