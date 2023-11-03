from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
    
db = SQLAlchemy()
DATABASE_NAME = 'music_app.db'
DATABASE = f'sqlite:///./instance/{DATABASE_NAME}'

def make_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config['SECRET_KEY'] = "zxcvbnm"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DATABASE}'
    db.init_app(app)
    app.app_context().push()
    from bin.api import make_api
    api = make_api(app)

    with app.app_context():
        init_db()

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    from bin.api import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    return app, api


def init_db():
    from bin import api

    api.User.add_default()
    api.Role.add_default()
