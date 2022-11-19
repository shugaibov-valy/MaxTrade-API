from sanic import Blueprint
from sanic.response import json
from components.users.exc import AuthLoginUserNotFound, RegLoginUserNotFound
from components.complaints.model import Complaint
from sanic.response import text
from db import Base, session


api_complaints = Blueprint('api_complaints', url_prefix='/api/complaints/')


### создание жалобы
@api_complaints.route('/create_complaint', methods=['POST'])
async def create_complaint(request):
    title = request.json.get('title')
    longitude = request.json.get('longitude')
    latitude = request.json.get('latitude')
    desc = request.json.get('description')
    category = request.json.get('type')
    user_id = request.json.get('authorId')
    problemImageURL = request.json.get('problemImageUrl')
    complaint = Complaint.create_complaint(title, longitude, latitude, desc, category, user_id, problemImageURL)
    return json({'result': 'success',
                'complaintId': complaint.id})

### выгрузка жалоб определенного пользователя по user_id
@api_complaints.route('/complaints_of_user', methods=['POST'])
async def create_complaint(request):
    user_id = request.json.get('authorId')
    complaints = Complaint.comlaints_by_user_id(user_id)
    complaints = [obj.to_json() for obj in complaints]
    return json({'result': complaints})

### выгрузка всех жалоб c БД
@api_complaints.route('/all_complaints', methods=['POST'])
async def all_complaints(request):
    complaints = Complaint.all_comlaints()
    complaints = [obj.to_json() for obj in complaints]
    return json({'result': complaints})

### лайкаем жалобу по его id в БД
@api_complaints.route("/like_complaint", methods=['POST'])
async def like_complaint(request):
    complaint_id = request.json.get('complaintId')
    print(complaint_id)
    complaint = Complaint.get_by_id(complaint_id)
    print(complaint)
    complaint.count_like += 1
    session.commit()
    return json({'result': "success"})
