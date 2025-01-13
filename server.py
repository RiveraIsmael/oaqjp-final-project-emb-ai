from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Assuming index.html exists in templates folder

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text_to_analyze = request.form.get('text')  # Get the text input from the user
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        formated_response = {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }
        return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )
    else:
        return jsonify({"error": "No text provided for analysis."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Make the app accessible at localhost:5000