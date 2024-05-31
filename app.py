import streamlit as st

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
pickup_datetime = st.text_input('Pickup Date and Time', '2014-07-06 19:18:00')
pickup_longitude = st.number_input('Pickup Longitude', -73.950655)
pickup_latitude = st.number_input('Pickup Latitude', 40.783282)
dropoff_longitude = st.number_input('Dropoff Longitude', -73.984365)
dropoff_latitude = st.number_input('Dropoff Latitude', 40.769802)
passenger_count = st.number_input('Passenger Count', 1, min_value=1, max_value=8)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

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
        st.success(f'The predicter fare is ${prediction}')
    else:
        st.error('Error')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
