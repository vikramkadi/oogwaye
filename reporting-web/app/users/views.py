from flask import Blueprint, render_template
from flask import request

users_mod = Blueprint('users', __name__)

@users_mod.route('/profiles/<id>')
def show_template(id):
    print 'looking for the user profile of : ' + str(id)
    user = {}
    user['id']=id
    user['fname']='vikram'
    user['lname']='kadi'
    user['phone']='818-232-2354'
    return render_template('/users/profile.html', user=user)
