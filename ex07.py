print("Grades\n")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
while True:  
    print(get_grade(int(input("NOTA: "))))



"""print("Grades\n")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

while True:
    score = input("Enter a score (or 'quit' to exit): ")
    if score == "quit":
        print("Bye! 👋")
        break
    print(get_grade(int(score)))"""