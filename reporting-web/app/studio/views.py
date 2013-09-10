from flask import Blueprint, render_template
from flask import request

studio_main = Blueprint('studio main', __name__)

@studio_main.route('/<id>')
def show_template(id):
    print 'Running studio for user: ' + str(id)
    user = {}
    user['id']=id
    user['fname']='vikram'
    user['lname']='kadi'
    user['phone']='818-232-2354'
    return render_template('/studio/main.html', user=user)
