from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DATABASE_NAME = 'music_app.db'
DATABASE = f'sqlite:///./database/{DATABASE_NAME}'

def make_app():
    app = Flask(__name__)   
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DATABASE}'
    db.init_app(app)
    from bin.api import make_api
    api = make_api(app)

    with app.app_context():
        init_db()

    return app, api


def init_db():
    # Create a test user
    from bin import api

    api.User.set(user_name='default_user')