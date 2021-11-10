from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe


#  Create Recipe in WorkBench and send to Recipe Info
@app.route('/create_recipe', methods = ['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/new_recipe')
    user_id = session['user_id']
    data = {
        'user_id' : user_id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instruction' : request.form['instruction'],
        'created_on' : request.form['created_at'],
        'under_30' : request.form['under_30'],
    }

    Recipe.create(data)
    return redirect('/dashboard')

#  Displays a Recipe's Info
@app.route('/recipe_info/<int:id>')
def recipe_info(id):
    print("????")
    print(id)
    data = {
        'id' : id
    }
    user = User.get_one(session['user_id'])
    print("!!!!")
    print(user)

    recipe = Recipe.get_recipe(data)
    print(recipe)
    return render_template('recipe_info.html', recipe = recipe, user = user)

    #  Page for User to edit Recipe
@app.route('/edit')
def edit_recipe():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('edit_recipe.html')

@app.route('/update', methods=['POST'])
def update_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/edit')
    print("!!!!!")
    user_id = session['user_id']
    data = {
        'user_id' : user_id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instruction' : request.form['instruction'],
        'created_on' : request.form['created_at'],
        'under_30' : request.form['under_30'],
    }

    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    print(id)
    data = {
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')