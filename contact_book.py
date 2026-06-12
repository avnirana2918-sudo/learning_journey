import json
try:
     with open("contacts.json", "r") as f:
          contacts = json.load(f)
except:
     contacts = []

while True:
    print("=== Contact Book ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    choice=int(input("You chose:"))
    if choice == 5:
        break
    
    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = {"name":name , "phone":phone , "email":email}
        contacts.append(contact)
        print("Contact added!")
        with open("contacts.json", "w") as f:
             json.dump(contacts, f)
    
    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print("Name: ",contact["name"])
                print("Phone: ",contact["phone"])
                print("Email: ",contact["email"])
                print("----------")

    elif choice == 3:
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("Name: ", contact["name"])
                print("Phone: ", contact["phone"])
                print("Email: ", contact["email"])
                found = True
        if found == False:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                found = True
                break
        if found == True:
                print("Contact deleted!")
                with open("contact.json", "w") as f:
                     json.dump(contacts, f)
        if found == False:
                print("Contact not found")