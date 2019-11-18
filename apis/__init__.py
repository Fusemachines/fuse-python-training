import os
from settings import config
from flask import Flask
from flask_pymongo import PyMongo

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	env = os.environ.get("FLASK_ENV")
	# app.config["MONGO_URI"] = "mongodb://localhost:27017/admin"
	if env:
		app.config.from_object(config(env))
		print(app.config["DB_NAME"])
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route("/hello")
	def hello():
		print(app.instance_path)
		return "hello world"

	return app

