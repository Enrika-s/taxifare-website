import streamlit as st
from datetime import datetime
import requests
import pytz

# Inline CSS for background
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
        background-image: url('https://www.example.com/your-image.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Input fields
local_tz = pytz.timezone('America/New_York')

current_datetime = datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')

pickup_datetime = st.text_input('Pickup Date and Time', current_datetime)
pickup_longitude = st.number_input('Pickup Longitude',  -73.980150, format="%.6f")
pickup_latitude = st.number_input('Pickup Latitude', 40.747925, format="%.6f")
dropoff_longitude = st.number_input('Dropoff Longitude',  -73.918524, format="%.6f")
dropoff_latitude = st.number_input('Dropoff Latitude', 40.831623, format="%.6f")
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8)


url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

if st.button('Get Fare Prediction'):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()['fare']
        st.success(f'The predicted fare is ${prediction:.2f}')
    else:
        st.error('Error')
