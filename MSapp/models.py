from MSapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    great = db.relationship('Great', backref='great_user', lazy=True)

class Great(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    origin = db.Column(db.String(80), unique=False, nullable=False)
    birth = db.Column(db.String(80), unique=False, nullable=False)
    death = db.Column(db.String(80), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    url = db.Column(db.String(200), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Great %r>' % self.name