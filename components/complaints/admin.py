from flask_admin.contrib.sqla import ModelView
from components.complaints.model import Complaint
from flask import session


class ComplaintView(ModelView):
 
    create_modal = True
    edit_modal = True


def load_views(admin, session):
    admin.add_view(ComplaintView(Complaint, session))