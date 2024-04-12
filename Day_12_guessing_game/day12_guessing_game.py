import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1,100)

difficulty = ''
while True:
    difficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
    if difficulty.lower() in ['easy','hard']:
        break
    else:
        print("Invalid choice.")

guesses = 5 if difficulty.lower() == 'hard' else 10

while guesses > 0:
    print(f"\nYou have {guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"You got it! The answer was {answer}")
        break
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")

    print("Guess again.")
    guesses -= 1

if guesses == 0:
    print(f"You've run out of guesses, you lose.\nThe answer was {answer}")
