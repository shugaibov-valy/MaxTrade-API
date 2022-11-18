from sanic import Blueprint
from sanic.response import json
from components.users.exc import AuthLoginUserNotFound, RegLoginUserNotFound
from components.complaints.model import Complaint


api_complaints = Blueprint('api_complaints', url_prefix='/api/complaints/')


### создание жалобы
@api_complaints.route('/create_complaint', methods=['POST'])
async def create_complaint(request):
    title = request.json.get('title')
    longitude = request.json.get('longitude')
    latitude = request.json.get('latitude')
    desc = request.json.get('desc')
    category = request.json.get('category')
    user_id = request.json.get('user_id')
    Complaint.create_complaint(title, longitude, latitude, desc, category, user_id)
    return json({'result': 'success'})

### выгрузка жалоб определенного пользователя по user_id
@api_complaints.route('/complaints_of_user', methods=['POST'])
async def create_complaint(request):
    user_id = request.json.get('user_id')
    complaints = Complaint.comlaints_by_user_id(user_id)
    complaints = [obj.to_json() for obj in complaints]
    return json({'result': complaints})

    # try:
    #     user = User.check_login(login)
    #     return json({'result': 'failed', 
    #                 'message': 'login is busy'})   #### логин существует
    # except RegLoginUserNotFound:                    ###  если не сущетсвует, то создаем его
    #     User.create_user(email, login, password)
    #     return json({'result': 'success'})