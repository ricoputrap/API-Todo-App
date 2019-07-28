from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_cors import CORS
import os

# init app
app = Flask(__name__)
CORS(app)

# init base path
basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # # stop it from complaining in the console 

# init db
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title):
        self.title = title

# Todo Schema
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'date_created')

# init schema
todo_schema = TodoSchema(strict=True)
todos_schema = TodoSchema(many=True, strict=True)