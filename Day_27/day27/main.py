import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
window.title("My First GUI App")
window.minsize(width=500, height=500)

# labels
label1 = tkinter.Label(text="I'm a label!", font=('Times New Roman', 24, 'bold'))
label1.pack()
label1['text'] = 'New text'


# buttons
def btn_clicked():
    label1.config(text=input.get())


button = tkinter.Button(text="I'm a button!", font=('Times New Roman', 24, 'bold'), command=btn_clicked)
button.pack()

# entry (text input field)
input = tkinter.Entry()
input.pack()

# color picker
color_code = ''
def choose_color():
    color_code = colorchooser.askcolor(title='pick a color')
    print(color_code[1])

color_button = tkinter.Button(text='choose a color', command=choose_color)
color_button.place(x=100, y=450)



window.mainloop()
