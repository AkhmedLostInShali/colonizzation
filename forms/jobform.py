from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SubmitField, TimeField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Job title', validators=[DataRequired()])
    team_leader = StringField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size(in hours)', validators=[DataRequired()])
    collaborators = StringField('Team (id1, id2, ...)', validators=[DataRequired()])
    is_finished = BooleanField("Is finished?", validators=[DataRequired()])
    submit = SubmitField('Submit')