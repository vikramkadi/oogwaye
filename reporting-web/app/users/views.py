from flask import Blueprint, render_template, redirect
from flask import request, session
from app.users import security

users_mod = Blueprint('users', __name__)

@users_mod.route('/login', methods=['POST'])
def login():
	(result, reason) = security.check_auth(request)
	if result:
		session['user'] = {"name":"vikram"}	
		if 'redirect_url' in request.form:
			return redirect(request.form['redirect_url'])
		else:
			return redirect('/report/create/step1')
	else:
		return render_template('/users/login.html', message=reason)

@users_mod.route('/logout', methods=['GET'])
def logout():
	session['user'] = None
	return render_template('/users/login.html', message="You have been successfully logged out")