from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from app.forms import ProjectForm, DetailForm
from app.models import Project

Bootstrap(app)


@app.route('/newproject/', methods=['GET', 'POST'])
def new_project():

    form = ProjectForm()

    if form.validate_on_submit():
        project = Project(name=form.name.data, client=form.client.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('create_scopes'))
    else:
        print("Form submission failed")
        flash("Failed to submit data")

    return render_template("newproject.html", form=form)


@app.route('/createscopes/', methods=['GET', 'POST'])
def create_scopes():

    form = DetailForm()
    if form.validate_on_submit():
        print("success")

    return render_template("createscope.html", form=form)
