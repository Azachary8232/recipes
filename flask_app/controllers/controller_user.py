# all @app.route() functions

import re
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt  #<---- Install to top of controller
bcrypt = Bcrypt(app)
# model_db = Sample

@app.route('/')
def index():
    return render_template('login.html')


# User Registration
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create(data)
    print(user_id)
    session['user_id'] = user_id
    print(session['user_id'])
    return redirect('/dashboard')

# Login Verification
@app.route('/login', methods=['POST'])
def login():
    data = { 
        "email" : request.form["email"]
        }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email", category= "login_email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password", category= "login_password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")


#  Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    person = User.get_one(data)
    recipes = Recipe.get_all_recipes()
    print(recipes)
    return render_template('dashboard.html', recipes = recipes, user = person)


#  Logout
@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')

#  User Add New Recipe
@app.route('/new_recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    id = session['user_id']

    return render_template('new_recipe.html')

