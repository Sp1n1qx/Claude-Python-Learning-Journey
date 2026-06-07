# time of suspence
import time as t

# make a escape/thinking game for my wife
# score
score = 0

# name of the game
print("Escape and Think...\n")
t.sleep(0.3)

def show():
    for x in range(5):
        print("lvl",x + 1)
        t.sleep(0.3)

def lvl1():
    print("To open the safe, enter 4 digit code.\n" \
    "hint: the month we met + the year we are * 16*14 / 30.")
    answer = int(input())
    if answer == 2034:
        print("Good job.")
    else:
        print("Try again.")

show()
choice = input("choose your lvl: ")
if choice == "1":
    lvl1()
#needs a "if see answers print answers, if not try again" type of thing, so she would decide if she wants or no