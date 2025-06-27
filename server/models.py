from config import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True,nullable=False)
    password_hash=db.Column(db.String,nullable=False)

    notes=db.relationship('Note', backref='user',lazy=True)

