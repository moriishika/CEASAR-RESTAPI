from flask import Flask, jsonify, make_response, request
from convert_to_caesar import convert_to_Caesar
from encrypt_caesar import encrypt_caesar
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
  if request.method == "GET":
    return "Hai ayang"

  if request.method == "POST":
    data = request.get_json()
    shiftNumber = int(data["shiftNumber"])
    convertedText = convert_to_Caesar(data["text"])
    result = encrypt_caesar(shiftNumber, convertedText)

    response = {"status":"Success", "result" : result}

    return make_response(jsonify(response))


app.run(host='0.0.0.0', port=81)


