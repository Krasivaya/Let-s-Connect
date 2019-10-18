from flask import render_template,flash, request, redirect, url_for
from app.auth import auth
from app.models import User
from .forms import RegistrationForm


@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password=form.password.data)
        user.save()
        flash('Your account has been created successful')
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/signup.html',registration_form=form )