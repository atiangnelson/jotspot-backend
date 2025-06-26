from config import app, db
from models import User, Note 

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username='demo')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()






