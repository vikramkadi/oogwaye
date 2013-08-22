from flask import Flask, render_template
from app.users.views import users_mod

app = Flask(__name__, static_folder='static')
app.register_blueprint(users_mod, url_prefix='/users')


