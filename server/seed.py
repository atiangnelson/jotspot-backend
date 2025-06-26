from config import app, db
from models import User, Note 

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username='demo')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

    note = Note(title='Welcome', content='This is your first note!', tags='welcome,first', user_id=user.id)
    db.session.add(note)
    db.session.commit()


    print('Database seeded!')





