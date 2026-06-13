import json
def add_contact(contacts):
      name = input("Enter Name: ")
      duplicate = False
      for contact in contacts:
             if contact["name"].lower() == name.lower():
                  duplicate = True
      if duplicate == True:
             print("Contact already exists!")
      else:
                while True:
                    phone = input("Enter phone: ")
                    if phone.isdigit():
                         break
                    else:
                         print("Invalid! Numbers only.")

                email = input("Enter email: ")
                contact = {"name":name , "phone":phone , "email":email}
                contacts.append(contact)
                print("Contact added!")
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f)    

def view_contacts(contacts):
     if len(contacts) == 0:
            print("No contacts found.")
     else:
         for contact in contacts:
             print("Name: ",contact["name"])
             print("Phone: ",contact["phone"])
             print("Email: ",contact["email"])
             print("----------")

def search_contacts(contacts):
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

def delete_contact(contacts):
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

def edit_contact(contacts):
      search = input("Enter name to search: ")
      found = False
      for contact in contacts:
             if contact["name"].lower() == search.lower():
                print("Name: ", contact["name"])
                print("Phone: ", contact["phone"])
                print("Email: ", contact["email"])
                found = True
                existing_contact = contact
      if found == True:
            print("Enter details to update or press Enter to keep old")
            new_name = input("Enter New Name: ")
            new_phone = input("Enter New phone: ")
            new_email = input("Enter New email: ")
            existing_contact["name"]=new_name or existing_contact["name"]
            existing_contact["phone"]=new_phone or existing_contact["phone"]
            existing_contact["email"]=new_email or existing_contact["email"]
            with open("contact.json", "w") as f:
                     json.dump(contacts, f)
            print("Contact updated!")

      elif found == False:
            print("Contact not found.") 


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
    print("6. Edit contact")
    choice=int(input("You chose:"))
    if choice == 5:
        break
    
    if choice == 1:
       add_contact(contacts)
    
    elif choice == 2:
        view_contacts(contacts)

    elif choice == 3:
        search_contacts(contacts)
       
    elif choice == 4:
        delete_contact(contacts)

    elif choice == 6:
         edit_contact(contacts)
