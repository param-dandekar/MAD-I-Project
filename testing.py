from flask import Flask
from bin import db
from bin.models import User, engine
from sqlalchemy.orm import Session

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///music_app.db'
db.init_app(app)
    
    
with app.app_context():
    db.create_all()
    
q = 0
with Session(engine, autoflush=False) as session:
    session.begin()
    print('aaa')
    q = session.query(User).all()
    # q = session.query(m.User).filter(m.User.user_id == user_id).first()
    session.commit()
print(q)