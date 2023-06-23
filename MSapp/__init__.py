from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) # this line will create the flask object
app.app_context().push() # this line will create the application context, which is needed for the db object because it is not created with the app object in this file
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280bc245' # this is the secret key for the form
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') # this line will connect flask with the database, also /// means relative path, //// means absolute path
db = SQLAlchemy(app) # this line will create the database object
migrate = Migrate(app, db) # this line will create the migration object
bcrypt = Bcrypt(app) # this line will create the bcrypt object

login_manager = LoginManager(app) # this line will create the login manager object
login_manager.login_view = 'login' # this line will set the login view to the login function
login_manager.login_message_category = 'info' # this line will set the login message category to info
login_manager.remember_cookie_duration = timedelta(seconds=3600) # this line will set the remember me cookie to expire after 30 seconds
login_manager.login_message = (u'Please log in to access this page.') # this line will set the login message to the message in the brackets

# we import routes after the app object is created because the routes module needs to import the app object
from MSapp import routes