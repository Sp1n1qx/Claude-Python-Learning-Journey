print("Calculator\n")
def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

while True:
    num01 = input("First num (write quit to quit the program): ")
    if num01 == "quit":
        break
    num01 = int(input("First num (write quit to quit the program): "))
    num02 = int(input("Second num: "))
    symbol = input("Choose from +, -, *, / ")

    if symbol == "+":
        print(add(num01, num02))
    elif symbol == "-":
        print(subtract(num01, num02))
    elif symbol == "*":
        print(multiply(num01, num02))
    elif symbol == "/":
        print(divide(num01, num02))
    else:
        break



"""print("Calculator\n")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by zero!"
    return x / y

while True:
    num01 = input("First num (write quit to quit the program): ")
    if num01 == "quit":
        break
    num01 = int(num01)
    num02 = int(input("Second num: "))
    symbol = input("Choose from +, -, *, /: ")

    if symbol == "+":
        print(add(num01, num02))
    elif symbol == "-":
        print(subtract(num01, num02))
    elif symbol == "*":
        print(multiply(num01, num02))
    elif symbol == "/":
        print(divide(num01, num02))
    else:
        print("Invalid operation!")"""