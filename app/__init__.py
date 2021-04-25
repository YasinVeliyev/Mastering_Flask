from flask import Flask
from app.config import DevConf

app = Flask(__name__)
app.config.from_object(DevConf)


from app import routes