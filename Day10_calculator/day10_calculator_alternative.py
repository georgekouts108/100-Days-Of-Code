logo ="""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

ops = {'+':add, '-':subtract, '*':multiply, '/':divide}


print(logo)

result = 0
choice = 'n'
while True:
    num1 = 0
    if choice == 'n':
        num1 = float(input("What's the first number? : "))
        for op in ['+','-','*','/']:
            print(op)
    elif choice == 'y':
        num1 = result
        
    oper = input("Pick an operation: ")
    num2 = float(input("What's the next number? : "))

    result = ops[oper](num1,num2)
    print(f"{num1} {oper} {num2} = {result}")

    choice = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ")
    

    
