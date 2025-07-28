import joblib
import os

# Check the model path again
model_path = os.path.join(os.getcwd(), "model.pkl")
print(f"Looking for model in: {model_path}")

try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
