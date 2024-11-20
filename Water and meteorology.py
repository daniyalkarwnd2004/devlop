import datetime
import requests

API_KEY = "81443f14908bdae431791e75ed8479ed"


def get_request(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        print(f"The weather in your city: {city}")
        print(f"temperature: {main['temp']} C")
        print(f"sense of temperature: {main['feels_like']} C")
        print(f"status: {weather['description']}")
        print(f"the wind: {wind['speed']} meters per second")
        with open("openweathermap.json", "a", encoding="utf-8") as file:
            file.write(f"'Information of the desired city': "
    f"{city, main['temp'], main['feels_like'], weather['description'], wind['speed']}, {datetime.datetime.now()}, \n")
    else:
        print("Oh, the desired city was not found :(")


name_city = input("Please enter the desired city name: ")
get_request(name_city)
