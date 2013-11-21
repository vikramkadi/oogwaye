from flask import Flask, render_template
from app.users.views import users_mod
from app.report.views import report_mod
from app.report import datasources
from app.services import mongo
from app.users import security

import os
import settings

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(users_mod, url_prefix='/users')
app.register_blueprint(report_mod, url_prefix='/report')
app.secret_key = settings.secret_key

def initialize(config):
    base_dir = config.base_dir
    
    if os.path.exists(os.path.join(base_dir,config.datasources_store)):
        datasources.init_datasources(os.path.join(base_dir,config.datasources_store))
        datasources.init_db_engines(base_dir)
    

    mongo.init_mongo(config.mongo_host, config.mongo_port, config.mongo_db_name)

    if os.path.exists(os.path.join(base_dir, config.credentials_store)):
		security.init(os.path.join(base_dir, config.credentials_store))

initialize(settings)
