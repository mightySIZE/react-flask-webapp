from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # this line will create the flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/mo/Desktop/current project/MSapp/instance/MS.db' # this line will connect flask with the database, also /// means relative path, //// means absolute path
db = SQLAlchemy(app) # this line will create the database object
migrate = Migrate(app, db) # this line will create the migration object
app.debug = True

from MSapp import routes