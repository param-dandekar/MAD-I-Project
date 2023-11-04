from bin import models as m
from bin import errors as e
from flask_restful import Api, Resource, fields, marshal_with
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from flask_restful import Resource

def make_api(app):
    api = Api(app)
    api.add_resource(User, '/user/<string:user_id>', methods=["GET", "POST"])
    return api

user_fields = {
    'user_name': fields.String,
    'user_id': fields.Integer,
    'role_id': fields.Integer,
    'password': fields.String,
    'email': fields.String,
    'profile_photo': fields.String,
    'about_me': fields.String,
}
class User(Resource):
    # @marshal_with(user_fields)
    def get(user_id):
        user = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            q = session.query(m.User).filter(m.User.user_id == user_id)
            return q.first()
    
    def is_admin(user):
        print(Role.get(user.role_id))
        if Role.get(user.role_id) == 'admin':
            return True
        return False

    def add_default():
        q = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            new_user = m.User()
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError:
                e.default_already_created_warning('user')
                session.rollback()
        return q
    
    def add(user_name, password, email):
        q = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            new_user = m.User(user_name=user_name, password=password, email=email)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError:
                e.already_exists_error(user_name, 'user_name', 'user')
                session.rollback()
        return 201
    
class Role(Resource):
    def get(role_id):
        role_name = None
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            role_name = session.query(m.Role).filter(m.Role.role_id == role_id).first().role_name
            session.commit()
        return role_name
    
    def add_default():
        new_role_created = False
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            for role in (roles := m.Role.roles):
                role = m.Role(role_id=role, role_name=roles[role])
                session.add(role)
                try:
                    session.commit()
                    new_role_created = True
                except IntegrityError:
                    e.default_already_created_warning('role')
                    session.rollback()
        if new_role_created: return 201
        return 200
    
    def set(user_id, role_id):
        if role_id not in m.Role.role_ids:
            e.invalid_parameter_error(role_id, 'role_id')
        with Session(m.engine, autoflush=False) as session:
            session.begin()
            user = session.query(m.User).filter(m.User.user_id == user_id).first()
            user.role_id = role_id
            try:
                session.commit()
            except IntegrityError:
                print('Username is taken!')
                session.rollback()
        return 200