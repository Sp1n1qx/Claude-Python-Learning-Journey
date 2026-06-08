# time of suspence
import time as t

# make a escape/thinking game for my wife
# score
score: int = 0

# name of the game
print("Escape and Think...\n")
t.sleep(0.3)

def show():
    for x in range(5):
        print("lvl",x + 1)
        t.sleep(0.3)

def lvl1():
    print("To open the safe, enter 4 digit first last code.\n" \
    "hint: the month we met / the year we are * 16*14 * 30.")
    while True:
        answer = input()
        if answer == "2398":
            print("Good job.")
            return 1
        else:
            print("Try again.\n")
            print("To open the safe, enter 4 digit code.\n" \
            "hint: the month we met + the year we are * 16*14 / 30.")
        
def lvl2():
    print("You are in our house, and you forgot the code, what is the code?\n" \
    "hint: IWTMY\n")
    while True:
        answer = input()
        if answer.upper() == "I WANT TO MARRY YOU":
            print("Good Girl.")
            return 1
        elif answer == "2":
            print("This is like the videos on tik tok you see someone putting letters as a meaning.")
        elif answer == "3":
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