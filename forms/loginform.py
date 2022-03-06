from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astro = StringField('id астронавта', validators=[DataRequired()])
    pass_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    pass_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')