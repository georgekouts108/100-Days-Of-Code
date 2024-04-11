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


def encrypt(msg, shift):
    res = ""
    for i in range(len(msg)):
        if msg[i] != ' ':
            original_index = alphabet.index(msg[i])
            new_index = (original_index + shift) % len(alphabet)
            res += alphabet[new_index]
        else:
            res += ' '
    return res

def decrypt(msg, shift):
    res = ""
    for i in range(len(msg)):
        if msg[i] != ' ':
            original_index = alphabet.index(msg[i])
            new_index = original_index - shift
            res += alphabet[new_index]
        else:
            res += ' '
    return res

print(logo)
print()

while True:
    choice = input("Type \'encode\' to encrypt or \'decode\' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    
    if choice.upper() == 'encode'.upper():
        print("Here\'s the encoded result:", encrypt(message,shift))

    elif choice.upper() == 'decode'.upper():
        print("Here\'s the encoded result:", decrypt(message,shift))

    again = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n")
    if again.upper() == 'no'.upper():
        break
        
    
