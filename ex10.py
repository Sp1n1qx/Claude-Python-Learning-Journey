print("Shopping list manager\n")

item = []

def add():
    user_input = input("What to add? ")
    item.append(user_input)
    print(f"{user_input} has been added to the list!")
    print(f"current list: {item}\n")

def remove():
    print(f"current list {item}")
    user_input = input("What to remove? ")
    item.remove(user_input)
    print(f"{user_input} has been removed from the list!")
    print(f"current list: {item}\n")


while True:
    decision = input("Command (add/remove/show/quit): ")

    if decision == "add":
        add()
    elif decision == "remove" and item != []:
        remove()
    elif decision == "show":
        print(item)
    else:
        print("Goodbye!")
        break