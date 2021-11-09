# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top
model_db = 'recipes'



class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#   Check Registration Input Correctness
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true

        if len(user['first_name']) < 2: 
            flash("First Name must be included.", category= "first_name")
            is_valid = False  #-- use different if statement for all inputs
        if len(user['last_name']) < 2: 
            flash("Last Name must be included.", category= "last_name")
            is_valid = False  #-- use different if statement for all inputs
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", category= "email")
            is_valid = False
        if len(user['password']) < 1: 
            flash("A Password must be included.", category= "password")
            is_valid = False  #-- use different if statement for all inputs
        if user['password'] != user['confirm_password']: 
            flash("Passwords do not match.", category= "confirm_password")
            is_valid = False  #-- use different if statement for all inputs
        return is_valid



    # ***CREATE***

#   Creates User from Login/Regisrtation
    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(model_db).query_db(query,data)
        return user_id
        




    # ***Retreive***

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(model_db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])






    # ***Update***







    # ***Delete***