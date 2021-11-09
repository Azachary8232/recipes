# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt  #<---- Install to top of controller
bcrypt = Bcrypt(app)
# model_db = Sample

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/dashboard')