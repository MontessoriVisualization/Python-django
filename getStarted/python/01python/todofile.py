# todo list to save on a file





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
    
          
                
