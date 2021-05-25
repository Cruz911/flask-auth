from .. import db
from app.main.model.blacklist import BlacklistToken
from ..config import key

class Aid(db.Model):
    """ Patient Model for storing patient related details """
    __tablename__ = "aid"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    status = db.Column(db.String(50))
    district = db.Column(db.String(50))
    no_of_patients = db.Column(db.Integer, default=1)
    
    
    def __repr__(self):
        return "<Aid '{}'>".format(self.email)