student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(f"key = {key}, value = {value}")
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    print(f"index {index} -- row = {row.student}, {row.score}")
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {str(nato['letter'][i]): str(nato['code'][i]) for i in range(len(nato))}

print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
codes = [nato_dict[char.upper()] for char in word]
print(f'{word} --> {codes}')
