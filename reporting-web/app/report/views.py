from flask import Blueprint, render_template
from flask import request

report_mod = Blueprint('report', __name__)

@report_mod.route('/create/step1')
def create_report_step_1():
    datasources = {"mysql-dc-1":"MySql DataCenter 1", "vertica-dc-2" :"HP Vertica DataCenter 2"}
    return render_template('/report/create_step_1.html', ds=datasources)

@report_mod.route('/create/step2')
def create_report_step_2():
    return render_template('/report/table.html')
