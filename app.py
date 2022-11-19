from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from sanic.log import logger
from config import DevConfig as config
from geocoder import coords_to_address
from sanic.response import text
from api import bps


app = Sanic('maxtrade-api')

#подключаем все blueprints
for bp in bps:
    app.blueprint(bp)


#api info
@app.route('/')
async def info(request):
    return json({'result': 'ok',
                 'version': config.VERSION})


@app.exception(NotFound)
def ignore_404s(request, exception):
    return json({'error': 'not found'}, status=404)

@app.post("/get_address")
async def get_address(request):
    longitude = request.json.get('longitude')
    latitude = request.json.get('latitude')
    address = coords_to_address(longitude, latitude)
    return json({'result': 'success',
                 'streetName': address})