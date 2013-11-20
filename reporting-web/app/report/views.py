import flask
import jsonpickle
from flask import Blueprint, render_template
from flask import request
from flask import jsonify
from app.report import datasources, dbhelper, helper
from app.users import security
from app.services import mongo

report_mod = Blueprint('report', __name__)

@report_mod.route('/create/step1')
@security.requires_auth
def create_report_step_1():
    print datasources.datasources
    return render_template('/report/create_step_1.html', ds=datasources.datasources)

@report_mod.route('/create/step2')
def create_report_step_2():
    return render_template('/report/table.html')

@report_mod.route('/create/step3')
def create_report_step_3():
    return render_template('/report/main2.html')

@report_mod.route('/create/step2/start', methods=["GET","POST"])
def create_report_step2_start():
    return render_template('/report/table.html', sql=request.form['sql'], datasource=request.form['datasource'])

@report_mod.route('/create/step2/pulldata', methods=["GET", "POST"])
def create_report_step2_pulldata():
    result = dbhelper.pull_from_db(request.form['datasource'], request.form['sql'])
    resp_body = jsonpickle.encode(result, unpicklable=False)
    return flask.Response(resp_body, mimetype='application/json')

@report_mod.route('/create/save', methods=["POST"])
def save_report():
	print request.json
	result, reason = helper.upsert_report(request.json)
	response = {}
	if result == True:
		response['code'] = 0
		response['report_id'] = reason
	else:
		response['code'] = -1
		response['message'] = reason
	resp_body = jsonpickle.encode(response, unpicklable=False)
	return flask.Response(resp_body, mimetype='application/json')
