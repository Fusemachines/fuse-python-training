import os

from flask import Flask
from flask_pymongo import PyMongo

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config["MONGO_URI"] = "mongodb://localhost:27017/admin"
	if test_config:
		app.config.from_mapping(test_config)
	else:
		app.config.from_pyfile("config.py", silent=True)
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route("/hello")
	def hello():
		print(app.instance_path)
		return "hello world"

	return app

