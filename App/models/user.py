from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False,unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    programme_id = db.Column(db.Integer, db.foreign_key('programme.id'))
    graduation_year = db.Column(db.Integer, nullable=False)
    facebook_id = db.Column(db.String, nullable=False)
    instagram_id = db.Column(db.String, nullable=False)
    linkedin_id = db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

