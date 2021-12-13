from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/" , methods=["POST", "GET"])
def helloWorld():
    if request.method == 'POST':
        if request.is_json:
            r = request.json["rrr"]
        else:
            r = request.form["rrr"]
        return jsonify({"input_text":r})
    return "bad request or not POST request"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)