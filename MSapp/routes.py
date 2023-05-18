from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from MSapp import app, db, bcrypt, login_manager
from MSapp.models import Great, User
from MSapp.forms import RegisterationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user

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
        if  current_user.is_authenticated:
            name = request.form.get('name')
            origin = request.form.get('origin')
            birth = request.form.get('birth')
            death = request.form.get('death')
            age = request.form.get('age')
            url = request.form.get('url')
            if name == '':
                flash('Name cannot be empty', category='info')
                return render_template('insertData.html')
            user = Great(name=name, origin=origin, birth=birth, death=death, age=age, url=url)
            db.session.add(user)
            db.session.commit()
            flash('Great human, immortilized!', category='success')
        else:
            flash('You must be logged in to insert data', category='info')
    return render_template('insertData.html')


@app.route('/integrations')
def integrations():
    return render_template('integrations.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data): # this line will check if we have a user with the username that the user entered and if the password that the user entered is correct
            if form.remember.data:
                login_user(attempted_user, remember=True)
                flash(f'Success! You are logged in as: {attempted_user.username} and you are remembered!', category='success')
                return redirect(url_for('home'))
            
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect Username or Password. Please try again.', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='success')
    return redirect(url_for('home'))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegisterationForm()
    if form.validate_on_submit(): # if the form is valid/user has submitted the form
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('You have successfully created an account!', category='success')
        return redirect(url_for('home'))
    if form.errors != {}: # if there are no errors from the validations
        for err_msg in form.errors.values(): # loop through the dictionary of errors
            flash(f'Registeration Error: {err_msg}', category='danger') # print each error message to the screen
    return render_template('signup.html', form=form)
