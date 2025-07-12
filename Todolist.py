tasks = []
def addtask (task,status) :
        tasks.append({"task": task, "done" :status})
        with open ("todolist.txt" , "a") as f :
            f.write(f"{task} - {"Done" if status else "Not Done"}\n")

def view_all_tasks() :
    for index, task in enumerate(tasks) :
        status = "Done" if task ["done"] else "Not Done"
        print(f"{index + 1}: {task["task"]} [{status}]")
        

def delete (task_name) :
    for task in tasks : 
        if task["task"] == task_name :
            tasks.remove(task)
            print(f"Task {task} has been removed")
    else : 
        print(f"Not Found!")

try : 
    while True :
        print("===Welcome===")
        print("-----To Do List Manager-----")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1" :
            new_task = input("Enter new task: ")
            status = input("Did you complete it? (Y/N): ").lower() == "y"
            addtask(new_task,status) 
        elif choice == "2" :
            view_all_tasks()
        elif choice == "3" :
            delete_task = input("Enter the task you want to remove: ")
            delete (delete_task)
        elif choice == "4" :
            print("Thank You!, Goodwork!")
            print("Exiting...")
            break
        else :
            print("Invalid input!")

except Exception as e:
    print(e)


