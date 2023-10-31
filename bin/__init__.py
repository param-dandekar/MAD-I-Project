from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DATABASE_NAME = "music_app.db"

def make_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    db.init_app(app)



    return app

