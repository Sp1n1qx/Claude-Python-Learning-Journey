names = []
grades = []

print("Student Grade Tracker\n")

def add():
    name = input("Student name: ")
    grade = int(input("Grade: "))
    print(f"{name} added with grade {grade}!\n")
    names.append(name)
    grades.append(grade)

def show():
    if names == [] and grades == []:
        print("No names or grades!")
    else:
        #needed help from claude, it was him who gave me this.
        for index, name in enumerate(names, 1):
            print(f"{index}. {name} - {grades[index-1]}")

def average():
    if names == [] or grades == []:
        print("No info")
    else:
        result = sum(grades) / len(grades)
        print(result)

def best():
    if names == [] or grades == []:
        print("No info")
    else:
        #needed help from claude, it was him who gave me most of this
        max_grade = max(grades)
        position = grades.index(max_grade)
        best_name = names[position]
        best_grade = grades[position]
        print(f"best student: {best_name} with {best_grade}")


while True:
    command = input("Command (add/show/average/best/quit): ")
    if command == "add":
        add()
    elif command == "show":
        show()
    elif command == "average":
        average()
    elif command == "best":
        best()
    elif command == "quit":
        break
    else:
        print("Invalid Output")