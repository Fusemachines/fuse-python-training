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
    MONGODB_DB = os.environ.get("MONGODB_DB")
    MONGODB_HOST = os.environ.get("MONGODB_HOST")
    MONGODB_PORT = os.environ.get("MONGODB_PORT")
    MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
    MONGODB_CONNECT = True

    @classmethod
    def fields(self):
        return {
            "DEBUG":self.DEBUG,
            "TESTING": self.TESTING,
            "DB_HOST": self.DB_HOST,
            "DB_PORT": self.DB_PORT,
            "DB_NAME": self.DB_NAME,
            "MONGO_URI":  self.MONGO_URI,
            "MONGODB_DB" : self.MONGODB_DB,
            "MONGODB_HOST" : self.MONGODB_HOST,
            "MONGODB_PORT" : self.MONGODB_PORT,
            "MONGODB_USERNAME" : self.MONGODB_USERNAME,
            "MONGODB_PASSWORD" : self.MONGODB_PASSWORD,
            "MONGODB_CONNECT" :  self.MONGODB_CONNECT
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
    DEBUG = True
    TESTING = True
    DB_HOST = "localhost"
    DB_PORT = "27017"
    DB_NAME = "admin"
    MONGODB_DB = "admin"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    # MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
    # MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
    MONGODB_CONNECT = True


class TestingConfig(Config):
    """
    This configuration is for testing environment
    """
    DEBUG = False
    TESTING = True
    DB_HOST = "localhost"
    DB_PORT = "27017"
    DB_NAME = "test"

