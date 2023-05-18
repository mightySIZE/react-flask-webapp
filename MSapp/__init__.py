from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__) # this line will create the flask object
app.app_context().push() # this line will create the application context, which is needed for the db object because it is not created with the app object in this file
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280bc245' # this is the secret key for the form
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/mo/Desktop/Flask-practice-website-for-learning/MSapp/instance/MS.db' # this line will connect flask with the database, also /// means relative path, //// means absolute path
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=3600) # this line will set the remember me cookie to expire after 30 seconds
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=3600) # this line will set the session to expire after 30 seconds
db = SQLAlchemy(app) # this line will create the database object
migrate = Migrate(app, db) # this line will create the migration object
bcrypt = Bcrypt(app) # this line will create the bcrypt object
login_manager = LoginManager(app) # this line will create the login manager object
login_manager.login_view = 'login' # this line will set the login view to the login function
login_manager.login_message_category = 'info' # this line will set the login message category to info

# we import routes after the app object is created because the routes module needs to import the app object
from MSapp import routes