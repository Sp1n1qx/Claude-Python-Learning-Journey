import random

tries = 0
pc_guess = random.randint(1,20)
player_guess = int(input("Guess a number between 1-20: "))

while player_guess != pc_guess:
    player_guess = int(input("Guess a number between 1-20: "))
    if player_guess > pc_guess:
        print("Too high!")
        tries = tries + 1
    elif player_guess < pc_guess:
        print("Too low!")
        tries = tries + 1
    else:
        print(f"You got it with {tries} tries")

"""import random

tries = 0
pc_guess = random.randint(1, 20)

while True:
    player_guess = int(input("Guess a number between 1-20: "))
    tries = tries + 1
    if player_guess > pc_guess:
        print("Too high!")
    elif player_guess < pc_guess:
        print("Too low!")
    else:
        print(f"🎉 You got it in {tries} tries!")
        break"""