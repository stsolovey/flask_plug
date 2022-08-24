from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




app = Flask(__name__)
app.secret_key = 'some secret salt'


UPLOAD_FOLDER = 'uploads/'
FILE_FOR_DOWNLOADING = 'uploads/1GB.zip'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FILE_FOR_DOWNLOADING'] = FILE_FOR_DOWNLOADING
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/plug_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from sweater import models, routes

db.create_all()
