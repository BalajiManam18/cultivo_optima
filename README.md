Crop Recommendation System
Project Overview
The Crop Recommendation System is a web-based machine learning application designed to suggest the most suitable crop to grow based on key soil and climate parameters. This solution was created to support farmers and agricultural advisors in making informed crop planning decisions, using data-driven insights rather than intuition or tradition. The system analyzes essential input features such as nitrogen, phosphorus, potassium, temperature, humidity, pH level, and rainfall, then returns the optimal crop using a trained machine learning model.

Objective and Motivation
Modern agriculture increasingly relies on technology to improve yield and sustainability. This project was built with the intention of blending data science and agriculture to create a tool that’s practical, lightweight, and easy to use. The core aim is to make machine learning accessible for solving real-world farming challenges, especially in rural and semi-urban areas where such tools are most needed.

Dataset Used
The system is trained on a public dataset named Crop_recommendation.csv. This dataset includes over 2200 samples of crop data with labeled outputs representing various crop types. Each record contains values for soil nutrients (N, P, K), environmental conditions (temperature, humidity, rainfall), and soil pH. The data is preprocessed and used to train a classification model to accurately predict the crop best suited for the given conditions.

Technology Stack
This project uses Python and the Flask web framework to build the backend. Machine learning is implemented using scikit-learn and pandas, with the trained model saved using joblib. The frontend is developed using standard HTML, CSS, and JavaScript. Bootstrap is used for styling, and the form submission is handled through JavaScript’s fetch API to send data asynchronously to the backend.

Application Structure
The backend of the system is built around a Flask server with defined routes for rendering the HTML form and for processing user inputs to generate crop recommendations. A trained Random Forest Classifier model is loaded during server startup. The frontend is served using a simple HTML form where users can enter values manually. The CSS styling is managed via a separate static stylesheet, ensuring a clean and responsive layout.

Running the Project Locally
To run the project, start by cloning the repository and installing the required Python libraries. The model can be trained using a script (model_train.py) provided in the project directory. Once the model is saved, run the Flask application using app.py. When the server starts, open a web browser and navigate to http://127.0.0.1:5000. You will be presented with a form where you can input soil and climate values. Upon submission, the recommended crop will be displayed instantly.

Sample Usage
A user might input values such as 90 for nitrogen, 40 for phosphorus, 40 for potassium, 23°C temperature, 80% humidity, pH level of 6.5, and 120 mm rainfall. Based on these values, the system would recommend a suitable crop — for example, rice — depending on the model’s prediction.

Future Scope
While the current version is deployed locally, this project can be extended further by integrating cloud services like AWS or deploying it as a mobile-friendly web app. Additional features like geolocation-based weather fetching or fertilizer suggestions can also be added. It has potential for use in smart farming systems, educational tools, or even in regional government planning for crop distribution.
