import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "5827c99d71511b219b3a5f2d38517948"

weather_params = {
    "lat": 54.857800,
    "lon": -5.823622,
    "appid": api_key,
    "exclude": "current,minute,daily",
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

        if will_rain:
            print("Bring an umbrella")

#print(weather_data["hourly"][0]["weather"][0]["id"])



