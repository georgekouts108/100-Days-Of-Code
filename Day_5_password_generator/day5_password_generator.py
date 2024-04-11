import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[',
    ']', '{', '}', ',', '.', '|', '<', '>', '/', '?', ';', ':', '`', '~'
]

print("Welcome to the password generator!")
letter_count = int(input("How many letters do you want in your pwd?\n"))
symbol_count = int(input("How many symbols do you want in your pwd?\n"))
number_count = int(input("How many numbers do you want in your pwd?\n"))

pwd_chars = []

for _ in range(letter_count):
    case = random.randint(0, 1)
    char = random.randint(0, len(letters) - 1)
    next_letter = letters[char].lower() if case == 0 else letters[char].upper()
    pwd_chars.append(next_letter)

for _ in range(symbol_count):
    pwd_chars.append(symbols[random.randint(0, len(symbols) - 1)])

for _ in range(number_count):
    pwd_chars.append(str(numbers[random.randint(0, len(numbers) - 1)]))

pwd = ""
while len(pwd_chars) > 0:
    index = random.randint(0, len(pwd_chars) - 1)
    pwd += pwd_chars[index]
    pwd_chars.pop(index)

print()
print(f"Your password is {pwd}")
