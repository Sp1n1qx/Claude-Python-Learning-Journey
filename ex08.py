def Celcius(temperature):
    return (temperature * 9/5) + 32

def Fahrenheit(temperature):
    return (temperature - 32) * 5 / 9

print("Temperature converter")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius\n")

while True:
    choice = float(input("choose one option: "))
    temperature = float(input("Write the temperature: "))

    if choice == 1:
        print(Celcius(temperature))
    elif choice == 2:
        print(Fahrenheit(temperature))
    else:
        break



"""def celsius_to_fahrenheit(temperature):
    return (temperature * 9/5) + 32

def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5/9

print("Temperature Converter")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius\n")

while True:
    choice = input("Choose one option (or 'quit' to exit): ")
    if choice == "quit":
        print("Bye! 👋")
        break
    choice = int(choice)
    temperature = float(input("Write the temperature: "))

    if choice == 1:
        print(celsius_to_fahrenheit(temperature))
    elif choice == 2:
        print(fahrenheit_to_celsius(temperature))
    else:
        print("Invalid option!")"""