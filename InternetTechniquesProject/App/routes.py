from App import app, db, login_manager
from flask import render_template, url_for, redirect, request, flash, g
from App.models import PageUser, Parameters, check_if_parameters_are_unique 
from App.forms import RegisterForm, LoginForm, ParamForm
from flask_login import login_user, logout_user, current_user

@app.route('/users')
def users_page():
    users = PageUser.query.all()
    return render_template('users.html', items = users)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = PageUser.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password_hash == form.password.data:
            login_user(attempted_user)
            flash(f'Jesteś zalogowany(a) jako: {attempted_user.username}', category = 'success')
            return redirect(url_for('fizyka_page'))
        else:
            flash('Login i/bądź hasło nieprawidłowe! Spróbuj ponownie!', category='danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('Zostałeś pomyślnie wylogowany(a)!', category='info')
    return redirect(url_for('fizyka_page'))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = PageUser(      username = form.username.data, 
                                    email = form.email_address.data, 
                                    password_hash = form.password.data  )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))

    if form.errors: 
        for err in form.errors.values():
            flash(f'Wystąpił problem podczas rejestracji nowego uśytkownika: {err}', category='danger')

    return render_template('register.html', form = form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/fizyka', methods=['GET', 'POST'])
@app.route('/fizyka/<int:sp>/<int:rd>', methods=['GET', 'POST'])
def fizyka_page(sp = 5, rd = 15):
    form = ParamForm()
    if current_user.is_authenticated:
        parameters = Parameters.query.all()
        if check_if_parameters_are_unique(current_user.get_username(), form.speed.data, form.radius.data, parameters):
            if form.validate_on_submit():
                obj_to_create = Parameters(      user = current_user.get_username(),
                                                    speed = form.speed.data,
                                                    radius = form.radius.data )
                db.session.add(obj_to_create)
                db.session.commit()
                return redirect(url_for('fizyka_page', sp = form.speed.data, rd = form.radius.data))

    if form.errors:
        for err in form.errors.values():
            flash(f'Wystąpił błąd podczas dodawania parametrów: {err}', category='danger')
    return render_template('fizyka.html', form = form, spd = sp, rds = rd)

@app.route('/fizyka/load', methods=['GET', 'POST'])
def load_page():
    parameters = Parameters.query.all()
    return render_template('load.html', items = parameters)