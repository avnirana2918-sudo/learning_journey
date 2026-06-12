import math
tip_percent= float(input("Enter tip percentage(%):"))
num_items = int(input("How many items are purchased?: "))

items = []
people = []

for i in range(num_items):
     print("Enter these details:")
     item_name = input("Item name: ")
     price = float(input("Enter item's price: "))
     person_name = input("Enter person's name: ")
     shared = input("Is this item shared?(yes/no)")
     if (shared.lower() == "yes"):
          person = input("Enter names seperated by space: ").split()
          items.append((item_name , price , person))
     else:
          items.append((item_name , price , person_name ))
          people.append(person_name)
     
discount = float(input("Enter discount: "))
total_bill = sum(price for item_name , price , person in items)
total_bill = total_bill - discount
print(f"Total bill: {total_bill}")
num_people = len(people)

def itemized_split(items , total_bill , tip_percent):
     if len(items) == 0:
          print("No items entered!")
     
     tip_amount = total_bill*(tip_percent/100)
     balances = {}
     
     for item_name , price , person in items:
          tip_share = (price / total_bill)*tip_amount
          amount = price + tip_share
          if isinstance(person , list):
               share = amount / len(person)
               for p in person:
                if p in balances:
                   balances[p] += share
                else:
                   balances[p] = share
          else:
              if person in balances:
                  balances[person] += amount
              else:
                  balances[person] = amount
                  

     for person in balances:
          balances[person] = math.floor(balances[person])

     real_total = math.floor(total_bill+tip_amount)
     floored_total = sum(balances.values())
     remainder = real_total - floored_total

     first_person= list (balances.keys())[0]
     balances[first_person] += remainder
        
     for person , amount in balances.items():
         print(f"{person} owes:{amount}")

    
itemized_split(items , total_bill , tip_percent)
     
     





