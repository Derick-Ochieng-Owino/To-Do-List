todo = []

print("What do you want to do? ")
print("1. Add an item.")
print("2. Edit an item.")
print("3. Delete an item.")
print("4. Delete every item.")
print("6. Show list of all items.")
choice = int(input("Enter a choice: "))

if choice == 1:
    todo.append(input("Enter a new item: "))
    print("Updated List: ",todo)
elif choice == 2:
    print("")
elif choice == 3:
    print("")
elif choice == 4:
    print("")
elif choice == 5:
    print("")
elif choice == 6:
    print("Item List. ", todo)