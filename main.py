# dito nag store ng task
task_storage = []


# Adrian - view feature (DONE)
def display_tasks():
    if not task_storage:
        print("\nNo tasks yet!")
        return False

    print("\n----- YOUR TASKS -----")
    for i, task in enumerate(task_storage, start=1):
        print(f"{i}. {task}")
    print("-----------------------")
    return True


# Cassey - Gawa ka dito ng function na mag a-add ng task as string sa task_storage
def add_task():
    task_name = input("\nEnter the task to add: ").strip()
    if task_name:
        task_storage.append(task_name)
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task cannot be empty.")

# Joab - Gawa ka dito ng function na mag a-update or edit ng mga task
def edit_task():
    if not display_tasks():
        return
   
    try:
        task_num = int(input("\nEnter the number of the task you want to edit: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Enter the new task description: ").strip()
            if new_name:
                old_name = tasks[task_num - 1]
                tasks[task_num - 1] = new_name
                print(f"Updated '{old_name}' to '{new_name}'.")
            else:
                print("Task description cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")