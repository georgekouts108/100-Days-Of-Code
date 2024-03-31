letters = ['A', 'B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

logo = """

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   
"""

wrong1 = """
 _______
|/      |
|      (_)
|      
|       
|       
|
|___
"""
wrong2 = """
 _______
|/      |
|      (_)
|       |
|       
|      
|
|___
"""
wrong3 = """
 _______
|/      |
|      (_)
|      \|
|       
|      
|
|___
"""
wrong4 = """
 _______
|/      |
|      (_)
|      \|/
|       
|      
|
|___
"""
wrong5 = """
 _______
|/      |
|      (_)
|      \|/
|       |
|      
|
|___
"""
wrong6 = """
 _______
|/      |
|      (_)
|      \|/
|       |
|      /
|
|___
"""
wrong7 = """
 _______
|/      |
|      (_)
|      \|/
|       |
|      / \
|
|___
"""

def print_init_blanks(puzzle):
    blanks = ""
    for i in range(len(puzzle)):
        if puzzle[i] != ' ':
            blanks += '_ '
        else:
            blanks += '   '
    print(blanks)

def print_puzzle(puzzle, chars=[]):

    puzz = ""
    for i in range(len(puzzle)):
        if puzzle[i] != ' ':
            if puzzle[i] in chars:
                puzz += puzzle[i] + ' ' 
            else:
                puzz += '  '    
        else:
            puzz += '   '
    
    print(puzz)
    print_init_blanks(puzzle)

def is_puzzle_solved(puzzle, guesses):
    for i in range(len(puzzle)):
        if puzzle[i] != ' ' and puzzle[i] not in guesses:
            return False
        
    return True
            
##################################################################
##################################################################
print(logo)

lives_art = [wrong1, wrong2, wrong3, wrong4, wrong5, wrong6, wrong7]
incorrect_tries = 0
letters_guessed = []


puzzle = "PANAYIOTIS GIANOPOULOS"

while incorrect_tries < 8:
    
    if incorrect_tries > 0:
        print(lives_art[incorrect_tries - 1])
        
    print_puzzle(puzzle, chars=letters_guessed)

    if is_puzzle_solved(puzzle, letters_guessed):
        print("Congratulations! You solved the puzzle!")
        break
    
    letter_guess = (input("Guess a letter: ")).upper()
    if letter_guess not in letters_guessed:
        letters_guessed.append(letter_guess)
        
    if letter_guess not in puzzle:
        print("Sorry, there are no \'" + letter_guess + "\'s in the puzzle!")
        incorrect_tries += 1
        if incorrect_tries == 8:
            print("You lose!")

    print()
    print()
    
        
    
    
    
    
    

