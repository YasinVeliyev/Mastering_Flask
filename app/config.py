class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConf(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True