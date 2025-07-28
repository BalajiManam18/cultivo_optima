# Crop Recommendation System

## Project Overview

The Crop Recommendation System is a web-based machine learning application designed to suggest the most suitable crop to grow based on key soil and climate parameters. This tool helps farmers and agricultural advisors make informed decisions using data-driven insights rather than relying solely on tradition or guesswork.

## Objective and Motivation

Modern agriculture demands precision. This project combines data science and agriculture to assist in crop planning using measurable inputs like nitrogen, pH, and rainfall. It aims to bridge the gap between machine learning and rural applicability.

## Dataset Used

The model is trained on a dataset named `Crop_recommendation.csv`, which includes over 2200 samples of crop data labeled by crop type. Each record contains nutrient values and weather conditions essential for accurate crop selection.

## Technology Stack

The backend is built using Python’s Flask framework, with machine learning implemented using scikit-learn. The frontend is simple HTML/CSS, with JavaScript handling form submission via `fetch`. The model is saved using `joblib` and loaded in the Flask app.

## Application Structure

A Flask route serves the HTML form and processes the prediction requests. The user fills out the form with soil and climate values. The app sends this to the server, which loads the model, predicts the best crop, and returns the result without refreshing the page.

## How to Run

1. Clone the repo
2. Install the dependencies with `pip install -r requirements.txt`
3. Train the model using `model_train.py` (or use the existing one)
4. Run the Flask app with `python app.py`
5. Visit `http://localhost:5000` and use the form

## Future Scope

This project can be scaled for mobile use, integrated with real-time weather APIs, or deployed via platforms like AWS or Netlify. More features like fertilizer suggestions or soil health tracking can also be added.

## Author

Developed by Balaji Manam. For collaboration or inquiries, contact: bmtech@gmail.com
