from functools import wraps
from flask import session, render_template
import json

users={}
roles={}

def init(f):
    global users
    global roles
    with open(f) as dsfile:
        cred_store = json.load(dsfile)
        users = init_users(cred_store['users'])
        roles = init_roles(cred_store['roles'])

def init_users(store):
    users = {}
    for rec in store:
        if 'email' in rec:
            users[rec['email']] = rec
    print(str(users))
    return users 

def init_roles(store):
    roles = {}
    for rec in store:
        if 'id' in rec:
            roles[rec['id']] = rec
    print(str(roles))

def check_auth(request):
    if not all(param in request.form for param in ['user', 'passwd']):
        return (False, "Please provide both user and password", None)

    result, user_rec = valid_user(request.form['user'], request.form['passwd'])
    return (result, '' if result else 'Invalid user/pwd combination', user_rec)

def valid_user(user, pwd):
    if user in users:
        valid_login = users[user]['password'] == pwd
        return (valid_login, users[user] if valid_login else None)
    return (False, None)

def send_to_authenticate():
    return render_template('/users/login.html', message="please login to proceed")

def logged_in():
    if 'user' in session:
        return True
    return False

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not logged_in():
            return send_to_authenticate()
        return f(*args, **kwargs)
    return decorated