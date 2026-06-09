
tip_percent= float(input("Enter tip percentage(%):"))
num_items = int(input("How many items are purchased?: "))

items = []
people = []

for i in range(num_items):
     print("Enter these details:")
     item_name = input("Item name: ")
     price = float(input("Enter item's price: "))
     person_name = input("Enter person's name: ")
     items.append((item_name , price , person_name))
     people.append(person_name)

total_bill = sum(price for item_name , price , person in items)
print(f"Total bill: {total_bill}")
num_people = len(people)

def itemized_split(items , total_bill , tip_percent):
     tip_amount = total_bill*(tip_percent/100)
     balances = {}
     
     for item_name , price , person in items:
          tip_share = (price / total_bill)*tip_amount
          amount = price + tip_share
          if person in balances:
               balances[person] += amount
          else:
               balances[person] = amount
        
     for person , amount in balances.items():
         print(f"{person} owes:{amount}")

    
itemized_split(items , total_bill , tip_percent)
     
     





