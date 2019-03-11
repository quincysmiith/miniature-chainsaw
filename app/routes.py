from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from app.forms import ProjectForm, DetailForm
from app.models import Project, LineItem

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


@app.route('/project/<project_num>', methods=['GET', 'POST'])
def create_scopes():

    project = Project.query.filtery_by(id=project_num).first_or_404()

    # need to get all lines with project_id == project_num

    form = DetailForm()
    if form.validate_on_submit():
        line = LineItem(stage=form.stage.data,
                        description=form.description.data,
                        reason=form.reason.data,
                        estimate=form.estimate.data,
                        comments=form.comments.data,
                        rate=form.rate.data,
                        project_id= project_num)
        db.session.add(line)
        db.session.commit()
        print("success")

    return render_template("createscope.html", form=form)
