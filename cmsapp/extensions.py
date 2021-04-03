from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import os
SECRET_KEY = os.urandom(32)



app = Flask(__name__ , template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGOALCHEMY_DATABASE'] = 'test'
app.config['MONGOALCHEMY_SERVER'] = 'localhost'
app.config['MONGOALCHEMY_PORT'] = '27017'
db = MongoAlchemy(app)