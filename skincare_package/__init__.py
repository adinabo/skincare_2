from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)  # initialize app as package
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

from skincare_package import routes 
