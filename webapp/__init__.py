import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from sqlalchemy import func
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

from webapp.config import DevConfig
from webapp.controllers.blog import blog_blueprint
from webapp.models import db, Post, Tag, tags, Comment

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    bootatrap=Bootstrap(app)

    db.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)

    return app
