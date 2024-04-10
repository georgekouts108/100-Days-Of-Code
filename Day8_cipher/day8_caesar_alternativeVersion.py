alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = """
          88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                   
"""

def caesar(msg, shift, direction):
    res = ""
    for i in range(len(msg)):
        if msg[i] in alphabet:
            original_index = alphabet.index(msg[i])
            new_index = (original_index - shift if direction=='D' else ((original_index + shift) % len(alphabet)))
            res += alphabet[new_index]
        else:
            res += msg[i]

    return res

print(logo)
print()

while True:
    choice = input("Type \'encode\' to encrypt or \'decode\' to decrypt:\n")

    if choice.upper() in ['DECODE', 'ENCODE']:
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        if shift > len(alphabet):
            shift %= len(alphabet)
        res = caesar(message,shift,choice[0].upper())
        print(f"The {choice}d text is {res}")
    else:
        print("Invalid input.")
    
    again = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n")
    if again.upper() == 'no'.upper():
        print("Goodbye")
        break
        
    
