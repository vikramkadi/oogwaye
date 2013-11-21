from flask import Blueprint, render_template, redirect
from flask import request, session
from app.users import security

users_mod = Blueprint('users', __name__)

@users_mod.route('/login', methods=['GET'])
def login_screen():
	return render_template('/users/login.html', message="Enter email/password to access")

@users_mod.route('/login', methods=['POST'])
def login():
	(result, reason, user_rec) = security.check_auth(request)
	if result:
		session['user'] = user_rec
		if 'redirect_url' in request.form:
			return redirect(request.form['redirect_url'])
		else:
			return redirect('/report/create/step1')
	else:
		return render_template('/users/login.html', message=reason)

@users_mod.route('/logout', methods=['GET'])
def logout():
	session.clear()
	return render_template('/users/login.html', message="You have been successfully logged out")