from app import app
from flask_bootstrap import Bootstrap

Bootstrap(app)


@app.route('/newproject/')
def new_project():
    return "Hello World"
