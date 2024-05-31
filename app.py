import streamlit as st
from datetime import datetime
import requests
import pytz

'''
# TaxiFareModel Frontend
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Add ride parameters
'''

st.markdown('''
1. Let's ask for:
- Date and time
- Pickup longitude
- Pickup latitude
- Dropoff longitude
- Dropoff latitude
- Passenger count
''')

# Input fields
local_tz = pytz.timezone('America/New_York')

current_datetime = datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')

pickup_datetime = st.text_input('Pickup Date and Time', current_datetime)
pickup_longitude = st.number_input('Pickup Longitude')
pickup_latitude = st.number_input('Pickup Latitude')
dropoff_longitude = st.number_input('Dropoff Longitude')
dropoff_latitude = st.number_input('Dropoff Latitude')
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

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
