import os
from settings import config
from flask import Flask
from flask_pymongo import PyMongo
from apis.resources import user
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    env = os.environ.get("FLASK_ENV")
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    else:
        with open(app.instance_path+"/application.cfg", "w") as conf:
            from config import DevelopmentConfig
            line = '{}="{}"\n'
            for key, value in DevelopmentConfig.fields().items():
                if isinstance(value, (bool, int)):
                    conf.write('{}={}\n'.format(key, value))
                else:
                    conf.write(line.format(key, value))
            conf.writelines([line.format(key, value) for key, value in DevelopmentConfig.fields().items()])
    if env:
        app.config.from_object(config(env))
    else:
        app.config.from_pyfile("application.cfg")
    app.register_blueprint(user)
    return app

