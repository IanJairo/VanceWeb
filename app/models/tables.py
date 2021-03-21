from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    password_hash = db.Column(db.String(180))
    email = db.Column(db.String, unique=True)

    notes = db.relationship('Note', backref='author', lazy='dynamic')

    # Password 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



    # Login
    @property
    def is_authenticated(self):
        return True  
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
  
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.name


class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(60))
    content = db.Column(db.String(100))
    data = db.Column(db.Date(), default=datetime.today())
    # user = db.relationship('User', db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Note %r>' % self.id
