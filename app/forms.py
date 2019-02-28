from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo


class ProjectForm(FlaskForm):
    name = StringField("Project Name", validators=[DataRequired()])
    client = StringField("Client Name", validators=[DataRequired()])
