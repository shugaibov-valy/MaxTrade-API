from flask_admin.contrib.sqla import ModelView
from components.users.model import User
from flask import session


class UserView(ModelView): 
    create_modal = True
    edit_modal = True


def load_views(admin, session):
    admin.add_view(UserView(User, session))