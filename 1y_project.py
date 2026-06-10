# make a escape/thinking game for my wife

# suspence time
import time as t
# cleaning spaces when too much has been writen
import os

# score
score = 0

# hints from lvl 2
lvl2_hint = {
    "hint 1": ("This is like the videos on tik tok you see someone putting letters as a meaning."),
    "hint 2": ("each Letter = one word")
}

# hints for lvl 3
lvl3_hint = {
    "hint 1": ("you can use those numbers to add, subract, divide and multiply\n but doesnt mean you need to use all of those."),
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
    print("To open the safe, enter 4 digit first last code.\n" \
    "hint: the month we met / the year we are * 16*14 * 30.")
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
            print("To open the safe, enter 4 digit code.\n" \
            "hint: the month we met + the year we are * 16*14 / 30.")

def lvl2():
    clear()
    print("You are in our house, and you forgot the code, what is the code?\n" \
    "hint: IWTMY\n" \
    "to get hints write .help.")
    while True:
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
                print()
            else:
                print(lvl2_hint["hint 2"])
                print("Answer:")
        elif answer == "hint 2":
            clear()
            print(lvl2_hint["hint 2"])
            print()
        else:
            clear()
            print("Try again")

def lvl3():
    clear()
    print("You need to find a math calculation to reach 08072025, how will you do?\n" \
    "hint: you only need this numbers;\n" \
    "2,3,5,7,271\n")
    while True:
        answer = input("Answer: ")
        if answer == "3*3 5*5 7*7 * 271":
            print("Correct!")
        else:
            choice = input("Do you want a hint? ")
            if choice.lower() == "yes":
                clear()
                print("You need to find a math calculation to reach 08072025, how will you do?\n" \
                "hint: you only need this numbers;\n" \
                "2,3,5,7,271\n")
                print(lvl3_hint["hint 1"])
            elif choice.lower() == "no":
                clear()
                print("You need to find a math calculation to reach 08072025, how will you do?\n" \
                "hint: you only need this numbers;\n" \
                "2,3,5,7,271\n")

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
    except ValueError:
        clear()
        print("Invalid Output!")
        print("Try again.\n")

# look discord for one inspiration

# for you to be able to find the answer i would sugest you to only use the multiply