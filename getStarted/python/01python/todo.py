#normal to do list
def addtask(tasks):
    task = input("Enter a task: ")
    obj = {"id": len(tasks) + 1, "task": task}
    tasks.append(obj)
    print("Task added successfully!")
def viewtask(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"{task['id']}. {task['task']}")
def updatetask(tasks):
    task_id = int(input("Enter the task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_task = input("Enter the new task: ")
            task["task"] = new_task
            print("Task updated successfully!")
            return
    print("Task not found.")
def deletetask(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")


tasks=[]
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addtask(tasks)
        elif choice == "2":
            viewtask(tasks)
        elif choice == "3":
            updatetask(tasks)
        elif choice == "4":
            deletetask(tasks)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    
          
                
