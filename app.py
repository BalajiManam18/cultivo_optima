from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the dataset
dataset_path = os.path.join(os.getcwd(), "Crop_recommendation.csv")
try:
    df = pd.read_csv(dataset_path)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = None

def find_optimal_crop(input_data):
    """Find the crop with the closest feature match using Euclidean distance."""
    if df is None:
        return None, "Dataset not loaded."
    
    # Features to compare
    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    input_array = np.array(input_data)
    
    # Compute Euclidean distances
    distances = np.sqrt(((df[features] - input_array) ** 2).sum(axis=1))
    
    # Find the index of the minimum distance
    min_idx = distances.idxmin()
    
    # Return the corresponding crop
    return df.loc[min_idx, 'label'], None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if df is None:
            return jsonify({'error': 'Dataset not loaded.'}), 500

        try:
            # Get form inputs
            input_data = [
                float(request.form['Nitrogen']),
                float(request.form['Phosphorus']),
                float(request.form['Potassium']),
                float(request.form['Temperature']),
                float(request.form['Humidity']),
                float(request.form['pH']),
                float(request.form['Rainfall'])
            ]
            
            # Find the optimal crop
            crop, error = find_optimal_crop(input_data)
            
            if error:
                return jsonify({'error': error}), 400
            
            return jsonify({'crop': crop})
            
        except Exception as e:
            return jsonify({'error': f"Prediction error: {e}"}), 400

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)