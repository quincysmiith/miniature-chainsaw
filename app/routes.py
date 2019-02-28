from app import app, db
from flask import render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from app.forms import ProjectForm
from app.models import Project

Bootstrap(app)


@app.route('/newproject/', methods=['GET', 'POST'])
def new_project():

    form = ProjectForm()

    if form.validate_on_submit():
        project = Project(name=form.name.data, client=form.client.data)
        db.session.add(project)
        db.session.commit()

    return render_template("newproject.html", form=form)
