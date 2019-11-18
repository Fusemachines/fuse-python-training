from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig

def config(env="dev"):
    if env=="dev":
        return DevelopmentConfig
    if env == "prod":
        return ProductionConfig
    if env == "testing":
        return TestingConfig
    if env == "staging":
        return Config
   
