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

# maybe hints for lvl 3? idk yet

# name of the game
print("Escape and Think...\n")
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
    print("To open the safe, enter 4 digit first last code.\n" \
    "hint: the month we met / the year we are * 16*14 * 30.")
    # while doesnt get right, try to answer again
    while True:
        answer = input()
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
    print("You are in our house, and you forgot the code, what is the code?\n" \
    "hint: IWTMY\n" \
    "to get hints write .help.")
    while True:
        answer = input()
        if answer.upper() == "I WANT TO MARRY YOU":
            print("Good Girl.")
            return 1
        elif answer == "help":
            clear()
            answer = input("choose your hint, 1-3\n"
            "write like hint 1/etc... ")
        if answer == "hint 1":
            print(lvl2_hint["hint 1"])
            print()
            answer = input("Would you like to see the next hint? (yes/no) ")
            if answer.lower() == "no":
                print("Answer: ")
            else:
                print(lvl2_hint["hint 2"])

show()

choice = input("choose your lvl: ")
if choice == "1":
    lvl1()
elif choice == "2":
    lvl2()

# needs a "if see answers print answers, if not try again" type of thing, so she would decide if she wants or no


# need to use dictionary for hints, need function to clear
# add "import os" to use as os.system("clear"), and comment more on the code.

# look discord for one inspiration