from flask import Flask 
from flask.ext.bootstrap import Bootstrap 
from flask.ext.script import Manager 
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from settings import db_path

app = Flask(__name__)
app.secret_key = "secret"

<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////home/corina/dodo/dodo.db'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
>>>>>>> 2ba2ab0257a2718fab77aa6e3b457f0039969c49
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////home/corina/dodo/app.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

Bootstrap(app)
from app import views