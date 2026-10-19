shopping_list = []

while True:
    action = input("What do you want to do? (add / remove / show / done): ")

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Item added.")

    elif action == "remove":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        print("Shopping list:")
        for item in shopping_list:
            print(item)

    elif action == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")