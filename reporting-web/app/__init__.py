from flask import Flask, render_template
from app.users.views import users_mod
from app.report.views import report_mod
import os
import settings
from app.report import datasources

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(users_mod, url_prefix='/users')
app.register_blueprint(report_mod, url_prefix='/report')

def initialize(config):
    base_dir = config.base_dir
    if os.path.exists(os.path.join(base_dir,config.datasources_store)):
        datasources.init_datasources(os.path.join(base_dir,config.datasources_store))
        datasources.init_db_engines(base_dir)

initialize(settings)
