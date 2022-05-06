from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PhotoForm(FlaskForm):
    photo = FileField('Upload photo', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('submit')