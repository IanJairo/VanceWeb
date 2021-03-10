from app import app
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import NoteForm, LogInForm, SignUpForm
from app.models.tables import Note, User
from app import db, lm

from werkzeug.urls import url_parse

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        r = User(
            name=form.name.data,
            set_password = form.password.data,
            email=form.email.data)

        db.session.add(r)
        db.session.commit()

        flash("Conta Criada")
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Seja bem-vindo!")

        return redirect(url_for('notes'))

    form = LogInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user  or not user.check_password(form.password.data):
            login_user(user)
            flash("Usuário Confirmado")

            next_page = request.args.get('next')

            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('notes')
            return redirect(next_page)

        else:
            flash("Dados Invalidos")

    return render_template('login.html', form=form)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Usuário Saiu")
    return redirect(url_for("login"))


@app.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():
    user = User.query.get(current_user.id)
    notes = user.notes
    
    form = NoteForm()
    if form.validate_on_submit():
        f = Note(title=form.title.data, content=form.content.data, author=user)
        db.session.add(f)
        db.session.commit()
        return redirect(url_for("notes"))

    return render_template('notes.html', notes=notes, form=form)


