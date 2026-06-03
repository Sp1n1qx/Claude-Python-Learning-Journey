score = 0

def ask_question(question, answer):
    user_question = input(question)
    if user_question == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        print(f"The answer was {answer}")
        return 0

score = score + ask_question("How old am i? ", "20")
score = score + ask_question("Color of sky? ", "blue")
score = score + ask_question("Who do i love the most? ", "wife")

print(f"Your score is: {score}!")