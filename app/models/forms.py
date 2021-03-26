from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class NoteUpdateForm(FlaskForm):
    extra = StringField(6, validators=[DataRequired()])
    title = StringField('Título', validators=[DataRequired()])
    content = StringField('Descrição', widget=TextArea(),
                          validators=[DataRequired()])

    submit = SubmitField('Enviar')

class NoteSendForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    content = StringField('Descrição', widget=TextArea(),
                          validators=[DataRequired()])

    submit = SubmitField('Enviar')

class NoteShareForm(FlaskForm):
    role = SelectField('Cargo', choices=[
        (1, 'Editor'), 
        (2, 'Leitor')])
    email = StringField('Email do usuário', validators=[DataRequired()])
    note_id = StringField(6, validators=[DataRequired()])

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


class DeleteForm(FlaskForm):
    submit = SubmitField('Excluir')
