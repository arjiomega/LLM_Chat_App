
import requests
import streamlit as st

def get_weather(latitude, longitude, api_key=st.secrets["WEATHER_API_KEY"]):
    print("get weather function: ",(longitude, latitude))
    endpoint = "http://api.weatherapi.com/v1/current.json?"

    url = endpoint + f'key={api_key}' + f"&q={latitude},{longitude}&aqi=no"
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        # If the status code is 200 (OK), parse the JSON response
        data = response.json()
        print(data)
        return data
    else:
        # If the status code is not 200, print an error message
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print("Error message:", response.text)
        

if __name__ == "__main__":
    get_weather(13.3333, 123.4333)