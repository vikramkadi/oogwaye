from flask import Blueprint, render_template

users_mod = Blueprint('users', __name__)

@users_mod.route('/<page>')
def show_template(page):
    print 'looking for ' + page
    return render_template('/users/' + str(page))