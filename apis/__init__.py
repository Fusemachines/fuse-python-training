import os
from settings import config
from flask import Flask
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    env = os.environ.get("FLASK_ENV")
    
    try:
        os.makedirs(app.instance_path)
        print("create folder")
    except OSError:
        if env:
            app.config.from_object(config(env))
        else:
            app.config.from_pyfile("application.cfg")
    else:
        with open(app.instance_path+"/application.cfg", "w") as conf:
            from config import DevelopmentConfig
            conf.writelines([f"{key}={value}\n" for key, value in DevelopmentConfig.fields().items()])


    @app.route("/hello")
    def hello():
        print(app.instance_path)
        return "hello world"

    return app

