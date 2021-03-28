from app import app
from flask import request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import NoteUpdateForm, NoteSendForm, NoteShareForm, LogInForm, SignUpForm, DeleteForm
from app.models.tables import Note, User
from app import db, lm

from werkzeug.urls import url_parse

import random


@app.route("/home/")
@app.route("/")
def home():
    return render_template('home.html')


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        r = User(
            name=form.name.data,
            email=form.email.data)
        r.set_password(form.password.data)

        confirmation = User.query.filter_by(email=form.email.data).first()

        if (confirmation == None):
            db.session.add(r)
            db.session.commit()
            flash("Conta Criada")
            return redirect(url_for('login'))

        else:
            flash("Já exite uma conta com esse e-mail!")

    return render_template('signup.html', form=form)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Seja bem-vindo!")

        return redirect(url_for('notes'))

    form = LogInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):

            login_user(user)
            flash("Usuário Confirmado")

            next_page = request.args.get('next')

            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('notes')
            return redirect(next_page)

        else:
            flash("Dados Invalidos")

    return render_template('login.html', form=form)


@app.route("/perfil/", methods=['GET', 'POST'])
@login_required
def perfil():

    user = User.query.get(current_user.id)

    token = random.randint(1000, 50000)
    user.token = token
    db.session.commit()

    return render_template('perfil.html', user=user, token=token)


@app.route("/perfil/edit", methods=['GET', 'POST'])
@login_required
def perfil_edit():

    user = User.query.get(current_user.id)
    form = SignUpForm()

    if form.validate_on_submit():
        confirmation = None
        if (form.email.data != user.email):

            confirmation = User.query.filter_by(email=form.email.data).first()

        if(confirmation == None):
            user.name = form.name.data
            user.email = form.email.data
            user.set_password(form.password.data)
            db.session.commit()
            return redirect(url_for("perfil"))

        else:
            flash("Já exite uma conta com esse e-mail!")

    return render_template('perfil-edit.html', user=user, form=form)


@app.route("/perfil/delete/<int:id>/<int:token>/", methods=['GET', 'POST'])
@login_required
def perfil_delete(id, token):

    user = User.query.get(id)

    if(user is None or token != user.token):
        return abort(404)

    notes = user.notes

    for note in notes:
        db.session.delete(note)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("login"))


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Usuário Saiu")
    return redirect(url_for("login"))


@app.route("/notes/", methods=['GET', 'POST'])
@login_required
def notes():
    user = User.query.get(current_user.id)
    notes = user.notes
    share_notes = user.notes_sh



    form = NoteSendForm()
    formUpdate = NoteUpdateForm()
    formShare = NoteShareForm()

    if formUpdate.validate_on_submit() and formUpdate.extra.data:
        id = formUpdate.extra.data
        note = Note.query.filter_by(id=id).first()
        note.title = formUpdate.title.data
        note.content = formUpdate.content.data
        db.session.commit()
  
        return redirect(url_for("notes"))

    if form.validate_on_submit():
        f = Note(title=form.title.data, content=form.content.data, author=user)
        db.session.add(f)
        db.session.commit()
       
        return redirect(url_for("notes"))

    if formShare.validate_on_submit():
        user = User.query.filter_by(email=formShare.email.data).first()

        if(user is None):
            return abort(404)

        if (user.id == current_user.id):
            flash("Essa nota já lhe pertence")
            return redirect(url_for("notes"))


        note = Note.query.get(formShare.note_id.data)

        share_note = user.notes_sh.filter_by(id=note.id).first()
      

        if share_note == None:
            user.notes_sh.append(note)
            db.session.commit()
            flash("Nota compartilhada com sucesso")

        elif (user == None or note == None):
            flash("Não existe uma conta com esse e-mail!" ) 
        
        else: 
            flash("Você já compartilhou essa nota com esse usuário")          

        return redirect(url_for("notes"))

    return render_template('notes.html', 
                                        share_notes=share_notes, 
                                        notes=notes, form=form, 
                                        formUpdate=formUpdate, 
                                        formShare=formShare
                                        )


@app.route("/notes/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def note_delete(id):
    note = Note.query.get(id)

    if(note is None):
        return abort(404)

    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes"))

# Tratamento de erros


@app.route("/notes/share/<int:id>/delete", methods=['GET', 'POST'])
@login_required
def note_share_delete(id):
    user = User.query.get(current_user.id) 
    note = Note.query.get(id)

    if(note is None):
        return abort(404)

    user.notes_sh.remove(note)
    db.session.commit()


    return redirect(url_for("notes"))

@app.route("/notes/user/<int:note_id>/<int:usr_id>/remove", methods=['GET', 'POST'])
@login_required
def note_user_remove(usr_id, note_id):
    user = User.query.get(usr_id)
    note = Note.query.get(note_id)
    if(note is None):
        return abort(404)
    user.notes_sh.remove(note)
    db.session.commit()
    return redirect(url_for("notes"))

# Trat

@app.errorhandler(404)
def not_found_error(error):
    img = url_for('static', filename='imgs/error_404.svg')
    error_desc = "Página não encontrada!"
    return render_template('error.html',
                           error_id=404,
                           error_desc=error_desc,
                           img=img), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()

    img = url_for('static', filename='imgs/error_500.svg')
    error_desc = "Erro interno do servidor!"
    return render_template('error.html',
                           error_id=500,
                           error_desc=error_desc,
                           img=img), 500
