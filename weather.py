import requests

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def weather(name):
    token = "Get your weather api token name for detail visit here" \
            "https://home.openweathermap.org/"
    api_url = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=" + token + "&q=" + name)
    data = api_url.json()
    main = data['weather'][0]['main']
    temprature = data['main']['temp']
    temprature = temprature - 273.15
    degree_sign = u"\N{DEGREE SIGN}"
    feels_like = data['main']['feels_like'] - 273.15
    wind_speed = data["wind"]["speed"]
    wind_speed_degree = data["wind"]["deg"]

    return  f"Weather forcast of a specific city\nCity name :{name}\nWeather : {main}\nTemperature :{str(temprature) + degree_sign}C\nFeels like :{str(feels_like) + degree_sign}C\nWind speed :{wind_speed}\nDegree :{wind_speed_degree}"


vaild = False
while not vaild:
    City_name = input("Enter the city name : ")
    print(weather(City_name))
    print()
    print()






# token = "0c42f7f6b53b244c78a418f4f181282a"
# City_name = input("Enter the city name : ")
# api_url = requests.get("http://api.openweathermap.org/data/2.5/weather?appid="+token+"&q="+City_name)
# data = api_url.json()
# main = data['weather'][0]['main']
# temprature = data['main']['temp']
# temprature = temprature - 273.15
# degree_sign = u"\N{DEGREE SIGN}"
# feels_like = data['main']['feels_like'] - 273.15
# wind_speed = data["wind"]["speed"]
# wind_speed_degree = data["wind"]["deg"]
#
# print(f"Weather forcast of a specific city\nCity name :{City_name}"
#       f"\nWeather : {main}\nTemperature :{str(temprature)+degree_sign}C\n"
#       f"Wind speed :{wind_speed}\nDegree :{wind_speed_degree}")
