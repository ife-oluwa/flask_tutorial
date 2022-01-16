from flask_sqlalchemy import SQLAlchemy

from main import app

# Create database connection object
db = SQLAlchemy(app)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False) 
    url = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(200), nullable=True)
    subjects = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)


    def __init__(self, title, url, language=None, subjects=None, image_url=None):
        self.title = title
        self.description = description
        self.url = url
        self.language = language
        self.subjects = subjects
        self.image_url = image_url

db.create_all()

