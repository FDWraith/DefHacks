import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.urandom(24)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
