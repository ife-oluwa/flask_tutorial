from flask import Flask, render_template
from .channel_dictionary import channel_dictionary
#import models

app = Flask(__name__)

# # Connect sqlalchemy to app
# models.db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html", channel_dictionary = channel_dictionary)

@app.route("/<channel>")
def channel(channel):
    return render_template("channel.html", channel=channel_dictionary[channel])
    