from flask_app.controllers import controller_user  #<--- Add all contoller pages 
from flask_app.controllers import controller_recipe
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)