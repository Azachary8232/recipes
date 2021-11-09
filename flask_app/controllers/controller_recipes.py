# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_recipe import Recipe
from flask_bcrypt import Bcrypt  #<---- Install to top of controller
bcrypt = Bcrypt(app)
# model_db = Sample

@app.route('/')
def index():
    return render_template('recipe_info.html')