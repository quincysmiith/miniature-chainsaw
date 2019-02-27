from app import app


@app.route('/newproject/')
def new_project():
    return "Hello World"
