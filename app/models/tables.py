from app import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    email = db.Column(db.String, unique=True)

    notes = db.relationship('Note', backref='author', lazy='dynamic')

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
        return '<Note {} ({})>'.format(self.title, self.content)
