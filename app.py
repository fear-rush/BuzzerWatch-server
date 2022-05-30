from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from sentiment import sentiment
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>Service is Running!</h1>"

@app.route("/twitter", methods=['POST'])
def result():
    data = request.json['hashtag']
    print(data)
    # text = request.values['hashtag']
    # print(text)
    res = sentiment(data)
    responses = res.to_json(orient = "table")
    return responses

if __name__ == '__main__':
    app.run(debug=True)