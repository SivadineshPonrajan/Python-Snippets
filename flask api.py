import os
import json
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	token = request.args.get('token', default = '*', type = str)
	if (token != '*'):
		return "1"
	else:
		return "0"

app.run(host="127.0.0.1",port=1234)