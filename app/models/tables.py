from app import db

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    email = db.Column(db.String, unique=True)

    def __init__(self, name, password, email):
        self.name = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User %e>" self.name

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(60))
    content = db.Column(db.String(60))
    data = db.Column(db.Date)



    user = db.relationship('User', db.ForeignKey('users.id'))


    def __init__(self, content, user_id, title, data):
        self.content  = content
        self.user_id = user_id
        self.title = title
        self.data = data

    
    def __repr__(self):
        return "<Post %e>" self.id