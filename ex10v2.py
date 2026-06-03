print("Shopping list manager\n")

item = []

def add():
    user_input = input("What to add? ")
    item.append(user_input)
    print(f"{user_input} has been added to the list!")
    for x, y in enumerate(item):
        print(1 + x, y)

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
    elif decision == "quit":
        print("Good Bye!")
        break
    else:
        print("Invalid command!")