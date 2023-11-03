from bin import models as m
from flask_restful import Api
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from flask_restful import Resource

def make_api(app):
    api = Api(app)
    api.add_resource(User, '/user/<string:user_id>')
    return api

class User(Resource):
    def get(self, user_id):
        name = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            q = session.query(m.User).filter(m.User.user_id == user_id).first()
            try:
                name = q.user_name
            except AttributeError:
                pass
            session.commit()
        return name
    
    def set(user_name, password='password', email=''):
        q = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            new_user = m.User(user_name=user_name, password=password, email=email)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError:
                print('???')
        return q
