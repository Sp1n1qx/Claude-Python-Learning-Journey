# suspence
import time as t

# make a escape/thinking game for my wife
# score
score = 0

# name of the game
print("Escape and Think...\n")
t.sleep(0.3)
# print and then input on each question

def show():
    print("Lvl 1")
    t.sleep(0.3)
    print("Lvl 2")
    t.sleep(0.3)
    print("Lvl 3")
    t.sleep(0.3)
    print("Lvl 4")
    t.sleep(0.3)
    print("Lvl 5\n")

while True:
    show()
    choice = input("choose your lvl: ")
    if choice == "1":
        print("To open the safe, enter 4 digit code.\n" \
        "hint: the month we met + the year we are * 16*14 / 30.")
        answer = int(input())
        if answer == 2034:
            score = score + 1
            print("Good job.")
            print(f"this is your score: {score}")
        else:
            print("Try again.")
            print(f"this is your score: {score}")

#needs a "if see answers print answers, if not try again" type of thing, so she would decide if she wants or no