import os
from flask import Flask
from flask import jsonify

app = Flask(__name__)
weebkey = os.environ.get('WEEBSH', None)

@app.route('/explosion') # EXPLOSION!!!
def explosion():
    return jsonify({'hello': 'world'})
