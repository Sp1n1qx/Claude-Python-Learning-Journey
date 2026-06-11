# make a escape/thinking game for my wife

# suspence time
import time as t
# cleaning spaces when too much has been writen
import os

# score
score = 0

# main hints from each lvl to save lines

lvl1_main_hint = {
    "hint": ("To open the safe, enter 4 digit first last code.\nhint: the month we met / the year we are * 16*14 * 30.")
}

lvl2_main_hint = {
    "hint": ("You are in our house, and you forgot the code, what is the code?\nhint: IWTMY\nto get hints write .help.")
}

lvl3_main_hint = {
    "hint": ("You need to find a math calculation to reach 08072025, how will you do?\nhint: you only need this numbers;\n2,3,5,7,271\n")
}

lvl4_main_hint = {
    "hint": ("My Dear Love, i have a puzzle for you.\nFind the 5 digit code.\n"
    "Digit 1 is a quarter of digit 5\n"
    "Digit 2 is equal to digit 5\n"
    "digit 3 is digit 2 - digit 1\n"
    "digit 4 is half of digit 2\n"
    "digit 5 = 4\n")
}

# hints from lvl 2
lvl2_hint = {
    "hint 1": ("This is like the videos on tik tok you see someone putting letters as a meaning."),
    "hint 2": ("each Letter = one word")
}

# hints for lvl 3
lvl3_hint = {
    "hint 1": ("you can use those numbers to add, subract, divide and multiply\nbut doesnt mean you need to use all of those."),
    "hint 2": ("use only one of those 4 options")
}

# name of the game
print("Escape and Think...")
# wait time
t.sleep(0.3)

# funtion to clear screen
def clear():
    os.system('cls')

# function to show all levels available
def show():
    for x in range(5):
        print("lvl", x + 1)
        t.sleep(0.3)

# lvl 1
def lvl1():
    clear()
    print(lvl1_main_hint["hint"])
    # while doesnt get right, try to answer again
    while True:
        answer = input("Answer Here: ")
        if answer == "2398":
            print("Good job darling!")
            return 1
        else:
            clear()
            # if not right show prompt to try again 
            print("Try again.\n")
            print(lvl1_main_hint["hint"])

def lvl2():
    clear()
    while True:
        print(lvl2_main_hint["hint"])
        answer = input("Say Answer/Get Help here: ")
        if answer.upper() == "I WANT TO MARRY YOU":
            print("Good Girl.")
            return 1
        elif answer == "help":
            clear()
            answer = input("choose your hint, 1-3\n"
            "write like hint 1/etc... \n")
        elif answer == "hint 1":
            clear()
            print(lvl2_hint["hint 1"])
            print()
            answer = input("Would you like to see the next hint? (yes/no) ")
            if answer.lower() == "no":
                pass
            else:
                print(lvl2_hint["hint 2"])
                print("Answer:")
        elif answer == "hint 2":
            clear()
            print(lvl2_hint["hint 2"])
            print()
        else:
            clear()

def lvl3():
    clear()
    print(lvl3_main_hint["hint"])
    while True:
        answer = input("Answer: ")
        if answer == "3*3 + 5*5 + 7*7 * 271" or answer == "3*3+5*5+7*7*271":
            print("Correct!")
        else:
            choice = input("Do you want a hint? ")
            if choice.lower() == "yes":
                choice = int(input("How many? (1-2)"))
                if choice == 1:
                    clear()
                    print(lvl3_hint["hint 1"])
                else:
                    clear()
                    print(lvl3_main_hint["hint"])
                    print(f"hint 1: {lvl3_hint["hint 1"]}")
                    print()
                    print(f"hint 2: {lvl3_hint["hint 2"]}")
            elif choice.lower() == "no":
                clear()
                print(lvl3_main_hint["hint"])

def lvl4():
    clear()
    print(lvl4_main_hint["hint"])
    while True:
        answer = input("Answer: ")
        if answer == "14324":
            clear()
            print("Correct.")
            print("Part 2\n")
            print("Those numbers have meanings, try to find what it says.")
            print("Number is 14324")
            meaning = input("Answer: ")
            if meaning.upper() == "I LOVE YOU FOREVER":
                print("Good job Sweet Heart.\n" \
                "Almost at the end.")
        else:
            hint = input("Want a hint? ")
            if hint.lower() == "yes":
                print("\nIf you say it out loud, it takes 5 syllables. If you write it down, the length of each word matches the code. What am I trying to tell you?")
            elif hint.lower() == "no":
                pass

show()

while True:
    try:
        choice = int(input("choose your lvl (1-5): "))
        if choice == 1:
            lvl1()
        elif choice == 2:
            lvl2()
        elif choice == 3:
            lvl3()
        elif choice == 4:
            lvl4()
    except ValueError:
        clear()
        print("Invalid Output!")
        print("Try again.\n")

# look discord for one inspiration

# for you to be able to find the answer i would sugest you to only use the multiply