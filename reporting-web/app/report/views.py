import flask
import jsonpickle
from flask import Blueprint, render_template
from flask import request
from flask import jsonify
"""
from app.report import datasources
from app.report import dbhelper
"""

report_mod = Blueprint('report', __name__)

@report_mod.route('/create/step1')
def create_report_step_1():
    print datasources.datasources
    return render_template('/report/create_step_1.html', ds=datasources.datasources)

@report_mod.route('/create/step2')
def create_report_step_2():
    return render_template('/report/table.html')

@report_mod.route('/create/step3')
def create_report_step_3():
    return render_template('/report/main2.html')

"""
@report_mod.route('/create/step2/start', methods=["GET","POST"])
def create_report_step2_start():
    #result = dbhelper.pull_from_db(request.form['datasource'], request.form['sql'])
    #resp_body = jsonpickle.encode(result, unpicklable=False)
    return render_template('/report/table.html', sql=request.form['sql'], datasource=request.form['datasource'])

@report_mod.route('/create/step2/pulldata', methods=["GET", "POST"])
def create_report_step2_pulldata():
    result = dbhelper.pull_from_db(request.form['datasource'], request.form['sql'])
    resp_body = jsonpickle.encode(result, unpicklable=False)
    return flask.Response(resp_body, mimetype='application/json')
"""
