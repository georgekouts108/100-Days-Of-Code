def compute(num1, num2, oper):
    """
    Take two numbers and an operator symbol, and return the result of (num1 oper num2)
    """
    
    result = 0
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
        
    print(f"{num1} {oper} {num2} = {result}")
    
    return result
    

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

    result = compute(num1,num2,oper)

    choice = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ")
    

    
