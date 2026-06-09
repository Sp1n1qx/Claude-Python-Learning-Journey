# time of suspence
import time as t
# cleaning spaces when much much has been writen
import os as clean

# make a escape/thinking game for my wife
# score
score: int = 0

# name of the game
print("Escape and Think...\n")
# wait time
t.sleep(0.3)

# function to show all levels available
def show():
    for x in range(5):
        print("lvl", x + 1)
        t.sleep(0.3)

# lvl 1
def lvl1():
    print("To open the safe, enter 4 digit first last code.\n" \
    "hint: the month we met / the year we are * 16*14 * 30.")
    # while doesnt get right, try to answer
    while True:
        answer = input()
        if answer == "2398":
            print("Good job darling!")
            return 1
        else:
            # if not right show prompt and to try again 
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
            answer = input("choose your hint, 1-3\n"
            "write like hint 1/etc... ")
            if answer == "hint 1":
                print("This is like the videos on tik tok you see someone putting letters as a meaning.\n" \
                "IWTMY")
                answer = input("Do you want the other hint for now or no? ")
                if answer == "no":
                    print("IWTMY")
                elif answer == "yes":
                    print("You are in our house, and you forgot the code, what is the code?\n" \
                    "hint: IWTMY\n" \
                    "each Letter = one word")
            elif answer == "hint 2":
                print("You are in our house, and you forgot the code, what is the code?\n" \
                "hint: IWTMY\n" \
                "each Letter = one word")

show()

choice = input("choose your lvl: ")
if choice == "1":
    lvl1()
elif choice == "2":
    lvl2()

#needs a "if see answers print answers, if not try again" type of thing, so she would decide if she wants or no


#need to use dictionary for hints
# add "import os" to use as os.system("clear"), and comment more on the code.