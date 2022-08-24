from datetime import datetime

from flask_login import UserMixin

from sweater import db, manager, ALLOWED_EXTENSIONS


class Sentence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, translations):
        self.text = text.strip()
        self.translations = [
            Translation(text=translation.strip()) for translation in translations.split(',')
        ]


class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'), nullable=False)
    sentence = db.relationship('Sentence', backref=db.backref('translations', lazy=True))


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
def current_datetime_as_string():
    now = datetime.now()
    date_time = now.strftime("%Y%d%m-%H%M%S_")
    return date_time