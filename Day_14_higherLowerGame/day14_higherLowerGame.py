import random
from day14_gameData import data

logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""
 
 
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def formatChoice(obj):
    return f"{obj['name']}, a(n) {obj['description']}, based in {obj['country']}"
    
def game():
    score = 0

    choiceA = random.choice(data)
    choiceB = random.choice(data)

    winner = None
    
    while True:
        print("=" * (11+max(len(formatChoice(choiceA)),len(formatChoice(choiceB)))))
        print(f"Compare A: {formatChoice(choiceA)}.")
        print(vs)
        print(f"Against B: {formatChoice(choiceB)}.\n")

        guess = input("Which/Who has more followers? Type \'A\' or \'B\': ")
        print("\n")
        guessed_right = False
        if guess.upper() == 'A':
            if choiceA['follower_count'] >= choiceB['follower_count']:
                guessed_right = True
                winner = choiceA
                
        elif guess.upper() == 'B':
            if choiceB['follower_count'] >= choiceA['follower_count']:
                guessed_right = True
                winner = choiceB

        if not guessed_right:
            print("Game over!")
            print(f"Sorry, that's wrong! Final score = {score} points.")
            break

        score += 1

        print(f"You're right! Current score: {score}.\n")
        print("=" * (11+max(len(formatChoice(choiceA)),len(formatChoice(choiceB)))))
        
        if winner == choiceB:
            choiceA = choiceB
            
        choiceB = random.choice(data)      
    

print(logo)
game()

