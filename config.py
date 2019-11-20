import os
class Config:
    """
    Base class for all config.
    This class will be the configuration for stating environment
    """
    DEBUG=False
    TESTING=False
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    MONGO_URI = f'mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}'

    @classmethod
    def fields(self):
        return {
            "DEBUG":self.DEBUG,
            "TESTING": self.TESTING,
            "DB_HOST": self.DB_HOST,
            "DB_PORT": self.DB_PORT,
            "DB_NAME": self.DB_NAME,
            "MONGO_URI":  self.MONGO_URI
        }

class ProductionConfig(Config):
    """
    This configuration is for production environment
    """
    pass

class DevelopmentConfig(Config):
    """
    This configutation is for development environment
    """
    ENV = 'developement'
    DEBUG = True
    TESTING = True
    DB_HOST = "localhost"
    DB_PORT = "27017"
    DB_NAME = "admin"
    ENV = "developement"


class TestingConfig(Config):
    """
    This configuration is for testing environment
    """
    DEBUG = False
    TESTING = True
    DB_HOST = "localhost"
    DB_PORT = "27017"
    DB_NAME = "test"

