from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
from wtforms.validators import DataRequired, ValidationError


class ProjectForm(FlaskForm):
    name = StringField("Project Name", validators=[DataRequired()])
    client = StringField("Client Name", validators=[DataRequired()])
    submit = SubmitField("Submit New Project")


class DetailForm(FlaskForm):
    stage = StringField("Stage Number", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    reason = StringField("Reason")
    estimate = DecimalField("Estimated Hours", validators=[DataRequired()])
    comments = StringField("Additional Comments")
    rate = DecimalField("Hourly Rate ($)", validators=[DataRequired()])
    submit = SubmitField("Add task to project")
