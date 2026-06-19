import requests
import json

def choices():
    unit_choice = input("Choose units - Celsius or Fahrenheit? (C/F): ")
    if unit_choice.lower() == "f":
        units = "imperial"
    else:
        units = "metric"

    if units == "imperial":
        temp_symbol = "°F"
    else:
        temp_symbol = "°C"
        return units, temp_symbol

def get_forecast(city,units,temp_symbol):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=b30ee619cea83fed538d5730af750472&units={units}")
        if response.status_code == 200:
            for entry in response.json()["list"]:
                if "12:00:00" in entry["dt_txt"]:                                  
                    temperature = entry["main"]["temp"]
                    humidity = entry["main"]["humidity"]
                    wind_speed = entry["wind"]["speed"]
                    condition = entry["weather"][0]["description"]
                    temperature=round(temperature, 1)
                    wind_speed=round(wind_speed, 1)
                    print(f"Temperature: {temperature} {temp_symbol}")
                    print("Humidity: " ,humidity)
                    print("Wind speed: ",wind_speed)
                    print("Weather condition: ", condition)
        else:
            print("City not found, please try again")
    except requests.exceptions.ConnectionError:
        print("No internet connection, please check your network")
      
def get_current_weather(city,units,temp_symbol):
    
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid=b30ee619cea83fed538d5730af750472")
        if response.status_code == 200:
            data = response.json()                      
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            condition = data["weather"][0]["description"]
            temperature=round(temperature, 1)
            wind_speed=round(wind_speed, 1)
            print(f"Temperature: {temperature} {temp_symbol}")
            print("Humidity: " ,humidity)
            print("Wind speed: ",wind_speed)
            print("Weather condition: ", condition)
        else:
            print("City not found, please try again")
    except requests.exceptions.ConnectionError:
        print("No internet connection, please check your network")
def add_favorite(fav_city):
    try:
        with open("favorites.json", "r") as f:
            favorites=json.load(f)
    except:
        favorites = []

    favorite={"city": fav_city}
    favorites.append(favorite)
    with open("favorites.json", "w") as f:
        json.dump(favorites, f)
def view_favorites():
    try:
        with open("favorites.json", "r") as f:
            favorites=json.load(f)
        for favorite in favorites:
            print("City: ", favorite["city"])  
    except:
        if not favorites:
            print("No favorites saved yet")
units=None
temp_symbol=None
while True:
    print("1. Current weather")
    print("2. 5-day forecast")
    print("3. Add city to favorites")
    print("4. View favorites")    
    choice = input("Enter your choice: ")
    if choice == "1":
        if units is None:
            units, temp_symbol = choices()
        city = input("Enter the city name: ")
        get_current_weather(city,units,temp_symbol)
    elif choice == "2":
        if units is None:
            units, temp_symbol = choices()
        city = input("Enter the city name: ")
        get_forecast(city,units,temp_symbol)
    elif choice == "3":
        fav_city = input("Enter you favorite city: ")
        add_favorite(fav_city)
    elif choice == "4":
        view_favorites()
    else:
        print("Invalid choice, please enter correct choice.")

    search = input("Search another city?(y/n)")
    if search.lower() == "n" or search.lower() == "no":
        break