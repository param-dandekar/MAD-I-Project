import flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DATABASE_NAME = "music_app.db"


def make_app():
    app = flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    db.init_app(app)

    