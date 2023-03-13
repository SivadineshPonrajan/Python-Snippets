from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/foo', methods=['POST','OPTIONS','GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def foo():
    return request.args.get("page")

@app.route('/')
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def boo():
    return "success"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)