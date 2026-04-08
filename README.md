# Final Project: Emotion Detection Web Application

## Overview
This project is a Flask-based web application that analyzes text to determine its underlying emotional tone. Utilizing the IBM Watson NLP API, the application extracts confidence scores for five key emotions: anger, disgust, fear, joy, and sadness, and automatically identifies the dominant emotion. 

## Features
* **Watson API Integration:** Connects to the IBM Watson NLP service for accurate text classification.
* **Web Interface:** A user-friendly frontend interface, served via Flask, that allows users to submit text and view the emotional breakdown.
* **Error Handling:** Robust backend validation that safely handles blank or invalid text submissions, returning appropriate error messages to the user without crashing the server.
* **Unit Testing:** Automated tests implemented to ensure the reliability and accuracy of the dominant emotion extraction logic.

## Technology Stack
* **Backend:** Python 3.11, Flask
* **API/Machine Learning:** IBM Watson NLP 
* **Frontend:** HTML, JavaScript
* **Testing:** `unittest` module (Python standard library)

## Project Structure
* `EmotionDetection/`: A custom Python package containing the `emotion_detection.py` script, which handles the Watson API requests and JSON parsing.
* `server.py`: The main Flask application that routes web requests, handles frontend-backend communication, and manages error states.
* `test_emotion_detection.py`: A suite of unit tests validating the accuracy of the emotion analysis logic.
* `templates/` & `static/`: Contains the HTML and JavaScript files for the web interface.

## Usage
1. Enter a statement into the text box on the web interface.
2. Click **Run Emotion Detection**.
3. The system will return a formatted string displaying the confidence scores for each emotion and highlight the dominant emotion. If the input is invalid or blank, an error message will prompt the user to try again.