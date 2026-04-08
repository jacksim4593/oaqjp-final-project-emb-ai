"""
Flask server for the Emotion Detection application.
This module provides endpoints to analyze text for emotions and render the UI.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze the provided text and return the emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None (which happens on blank/invalid input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # If it is valid, extract the required set of emotions and their scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return the formatted string exactly as requested, split to avoid long lines
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    