import os
from flask import Flask
from flask import jsonify

app = Flask(__name__)
weebkey = os.environ['WEEBSH']

@app.route('/explosion') # EXPLOSION!!!
async def explosion(request):
    return json({'hello': 'world'})
