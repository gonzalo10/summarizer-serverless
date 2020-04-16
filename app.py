from summa.summarizer import summarize
from flask import Flask, request, jsonify

import json
app = Flask(__name__)

LANGUAGE = "english"
SENTENCES_COUNT = 12


@app.route("/",  methods=['POST'])
def translateText():

    if not request.data:
        return jsonify({'error': 'Data does not exist'}), 404

    payload = json.loads(request.data)

    if not type(payload) is dict:
        return jsonify({'error': 'Payload does not exist'}), 404

    text = payload.get("text")
    ratio = payload.get("ratio")

    if not ratio:
        ratio = 0.2
    if not text:
        return jsonify({"summary": "no text"})

    summary = summarize(text, ratio=ratio)

    if not summary:
        summary = text

    return jsonify({"summary": summary})


if __name__ == '__main__':
    app.run(debug=True)
