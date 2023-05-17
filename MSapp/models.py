from MSapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

class Great(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    birth = db.Column(db.String(80), unique=False, nullable=False)
    death = db.Column(db.String(80), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    url = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return '<Great %r>' % self.name

# how to delete all data from a table
# >>> python
# >>> from MSapp import models
# >>> from MSapp.models import User, Great
# >>> from MSapp import db

### for all records ###
# >>> db.session.query(User).delete()
# 1
# >>> db.session.

### for specific records ###
# >>> db.session.query(User).filter(User.id == 1).delete()
# >>> db.session.commit()