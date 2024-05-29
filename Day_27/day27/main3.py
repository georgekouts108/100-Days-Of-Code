import tkinter

window = tkinter.Tk()
window.title("My First GUI App")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

label1 = tkinter.Label(text="LABEL")
label1.grid(column=1, row=1)

button1 = tkinter.Button(text="BUTTON")
button1.grid(column=2, row=2)

button2 = tkinter.Button(text="NEW BUTTON")
button2.grid(column=3, row=1)

entry1 = tkinter.Entry()
entry1.grid(column=4, row=3)

window.mainloop()