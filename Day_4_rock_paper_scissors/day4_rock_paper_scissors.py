import random
you = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS: "))
cpu = random.randint(0,2)
print()
dic = {0:'ROCK', 1:'PAPER',2:'SCISSORS'}
print(f"YOU picked {dic[you]}")
print(f"CPU picked {dic[cpu]}")
print()
if you == cpu:
    print("tie")
elif you == 0:
    if cpu == 1:
        print("you lose")
    else:
        print("you win!")
elif you == 1:
    if cpu == 2:
        print("you lose")
    else:
        print("you win!")
elif you == 2:
    if cpu == 0:
        print("you lose")
    else:
        print("you win!")
        
    



