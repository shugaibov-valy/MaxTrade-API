from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from sanic.log import logger
from config import DevConfig as config
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