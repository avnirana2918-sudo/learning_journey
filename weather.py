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
def load_favorites():
    try:
        with open("favorites.json", "r") as f:
            favorites=json.load(f)
    except:
        favorites = []
    return favorites

def save_favorites(favorites):
    with open("favorites.json", "w") as f:
        json.dump(favorites, f)

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
    favorites = load_favorites()
    favorite={"city": fav_city}
    fav=False
    for existing in favorites:
        if fav_city == existing["city"]:
            fav=True
    if fav == True:
        print("City already exists as favorite")
    else:
        favorites.append(favorite)
        save_favorites(favorites)
        print("Added as favorite!")

def view_favorites():
    favorites=load_favorites()
    if len(favorites) == 0:
        print("No favorites saved yet!")
    else:
        for index, favorite in enumerate(favorites):
            print(index+1, favorite["city"])

def remove_duplicate_favorites():
    favorites= load_favorites()
    cleaned=[]      
    for original_city in favorites:
        to_delete= False
        for kept_city in cleaned:
            if kept_city["city"] == original_city["city"]:
                to_delete=True
        if to_delete == False:
            cleaned.append(original_city)
    save_favorites(cleaned)

def quick_research(units,temp_symbol):
    favorites=load_favorites()
    if not favorites:
        print("You have no favorites saved yet. Add one first!")
        return
    
    for index, favorite in enumerate(favorites):
        print(index+1, favorite["city"])
    while True:
        index=int(input("Enter city number to searh: "))-1
        if index>len(favorites)-1 or index<0:
            print("Invalid number, try again.")
        else:
            break            
    city=favorites[index]["city"]
    while True:
        print("1. Current weather")
        print("2. 5-day forecast")
        chosen=input("Enter your choice: ")
        if chosen == "1":
            get_current_weather(city,units,temp_symbol)
        elif chosen == "2":
            get_forecast(city,units,temp_symbol)
        else:
            print("Invalid choice please enter 1 or 2.")
        another= input("Search another from favorites?(y/n): ")
        if another.lower()=="n" or another.lower()=="no":
            break

def remove_favorite():
    favorites=load_favorites()
    if not favorites:
        print("You have no favorites saved yet. Add one first!")
        return
    for index, favorite in enumerate(favorites):
        print(index+1, favorite["city"])
    while True:
        index=int(input("Enter city number to remove: "))-1
        if index>len(favorites)-1 or index<0:
            print("Invalid number, try again")
        else:
            break
    city=favorites[index]["city"]
    to_remove=input(f"Are you sure you want to remove {city}?(y/n): ")
    if to_remove.lower() == "y" or to_remove.lower() == "yes":
        favorites.pop(index)
        print("City deleted!")
        save_favorites(favorites)
    else:
        print("Cancelled")

units=None
temp_symbol=None
while True:
    print("1. Current weather")
    print("2. 5-day forecast")
    print("3. Add city to favorites")
    print("4. View favorites") 
    print("5. To search from favorites.") 
    print("6. To remove from favorites.")  
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
    elif choice == "5":
        if units is None:
            units,temp_symbol = choices()
        quick_research(units,temp_symbol)
    elif choice == "6":
        remove_favorite()
    else:
        print("Invalid choice, please enter correct choice.")

    search = input("Search another city?(y/n)")
    if search.lower() == "n" or search.lower() == "no":
        break
#remove_duplicate_favorites()