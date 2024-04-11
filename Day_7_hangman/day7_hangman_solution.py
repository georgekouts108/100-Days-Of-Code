import random
from day7_hangman_art import logo, stages
from day7_hangman_words import word_list
            
##################################################################

print(logo)

incorrect_tries = 0
chosen_word = random.choice(word_list).lower()

display = []
for _ in range(len(chosen_word)):
    display += '_' # same as display.append('_')

game_over = False

while not game_over:
    if incorrect_tries > 0:
        print(stages[-incorrect_tries])

    print(f"{' '.join(display)}")
    
    guess = (input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You've already guessed \'{guess}\'")
    else:
        letter_not_there = True
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                letter_not_there = False
                display[i] = chosen_word[i]

        if letter_not_there:
            print(f"You guessed \'{guess}\', that\'s not in the word. You lose a life.")

        if letter_not_there:
            incorrect_tries += 1
            if incorrect_tries > 7:
                print("You lose!")
                print("The answer: "+chosen_word)
                game_over = True

    if '_' not in display:
        print("You win!")
        print("The answer: "+chosen_word)
        game_over = True
