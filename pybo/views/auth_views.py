import functools

from flask import Blueprint, url_for, render_template, flash, request, session, g
from sqlalchemy.sql.expression import null
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from .. import db
from ..forms import UserCreateForm, UserLoginForm, UserProfileForm
from ..models import User

import logging
import sys

from datetime import datetime

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data,
                        create_date= datetime.now(),  # 수정일시 저장
                        modify_date= datetime.now()
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.route('/profile/', methods=('GET', 'POST'))
def profile():
    form = UserProfileForm()

    if request.method == 'POST':  
        user = User.query.filter_by(username=g.user.username).first()
        
        if not user:
            error = "존재하지 않는 사용자입니다!!" + form.username.data
        else:
            if(form.password1.data is not None):
                user.password = generate_password_hash(form.password1.data)

            if(form.email.data is not None):
                user.email = form.email.data

            user.modify_date= datetime.now()
            db.session.commit()
            return redirect(url_for('question._list'))
        flash(error)
    return render_template('auth/profile.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        

        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            #return redirect(url_for('main.index'))
            return redirect(url_for('question._list'))
        flash(error)
    return render_template('auth/login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
