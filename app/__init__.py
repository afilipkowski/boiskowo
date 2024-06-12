from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

boiskowo = Flask(__name__)
boiskowo.config.from_object(Config)
db = SQLAlchemy(boiskowo)
migrate = Migrate(boiskowo, db)

from app import routes, models