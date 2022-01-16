from flask import Flask, render_template, request, redirect, url_for 
from werkzeug.utils import redirect
from .utils import row2dict

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from .models import Channel,db

@app.route("/")
def home():
    channel_list = []
    for channel in Channel.query.with_entities(Channel.title, Channel.description,Channel.image_url).all():
        channel_list.append(row2dict(channel,column_list=["title","description",'image_url']))
    return render_template("index.html", channel_list = channel_list)

@app.route("/<channel>")
def channel(channel):
    return render_template("channel.html", channel = row2dict(Channel.query.filter_by(title = channel).first()))

@app.route("/new_channel", methods=["POST",'GET'])
def new_channel():
    if request.method =="POST":
        channel = Channel(**request.form)
        db.session.add(channel)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_channel.html")
