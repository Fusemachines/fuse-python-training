class Config:
    """
    Base class for all config.
    This class will be the configuration for stating environment
    """
    DEBUG=False
    TESTING=False
    DB_HOST = "127.0.0.1"
    DB_PORT = "27017"
    DB_NAME = "admin"

    @property
    def MONGO_URI(self):         # Note: all caps
        return f'mongodb://{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

class ProductionConfig(Config):
    """
    This configuration is for production environment
    """
    pass

class DevelopmentConfig(Config):
    """
    This configutation is for development environment
    """
    DEBUG = False
    DB_HOST = "localhost"

class TestingConfig(Config):
    """
    This configuration is for testing environment
    """
    DEBUG = False
    DB_HOST = "localhost"
    DB_PORT = "27017"
    DB_NAME = "test"

