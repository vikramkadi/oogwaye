from flask import Blueprint, render_template

report_mod = Blueprint('report', __name__)

@report_mod.route('/<page>')
def show_template(page):
    print 'looking for ' + page
    return render_template('/report/' + str(page))

