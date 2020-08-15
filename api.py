import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Open House AI Demo </h1>
<p>Api demo for the purposes of the coding challenge from Open House Ai</p>'''


app.run()