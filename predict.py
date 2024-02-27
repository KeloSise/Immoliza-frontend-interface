import joblib
import pandas as pd

# Load the saved artifacts
artifacts = joblib.load("models/xgboost_artifacts.joblib")
num_pipeline = artifacts['num_pipeline']
model = artifacts['model']
num_features = artifacts['num_features']

def preprocess(data):
    """Preprocess the input data."""
    df = pd.DataFrame(data, index=[0])  # Assuming data is a dict for a single property
    processed_data = num_pipeline.transform(df[num_features])
    return processed_data

def predict(data):
    """Predict the property price."""
    processed_data = preprocess(data)
    prediction = model.predict(processed_data)
    return prediction[0]  # Return the first (and only) prediction if data is for a single property

# Example usage:
data = {"nbr_bedrooms": 3, "total_area_sqm": 120, "surface_land_sqm": 680.0, "latitude": 51.2171725, "longitude": 4.3799821, "construction_year": 1963}
price_prediction = predict(data)
print(price_prediction)
