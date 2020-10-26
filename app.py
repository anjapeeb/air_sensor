from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Particles

#MAIN HOME PAGE 
@app.route("/")
def hello():
    return "Testing Flask app is working"

#PAGE ROUTES - TO BE EDITED FOR OWN PROJECT

if __name__ == '__main__':
    app.run()