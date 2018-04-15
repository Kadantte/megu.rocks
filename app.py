import os
from sanic import Sanic
from sanic.response import json

app = Sanic()
weebkey = os.environ['WEEBSH']

@app.route('/explosion') # EXPLOSION!!!
async def explosion(request):
    return json({'hello': 'world'})
