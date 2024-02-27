import streamlit as st
import requests

st.title('Immo Eliza: Property Price Predictor')

# Define the input fields for the property attributes
nbr_bedrooms = st.number_input('Number of Bedrooms', min_value=1, value=2)
total_area_sqm = st.number_input('Total Area (sqm)', value=120.0)
surface_land_sqm = st.number_input('Surface Land (sqm)', value=100.0)
latitude = st.number_input('Latitude', value=0.0)
longitude = st.number_input('Longitude', value=0.0)
construction_year = st.number_input('Construction Year', min_value=1900, value=2000)


# When the 'Predict' button is clicked
if st.button('Predict the property price'):
    # The API endpoint URL
    url = 'http://localhost:8501'
    
    # The data to be sent to the API
    data = {
        'nbr_bedrooms': nbr_bedrooms,
        'total_area_sqm': total_area_sqm,
        'surface_land_sqm': surface_land_sqm,
        'latitude': latitude,
        'longitude': longitude,
        'construction_year': construction_year
    }
    
    # POST request to the API
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        prediction = response.json()['predicted_price']
        st.success(f'Predicted Property Price: ${prediction:.2f}')
    else:
        st.error('Error in prediction')

