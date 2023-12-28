import requests


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        weather = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']

        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Minimum Temperature: {temp_min} °C")
        print(f"Maximum Temperature: {temp_max} °C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")


api_key = '6060251afcdc6acb3f40ca8ecc8a9d54'

# Take user input for city name
city = input("Enter the city name (Example: Delhi): ")
get_weather(api_key, city)
