from sanic import Blueprint
from sanic.response import json
from components.marks.model import Mark
from sanic.response import text
from db import Base, session


api_marks = Blueprint('api_marks', url_prefix='/api/marks/')


### создание жалобы
@api_marks.route('/create_mark', methods=['POST'])
async def create_complaint(request):
    longitude = request.json.get('longitude')
    latitude = request.json.get('latitude')
    desc = request.json.get('description')
    mark = Mark.create_mark(longitude, latitude, desc)
    return json({'result': 'success',
                'markId': mark.id})


### выгрузка метки по ее id из БД
@api_marks.route('/get_by_id', methods=['POST'])
async def get_by_id(request):
    markId = request.json.get('markId')
    mark = Mark.get_by_id(markId)
    return json({'result': mark.to_json()})


### выгрузка всех меток из БД
@api_marks.route('/all_marks', methods=['POST'])
async def all_marks(request):
    marks = Mark.all_marks()
    marks = [obj.to_json() for obj in marks]
    return json({'result': marks})


### записываем новое описание метки
@api_marks.route('/update_mark', methods=['POST'])
async def update_mark(request):
    markId = request.json.get('markId')
    description = request.json.get('description')
    mark = Mark.get_by_id(mark_id)
    mark.description = description
    session.commit()
    return json({'result': 'success'})

