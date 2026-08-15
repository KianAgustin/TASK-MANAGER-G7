# Hi
user_list = []

print("Add a Task!")
print("Type what you want to add. Just type 'done' to finish.\n")

while True:
    new_item = input("Enter a Task: ").strip()
    
    if new_item.lower() == 'done':
        break 
        
 
    if new_item == "":
        print("Please type a valid item!")
        continue 
        
    user_list.append(new_item)
    print(f" Added '{new_item}'. Current list size: {len(user_list)}")

print("\n--- Your Final List ---")
print(user_list)