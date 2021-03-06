from flask import Flask
from app.config import DevConf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevConf)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes
from app import manage