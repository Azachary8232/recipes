from types import ModuleType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
model_db = 'recipes'


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instruction = data['instruction']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#   Validate Recipe Creation Data
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True 

        if len(recipe['name']) < 1: 
            flash("Recipe name must be included.", category= "recipe_name")
            is_valid = False  
        if len(recipe['description']) < 1: 
            flash("A recipe description must be included.", category= "recipe_description")
            is_valid = False  
        if len(recipe['instruction']) < 1: 
            flash("Your recipe's instructions must be included.", category= "recipe_instruction")
            is_valid = False  
        if len(recipe['created_at']) < 1: 
            flash("You must include a date.", category= "recipe_date")
            is_valid = False
        if recipe['under_30'] == '0': 
            flash("Please declare prep time.", category= "under_30")
            is_valid = False

        return is_valid




# Create

    @classmethod
    def create(cls,data):
        query = "INSERT INTO recipes (name, description, under_30, instruction, user_id) VALUES (%(name)s, %(description)s, %(under_30)s, %(instruction)s, %(user_id)s);"
        recipe_id = connectToMySQL(model_db).query_db(query,data)
        return recipe_id

# Retreive

    @classmethod
    def get_recipe(cls,data):
        query = 'SELECT * FROM recipes WHERE recipes.id = %(id)s;'
        result = connectToMySQL(model_db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(model_db).query_db(query)
        return results


# Update

    @classmethod
    def update(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_30 = %(under_30)s WHERE id = %(id)s';
        connectToMySQL(model_db).query_db(query, data)
        return print("Update Successful")


# Delete

    @classmethod
    def delete(cls,data):
        query = 'DELETE FROM recipes WHERE id = %(id)s';
        connectToMySQL(model_db).query_db(query, data)
        return print("Delete Successful")