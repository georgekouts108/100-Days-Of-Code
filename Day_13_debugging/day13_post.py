# Describe Problem -- This was buggy because the string would never be printed since 20 is excluded in range(x, 20)
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug -- This was buggy because randint(x,y) means the range [x, y], leading to a potential index out of bounds error
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num - 1])

# Play Computer -- This was buggy because there was no case for year == 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors -- This was buggy because the print method is not in the 'if' block, and you need an f-string to see the age. Also, input() is string by default.
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

#Print is Your Friend -- This was buggy because 'word_per_page' isn't actually assigned due to a syntax error
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

Use a Debugger -- This was buggy because the line for appending to b_list was out of scope of the for loop
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
