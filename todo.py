import json
try:
    with open("tasks.json" , "r") as f:
        tasks = json.load(f)
except:
    tasks=[]

def list_tasks(tasks):
    for index, task in enumerate(tasks):
            print(index+1 , task["name"] , task.get("due" , "No date"))

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_tasks(tasks):
    name=input("Enter task name: ")
    date=input("Enter due date: ")
    task={"name":name , "done":False , "due":date}
    tasks.append(task)
    print("Task added!")
    save_tasks(tasks)
    
def show_tasks(tasks):
    if len(tasks)==0:
            print("No tasks yet!")
    else:
        done_count=0
        for index, task in enumerate(tasks):
            if task["done"] == True:
                    status="Done"
                    done_count += 1
            else:
                    status="Pending"
                
            print(index +1, task["name"], status , task.get("due", "No dates"))
        print(done_count, " of ",len(tasks), " tasks done.")

def mark_done(tasks):
    list_tasks(tasks)       
    index = int(input("Enter task number to mark as done: "))-1
    tasks[index]["done"] = True
    print("Mark done!")
    save_tasks(tasks)

def delete_tasks(tasks):
     if len(tasks)==0:
            print("No tasks yet!")
     else:
            list_tasks(tasks)
            index = int(input("Enter task number to delete: "))-1
            tasks.pop(index)
            print("Task deleted!")
            save_tasks(tasks)

def edit_tasks(tasks):
      if len(tasks)==0:
            print("No tasks yet!")
      else:
            list_tasks(tasks)
            index=int(input("Which task number to edit?: "))-1
            new_name=input("Enter new name: ")
            tasks[index]["name"]=new_name
            tasks[index]["done"]=False
            save_tasks(tasks)
            print("Task edited!") 

while True:
    print("=== To-Do App started!===")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Edit task")
    print("6. Exit")
    choice=input("You chose: ")
    if choice == "6":
        break

    elif choice == "1":
        add_tasks(tasks)
        
    elif choice == "2":
        show_tasks(tasks)
    
    elif choice == "3":
        mark_done(tasks)
       
    elif choice == "4":
        delete_tasks(tasks)
            
    elif choice == "5":
        edit_tasks(tasks)

    else:
        print("Invalid choice! Please enter 1-5")