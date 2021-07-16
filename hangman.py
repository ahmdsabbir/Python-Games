import random

with open("words.txt") as file:
    lines = file.readlines()
    word = random.choice(lines)
    word = word.rstrip("\n").lower()

for index,char in enumerate(word):
    if index == 0:
        print(f"{char.upper()}", end="")
    else:
        print(f" _", end="")

correct_letters = ""
wrong_inputs = 0
threshold = 5

while True:
    user_choice = input(f" Guess the {len(word)} letter word: ").lower()
    if len(user_choice) > 1:
        if user_choice == word:
            print(f" WOW! You got the word at once! Yes the word is {word}")
            break
        else:
            print(f" You Lost! The word was {word}")
            break
    elif len(user_choice) == 1:
        if user_choice in word:
            print(f" Correct! {user_choice} appears in the secret word")
            correct_letters += user_choice
        else:
            print(f" You Guessed wrong and have {threshold}/{wrong_inputs} guesses left")
            wrong_inputs += 1

    if wrong_inputs >= threshold:
        print(f"Too many Wrong Guesses. You Loose. The Word was {word}")

    for index,char in enumerate(word):
        if index == 0:
            print(f" {char.upper()}", end="")
        elif char in correct_letters:
            print(f" {char}", end="")
        else:
            print(f" _", end="")
    
