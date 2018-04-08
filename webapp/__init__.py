import datetime
import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from sqlalchemy import func
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

from webapp.config import DevConfig
from webapp.controllers.admin import CustomModelView, CustomFileAdmin
from webapp.controllers.blog import blog_blueprint
from webapp.extensions import bootatrap, admin
from webapp.models import db, Post, Tag, tags, Comment, User


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)


    bootatrap.init_app(app)
    db.init_app(app)
    admin.init_app(app)

    models=[User,Post,Comment,Tag]
    for model in models:
        admin.add_view(CustomModelView(model,db.session,category='models'))

    admin.add_view(CustomFileAdmin(os.path.join(os.path.dirname(__file__),'static'),'/static/',name="Static Files"))

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)

    return app
