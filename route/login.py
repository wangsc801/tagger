from flask import render_template, request, redirect, url_for, Blueprint
from flask_wtf import Form
from flask_login import login_user, login_required, logout_user
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, DataRequired
from service.ServUser import ServUser

login_bp = Blueprint('login_bp', __name__, template_folder='templates')


class LoginForm(Form):
    username = StringField('username', validators=[InputRequired(), Length(
        min=4, max=16), DataRequired()])
    password = PasswordField('password', validators=[InputRequired(), Length(
        min=8, max=32), DataRequired()])
    remember = BooleanField('remember')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        user = ServUser.get_by_username(form.username.data)
        USERNAME_OR_PASSWD_ERROR = 'username or password wrong.'
        if user:
            from hashlib import sha1
            sha = sha1(str(form.password.data).encode('utf-8'))
            if user.password != sha.hexdigest():
                # password did not matched
                return render_template('login.html', login_info_hint=USERNAME_OR_PASSWD_ERROR)
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            # login successfully and then go to index
            return redirect(next or url_for('index_bp.index'))
        # user does not exists
        return render_template('login.html', login_info_hint=USERNAME_OR_PASSWD_ERROR)
    # form validation error
    return render_template('login.html', form=form)


@login_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_bp.index'))
