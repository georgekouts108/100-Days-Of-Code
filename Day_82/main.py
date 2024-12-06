
# In the MORSE dictionary, there is a list of numbers for each character.
# Positive numbers indicate dots, whereas negative numbers indicate dashes.
# The absolute value of the number indicates the quantity of the symbol to print.

# EXAMPLE 1: for 'L' write 1 dot, then 1 dash, then 2 dots
# EXAMPLE 2: for 'V' write 3 dots, then 1 dash
# EXAMPLE 3: for 'C' write 1 dash, then 1 dot, then 1 dash, then 1 dot

MORSE = {
    'A': [1, -1], 'B': [-1, 3], 'C': [-1, 1, -1, 1], 'D': [-1, 2], 'E': [1],
    'F': [2, -1, 1], 'G': [-2, 1], 'H': [4], 'I': [2], 'J': [1, -3], 'K': [-1, 1, -1],
    'L': [1, -1, 2], 'M': [-2], 'N': [-1, 1], 'O': [-3], 'P': [1, -2, 1], 'Q': [-2, 1, -1],
    'R': [1, -1, 1], 'S': [3], 'T': [-1], 'U': [2, -1], 'V': [3, -1], 'W': [1, -2],
    'X': [-1, 2, -1], 'Y': [-1, 1, -2], 'Z': [-2, 2], '1': [1, -4], '2': [2, -3],
    '3': [3, -2], '4': [4, -1], '5': [5], '6': [-1, 4], '7': [-2, 3], '8': [-3, 2],
    '9': [-4, 1], '0': [-5]
}

DOT = '⏺'
DASH = '▬▬▬'


def morse_lang(units):
    morse = ''
    for u in range(len(units)):
        _type = DOT if units[u] > 0 else DASH
        _count = int(abs(units[u]))
        _temp = ''
        for c in range(_count):
            _temp += f'{_type}'
        morse += _temp

    return morse


def morse_translation(text):
    translation = ''
    words = text.upper().split(' ')
    for w in range(len(words)):
        word_translation = ''
        chars = [char for char in words[w]]
        for c in range(len(chars)):
            word_translation += morse_lang(MORSE[chars[c]])
            if c != len(chars) - 1:
                word_translation += ' '

        translation += word_translation + ((' ' * 7) if w != len(words) - 1 else '')

    return translation


string = input('Enter text to translate: ')
print('\nMorse code translation:\n')
x = morse_translation(string)
print(x)
