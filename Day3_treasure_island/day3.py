print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" : ")
print()
if direction.upper() == "left".upper():

    lake_choice = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat, or \"swim\" to swim across : ")

    if lake_choice.upper() == "swim".upper():
        print("Game Over.")

    elif lake_choice.upper() == "wait".upper():
        print()
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? : ")
        print()
        if door_color.upper() in ["red".upper(),"blue".upper()]:
            print("You entered a room of beasts. Game Over.")
            
        elif door_color.upper() == "yellow".upper():
            print("Congratulations!! You found the treasure and won the game!")
        
elif direction.upper() == "right".upper():
    print("You fell into a hole. Game Over.")
