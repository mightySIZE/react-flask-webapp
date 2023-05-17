from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from MSapp import app, db, bcrypt
from MSapp.models import Great, User
from MSapp.forms import RegisterationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def viewData(): # this function will show the data from the database
    greats = Great.query.all()
    return render_template('viewData.html', greats=greats)

@app.route('/insertData', methods=['POST', 'GET'])
def insertData(): # this function will insert data into the database
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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Here you should validate the username and password against your user database.
        # For the sake of simplicity, let's assume we have a single user with username 'admin'
        # and hashed password '$2b$12$7.b1.wWY0UJjBoziSMERqOjG2v29xG.AYFJ23wWUUTLRYE1pBChhO'.
        # You would normally fetch the user's hashed password from your database.
        if username == 'admin':
            hashed_password = '$2b$12$7.b1.wWY0UJjBoziSMERqOjG2v29xG.AYFJ23wWUUTLRYE1pBChhO'
            if bcrypt.check_password_hash(hashed_password, password):
                # Password is correct, redirect to the home page or any other page.
                return redirect(url_for('home'))
            else:
                # Password is incorrect, show an error message.
                error = 'Invalid username or password'
                return render_template('login.html', error=error)

    # If the request method is GET or the login attempt was unsuccessful, show the login form.
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegisterationForm()
    if form.validate_on_submit(): # if the form is valid/user has submitted the form
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}: # if there are no errors from the validations
        for err_msg in form.errors.values(): # loop through the dictionary of errors
            flash(f'Registeration Error: {err_msg}', category='danger') # print each error message to the screen
    return render_template('signup.html', form=form)