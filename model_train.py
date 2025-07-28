import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

# Split features and target
X = df.drop('label', axis=1)
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'crop_model.pkl')
print("Model saved as crop_model.pkl")
