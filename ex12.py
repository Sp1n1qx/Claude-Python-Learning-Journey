phone_book = {}

print("Phone book\n")

def add():
    name = input("Name: ")
    number = (input("Number: "))
    phone_book[name] = number
    print(f"{name} added!")

def search():
    name = input("Name: ")
    if name in phone_book:
        # this no, because it shows "{'937045829', 'Carla'}" and the other one is the correct!
        # it shows "Carla: 937045829"
        #print({phone_book[name], name})
        print(f"{name}: {phone_book[name]} 📞")
    else:
        print("Invalid")

def delete():
    name = input("Name: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} has been deleted")
    else:
        print("Invalid")

def show():
    if not phone_book:
        print("Nothing here.")
    else:
        for name, number in phone_book.items():
            print(f"{name}: {number}")

while True:
    command = input("Command (add/search/delete/show/quit): ")
    if command == "add":
        add()
    elif command == "search":
        search()
    elif command == "delete":
        delete()
    elif command == "show":
        show()
    elif command == "quit":
        break
    else:
        print("Invalid output!")