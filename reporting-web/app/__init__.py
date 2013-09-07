from flask import Flask, render_template
from app.users.views import users_mod
from app.studio.views import studio_main

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(users_mod, url_prefix='/users')
app.register_blueprint(studio_main, url_prefix='/studio')
