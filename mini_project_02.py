while True:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    operation = input("Choose between +, -, *, / ")
    if operation == "+":
        print(first_num + second_num)
    elif operation == "-":
        print(first_num - second_num)
    elif operation == "*":
        print(first_num * second_num)
    elif operation == "/":
        print(first_num / second_num)
    else:
        break



"""while True:
    first_num = input("Enter first number (or 'quit' to exit): ")
    if first_num == "quit":
        print("Bye! 👋")
        break
    first_num = int(first_num)
    second_num = int(input("Enter second number: "))
    operation = input("Choose between +, -, *, /: ")
    
    if operation == "+":
        print(first_num + second_num)
    elif operation == "-":
        print(first_num - second_num)
    elif operation == "*":
        print(first_num * second_num)
    elif operation == "/":
        if second_num == 0:
            print("Can't divide by zero!")
        else:
            print(first_num / second_num)
    else:
        print("Invalid operation!")"""