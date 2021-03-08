from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class NoteForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    content = StringField('Descrição', widget=TextArea(),
                          validators=[DataRequired()])

    submit = SubmitField('Enviar')


class LogInForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class SignUpForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])

    submit = SubmitField('Enviar')

