class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite"
    SQLALCHEMY_ECHO=True