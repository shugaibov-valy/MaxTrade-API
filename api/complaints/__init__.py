from sanic import Blueprint
from sanic.response import json
from components.users.exc import AuthLoginUserNotFound, RegLoginUserNotFound
from components.complaints.model import Complaint
from sanic.response import text


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
    Complaint.create_complaint(title, longitude, latitude, desc, category, user_id, problemImageURL)
    return json({'result': 'success'})

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

