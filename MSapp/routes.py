from flask import request, render_template
from MSapp import app, db
from MSapp.models import Great

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def viewData():
    greats = Great.query.all()

    return render_template('viewData.html', greats=greats)

@app.route('/insertData', methods=['POST', 'GET'])
def insertData():
    if request.method == 'POST':
        name = request.form.get('name')
        origin = request.form.get('origin')
        birth = request.form.get('birth')
        death = request.form.get('death')
        age = request.form.get('age')
        url = request.form.get('url')
        user = Great(name=name, origin=origin, birth=birth, death=death, age=age, url=url)
        db.session.add(user)
        db.session.commit()
    return render_template('insertData.html')


@app.route('/integrations')
def integrations():
    return render_template('integrations.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

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
