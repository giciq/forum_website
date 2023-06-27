from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/contact', methods=['GET', 'POST'])
@auth.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if request.form.get('username'):
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()
            username_base = User.query.filter_by(first_name=username).first()


            if username_base:
                flash('Username is already used!', category='error')
            elif user:
                flash('Email is already in use!', category='error')
            elif len(password) < 8:
                flash('Password must be at least 8 characters.', category='error')
            else:
                new_user = User(email=email, first_name=username, password=generate_password_hash(password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account has been created!', category='success')
                return redirect(url_for('views.home'))
        else:
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('You have logged in!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('It is a wrong password!', category='error')
            else:
                flash('Email does not exist!', category="error")
    if request.path == '/':
        return render_template("main.html", user=current_user)
    else:
        return render_template("contact.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.main'))
