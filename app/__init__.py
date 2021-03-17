
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')  

import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists("logs"):
    os.mkdir("logs")
archive_handler = RotatingFileHandler("logs/errors.log", maxBytes=100000, backupCount=10)
archive_handler.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s [em %(pathname)s:%(lineno)d]"))
archive_handler.setLevel(logging.WARNING)
app.logger.addHandler(archive_handler)
app.logger.setLevel(logging.INFO)
app.logger.info("Aplicação inicializada!")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app.models import tables, forms
from app.controllers import default
