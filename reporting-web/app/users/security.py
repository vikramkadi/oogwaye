from functools import wraps
from flask import session, render_template

def check_auth(request):
    if not all(param in request.form for param in ['user', 'passwd']):
        return (False, "Please provide both user and password")

    result = request.form['user'] == 'admin' and request.form['passwd'] == 'secret'
    return (result, '' if result else 'Invalid user/pwd combination')

def send_to_authenticate():
    return render_template('/users/login.html', message="please login to proceed")

def logged_in():
    if 'user' in session:
        return True
    return False

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print 'login check called'
        if not logged_in():
            return send_to_authenticate()
        return f(*args, **kwargs)
    return decorated