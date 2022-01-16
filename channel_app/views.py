from flask import Flask, render_template
from .channel_dictionary import channel_dictionary

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route("/")
def home():
    return render_template("index.html", channel_dictionary = channel_dictionary)

@app.route("/<channel>")
def channel(channel):
    return render_template("channel.html", channel=channel_dictionary[channel])
    