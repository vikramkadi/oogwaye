from flask import Flask, render_template
from app.users.views import users_mod
from app.report.views import report_mod

app = Flask(__name__)
app.register_blueprint(users_mod, url_prefix='/users')
app.register_blueprint(report_mod, url_prefix='/report')

