from tkinter import *
from random import *
import pandas as pd
import csv

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# -------------------------------- MANIPULATING THE DATA -------------------------- #
data = {}
try:
    data = pd.read_csv('data/words_to_learn.csv').to_dict()
except Exception:
    data = pd.read_csv('data/french_words.csv').to_dict()

french = data['French']
english = data['English']

translations = {}
for i in range(len(french)):
    translations[french[i]] = english[i]

current_card = {}


def next_card_right():
    global translations
    del translations[current_card['French']]
    get_next_card()


def get_next_card():
    global translations
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    try:
        with open('data/words_to_learn.csv', 'w') as file:
            csv.writer(file).writerow(['French', 'English'])
            for fr_word in translations:
                csv.writer(file).writerow([fr_word, translations[fr_word]])
    except Exception:
        pass

    french_word = choice(list(translations.keys()))
    english_version = translations[french_word]
    current_card['French'] = french_word
    current_card['English'] = english_version

    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=french_word, fill='black')
    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    global translations
    global current_card
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='#ffffff')
    canvas.itemconfig(card_word, text=current_card['English'], fill='#ffffff')


# -------------------------------- CREATING THE UI -------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=flip_card)

wrong_icon = PhotoImage(file='images/wrong.png')
right_icon = PhotoImage(file='images/right.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')

canvas = Canvas(width=800, height=526)
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=LANGUAGE_FONT, fill='#000000')
card_word = canvas.create_text(400, 263, text='', font=WORD_FONT, fill='#000000')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

button_wrong = Button(image=wrong_icon, highlightthickness=0, borderwidth=0, command=get_next_card)
button_wrong.grid(row=1, column=0)

button_right = Button(image=right_icon, highlightthickness=0, borderwidth=0, command=next_card_right)
button_right.grid(row=1, column=1)

get_next_card()

window.mainloop()
