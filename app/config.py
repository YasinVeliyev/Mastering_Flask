class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConf(Config):
    debug = True