from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig
import dotenv
def config(env="dev"):
    dotenv.load_dotenv()
    if env=="dev":
        return DevelopmentConfig
    if env == "prod":
        return ProductionConfig
    if env == "testing":
        return TestingConfig
    if env == "staging":
        return Config
   
