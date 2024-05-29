import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("My First GUI App")
window.minsize(width=500, height=500)

text1 = tkinter.Label(text="this is new text", font=('Arial', 14, 'bold'))
text1.pack()

button1 = tkinter.Button(text='Click Me', font=('Arial', 14, 'normal'))
button1.pack()

entry1 = tkinter.Entry(width=25)
entry1.pack()

text1 = tkinter.Text(width=30, height=5)
text1.focus()
text1.insert(END, 'Your text here...')
print(text1.get('1.0', END))
text1.pack()

spinbox = tkinter.Spinbox(from_=0, to=100, width=5)
spinbox.pack()

scale = tkinter.Scale(from_=100, to=0)
scale.pack()

checkbox = tkinter.Checkbutton(text='Is On?')
checkbox.pack()

radio_state = tkinter.IntVar()
radiobtn1 = tkinter.Radiobutton(text='option 1', variable=radio_state, value=1)
radiobtn2 = tkinter.Radiobutton(text='option 2', variable=radio_state, value=2)
radiobtn1.pack()
radiobtn2.pack()

listbox = tkinter.Listbox(height=4)
movies = ['Annabelle', 'The Wizard of Oz', 'The Chronicles of Narnia', 'In A Violent Nature', 'Terrifier 2', 'Mortal Kombat', 'White Christmas']
for m in range(len(movies)):
    listbox.insert(m, movies[m])
listbox.pack()


window.mainloop()