from sanic import Blueprint
from sanic.response import json
from components.users.exc import AuthLoginUserNotFound, RegLoginUserNotFound
from components.users.model import User
from db import Base, session


api_users = Blueprint('api_users', url_prefix='/api/users/')


### регистрация пользователя по почте, логину и паролю
@api_users.route('/reg', methods=['POST'])
async def reg(request):
    email = request.json.get('email')
    login = request.json.get('login')
    password = request.json.get('password')
    try:
        user = User.check_login(login)
        return json({'result': 'failed', 
                    'message': 'login is busy'})   #### логин существует
    except RegLoginUserNotFound:                    ###  если не сущетсвует, то создаем его
        user = User.create_user(email, login, password)
        return json({'result': 'success',
                    'authorId': user.id})


### авторизация пользователя по логину и паролю
@api_users.route('/auth', methods=['POST'])
async def auth(request):
    login = request.json.get('login')
    password = request.json.get('password')
    try:
        user = User.get_user(login, password)
        if user.is_admin:
            return json({'result': 'success',
                        'is_admin': user.is_admin,
                        'authorId': user.id})    ### проверка если это минстрой или обычный пользователь
        return json({'result': 'success', 
                    'is_admin': user.is_admin,
                    'authorId': user.id}) ### пользователь существует
    except AuthLoginUserNotFound:
        return json({'result': 'failed', 
                    'message': 'not found user'})


### авторизация пользователя по логину и паролю
@api_users.route('/get_by_id', methods=['POST'])
async def get_by_id(request):
    user_id = request.json.get('authorId')
    user = User.get_by_id(user_id)
    return json({'result': user.to_json()})



### метод для обновления информации о пользователи
@api_users.route('/update_info', methods=['POST'])
async def update_info(request):
    user_id = request.json.get('authorId')
    name = request.json.get('name')
    surname = request.json.get('surname')
    url_avatar = request.json.get('url_avatar')
    user = User.get_by_id(user_id)
    user.name = name
    user.surname = surname
    user.url_avatar = url_avatar
    session.commit()
    return json({'result': 'success'})

    