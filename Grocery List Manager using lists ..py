# Write a program to create a simple Grocery List Manager using lists.


# Grocery List Manager using lists :-


# In this projects users can :-

# 1.Add Items
# 2.Remove Items
# 3.Display all Items

grocery_list = []

print("Grocery List Manager")
while True:
    print("\nOptions: add / remove / show / exit")
    
    action = input("What would you like to do? ").strip().lower()

    if action == "add":
        item = input("Enter item you want to add: ")
        grocery_list.append(item)
        print(item, "added")

    elif action == "remove":
        item = input("Enter item you want to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(item, "removed")
        else:
            print("Item not found")

    elif action == "show":
        print("Your Grocery List:")
        for i in grocery_list:
            print("-", i)

    elif action == "exit":
        print("Thank you for using Grocery List Manager app.")
        break

    else:
        print("Invalid option")
