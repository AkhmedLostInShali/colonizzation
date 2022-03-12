from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Department title', validators=[DataRequired()])
    chief = StringField('chief id', validators=[DataRequired()])
    members = StringField('Members (id1, id2, ...)', validators=[DataRequired()])
    email = EmailField('Mail', validators=[DataRequired()])
    submit = SubmitField('Submit')