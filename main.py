# dito nag store ng task
task_storage = []

# Adrian - Gawa ka dito ng function na mag display ng mga TASK with proper system.

# Cassey  - Gawa ka dito ng function na mag a-add ng task as string sa task_storage

# Joab - Gawa ka dito ng function na mag a-update or edit ng mga task

# Kian - ako na sa menu and yung loop and remove task

def remove_task():
    if not display_tasks():
        return
    
    try:
        task_num = int(input("\nEnter the number of the task you want to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: '{removed}'")
    except (ValueError, IndexError):
        print("Invalid choice or number.")


def menu()
    while True:
        print("/n===SIMPLE TASK MANAGER===")
        print("/n--------MENU--------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit") 
        print("----------------------")

        choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
            view_tasks() #FUNCTION NAME MO TO ADRIAN
            elif choice == '2':
            add_task() #FUNCTION NAME MO TO CASSEY
            elif choice == '3':
            edit_task() #FUNCTION NAME MO TO JOAB
            elif choice == '4':
            remove_task()
            elif choice == '5':
                print("Thank You!")
                break
            else:
                print("!!!Invalid Choice, Choose 1 - 5 only!!!")


if __name__ == "__main__":
    main()