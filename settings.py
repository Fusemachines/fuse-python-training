from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig
import dotenv
def config(env="development"):
    dotenv.load_dotenv()
    if env == "development":
        return DevelopmentConfig
    if env == "production":
        return ProductionConfig
    if env == "testing":
        return TestingConfig
    if env == "staging":
        return Config
   
