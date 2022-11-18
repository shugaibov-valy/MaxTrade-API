import os
from flask import Flask, render_template, request, redirect
from flask_admin import Admin, AdminIndexView, helpers, expose
from flask_babelex import Babel
from config import config
from db import session as db_session
from components.admin_views import *

def admin_start():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        return 'ru'

        
    admin = Admin(app, name='MaxTrade-DB', template_mode='bootstrap3')
    users_view.load_views(admin, db_session)
    complaints_view.load_views(admin, db_session)

    app.config.from_object(config)
    app.run(debug=config.DEBUG, host=config.HOST, port=8001)