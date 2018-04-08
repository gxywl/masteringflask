import os


class Config(object):
    SECRET_KEY = 'yourpwd'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.sqlite")
    #SQLALCHEMY_DATABASE_URI = "sqlite://" + path.join(path.pardir, "database.sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
