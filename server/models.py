from config import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True,nullable=False)
    password_hash=db.Column(db.String,nullable=False)

    notes=db.relationship('Note', backref='user',lazy=True)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    serialize_rules = ('-password_hash','-notes.user',)    


 class Note(db.Model,SerializerMixin):
    __tablename_ = 'notes'

    id = db.Columm(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    content=db.Column(db.Text,nullable=False)
    tags=db.Column(db.String)

    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    serialize_rules=('-user')       

        

