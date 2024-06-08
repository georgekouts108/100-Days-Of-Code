from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

WHITE = '#FFFFFF'
BLACK = '#000000'
letters = [chr(i) for i in range(65, 65 + 26)] + [chr(i) for i in range(97, 97 + 26)]
numbers = [str(n) for n in range(0, 10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd_field.delete(0, END)
    pwd = ""
    letter_count = random.randint(8, 10)
    number_count = random.randint(2, 4)
    symbol_count = random.randint(2, 4)

    while True:
        char_type = random.randint(1, 3)
        if char_type == 1 and letter_count > 0:
            letter_count -= 1
            pwd += random.choice(letters)
        elif char_type == 2 and number_count > 0:
            number_count -= 1
            pwd += random.choice(numbers)
        elif char_type == 3 and symbol_count > 0:
            symbol_count -= 1
            pwd += random.choice(symbols)

        if letter_count == 0 and number_count == 0 and symbol_count == 0:
            break

    pwd_field.insert(0, pwd)
    messagebox.showinfo(title="Password Copied", message=f"The password\n\"{pwd}\"\nhas been copied to clipboard.")
    pyperclip.copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = website_field.get()
    email = email_field.get()
    pwd = pwd_field.get()

    new_data = {
        site: {
            'email': email,
            'password': pwd
        }
    }

    if (not site) or (not email) or (not pwd):
        messagebox.showerror(title="Error", message="ERROR: One or more fields are empty.")
    else:
        box_msg = f"These are the details entered:\nEmail: {email}\nPassword: {pwd}\n\nOK to save?"
        is_ok = messagebox.askokcancel(title=site, message=box_msg)
        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                pwd_field.delete(0, END)
                email_field.delete(0, END)
                website_field.delete(0, END)

def search_site():
    site_req = website_field.get()
    if site_req:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
                if site_req in list(data.keys()):
                    email, pwd = (data[site_req]['email'], data[site_req]['password'])
                    messagebox.showinfo(message=f"Website: {site_req}\n\nEmail: {email}\nPassword: {pwd}")
                else:
                    messagebox.showinfo(message=f"Website '{site_req}' not found.")
        except Exception:
            pass
    else:
        messagebox.showinfo(message=f"No website to search for.")

window = Tk()
window.title("Password Manager")
window.config(width=700, height=600, padx=20, pady=20, bg='#ffffff')
window.wm_minsize(500,350)
window.resizable = False

canvas = Canvas(bg='#FFFFFF', highlightthickness=0, width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1, columnspan=2)

website_lbl = Label(text='Website:', bg=WHITE, fg=BLACK)
website_lbl.grid(column=1, row=2)
website_field = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=21)
website_field.grid(column=2, row=2, columnspan=2)

search_site_btn = Button(text='Search Website', highlightthickness=0, command=search_site, width=13)
search_site_btn.grid(column=4, row=2)

email_lbl = Label(text='Email/Username:', bg=WHITE, fg=BLACK)
email_lbl.grid(column=1, row=3)
email_field = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=35)
email_field.grid(column=2, row=3, columnspan=2)

pwd_lbl = Label(text='Password:', bg=WHITE, fg=BLACK)
pwd_lbl.grid(column=1, row=4)
pwd_field = Entry(bg=WHITE, fg=BLACK, highlightthickness=0, width=21)
pwd_field.grid(column=2, row=4)

gen_pwd_btn = Button(text='Generate Password', highlightthickness=0, command=generate_pwd)
gen_pwd_btn.grid(column=3, row=4)

add_btn = Button(text='Add', highlightthickness=0, width=36, command=save)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()