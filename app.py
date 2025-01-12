from flask import Flask, request, jsonify,render_template
import requests
import json

app = Flask(__name__)

# URL del endpoint de Watson Emotion
url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

# header with the model
headers = {
    'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
    'Content-Type': 'application/json'
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text_to_analyze = data.get('text')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Datos para la solicitud POST a Watson
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Realizando la solicitud a Watson Emotion
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        emotions = result.get("emotion", {})
        return jsonify({"emotions": emotions})
    else:
        return jsonify({"error": "Error with Watson API"}), 500

if __name__ == "__main__":
    app.run(debug=True)
