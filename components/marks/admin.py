from flask_admin.contrib.sqla import ModelView
from components.marks.model import Mark
from flask import session


class MarkView(ModelView):
    create_modal = True
    edit_modal = True


def load_views(admin, session):
    admin.add_view(MarkView(Mark, session))