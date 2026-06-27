from datetime import datetime
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

CONTACTS_FILE="contacts_capstone.json"

def load_contacts():   
    try:
        with open(CONTACTS_FILE, "r") as f:
            contacts=json.load(f)
    except FileNotFoundError:
        contacts=[]
    return contacts

def save_contacts(data):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(data,f)

def add_contacts():
    data=load_contacts()
    name=input("Enter name: ")
    duplicate=False
    for existing_contact in data:
        if existing_contact["name"].lower() == name.lower():
            duplicate = True
    if duplicate == True:
        print("Contact already exists!")
    else:
        while True:
            phone = input("Enter phone: ")
            cleaned=phone.replace(" ","").replace("+","").replace("-","")
            if cleaned.isdigit():
                break
            else:
                print("Invalid! Numbers only.")

        email = input("Enter email: ")
        birthday_str=input("Enter Birthday date: ")
        contact = {"name":name , "phone":phone , "email":email, "birthday":birthday_str}
        data.append(contact)
        print("Contact added!")
        save_contacts(data) 

def view_contacts():
    to_view=load_contacts()
    if len(to_view)==0:
        print("No contacts found!")
    else:
        for index, view in enumerate(to_view):
            print(index+1, view["name"] ,"-" , view["phone"] , view["email"] , view["birthday"])
            print("------------")

def days_until_birthday(birthday_str):
    try:
        birthday_date=datetime.strptime(birthday_str, "%Y-%m-%d")
        today=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        birthday_this_year=birthday_date.replace(year=today.year)
        if birthday_this_year<today:
            birthday_this_year=birthday_date.replace(year=today.year+1)
        days_until = birthday_this_year - today
        return days_until.days
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def check_upcoming_birthdays(contacts, days=7):
    for contact in contacts:
        days_left=days_until_birthday(contact["birthday"])
    if days_left is None:
         print("Something went wrong, please try again later.")
    elif days_left == 0:
        print("Birthday is TODAY!")
    elif days_left<=days:
        print("Birthday Upcoming!")
        print(f"Days left for the birthday: {days_left}")
    else:
        print("Birthday not upcoming!")

def get_public_holidays(country_code, year):
    api_key=os.getenv('CALENDARIFIC_API_KEY')
    url=f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country_code}&year={year}"
    # Holiday data provided by Calendarific (calendarific.com)
    try:
        info=requests.get(url)
        if info.status_code == 200:
            data=info.json()
            holidays=data["response"]["holidays"]
            return holidays
        else:
            print("Could not fetch holidays.")
            return[]
    except requests.exceptions.ConnectionError:
        print("No internet connection, please try again.")
        return[]
    
def check_birthday_holiday_overlap(contacts,holidays,threshold=3):
    found_match=False
    for contact in contacts:
        days_to_birthday=days_until_birthday(contact["birthday"])
        if days_to_birthday is None:
            continue
        if days_to_birthday>7:
            continue
        for holiday in holidays:
            days_to_holidays = days_until_birthday(holiday["date"]["iso"])
            near_days=days_to_birthday-days_to_holidays
            if abs(near_days)<=threshold:
                holiday_name=holiday["name"]
                print(f"HEY the {holiday_name} is near, Plan something big")
                found_match=True
    if not found_match:
        print("No birthdays near upcoming holidays right now!")
    
while True:
    print("===Contact Book===")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Check birthdays")
    print("4. Check birthdays near holidays")
    print("5. Exit")
    print("------------")
    choice=input("You chose: ")
    if choice == "5":
        break
    elif choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        data=load_contacts()
        check_upcoming_birthdays(data)
    elif choice == "4":
        data=load_contacts()
        country_code=input("Enter the code of country: ")
        year=input("Enter year: ")
        response=get_public_holidays(country_code, year)
        check_birthday_holiday_overlap(data,response)
    else:
        print("Invalid choice, please enter correct choice")
