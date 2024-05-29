import tkinter

window = tkinter.Tk()
window.title("My First GUI App")
window.minsize(width=250, height=120)
window.config(padx=20, pady=20)
window.resizable=False


# input
entry = tkinter.Entry(width=10)
entry.grid(column=2, row=1)

# labels
lb_miles = tkinter.Label(text="Miles")
lb_miles.grid(column=3, row=1)

lb_iseqto = tkinter.Label(text="is equal to")
lb_iseqto.grid(column=1, row=2)

lb_result = tkinter.Label(text="0")
lb_result.grid(column=2, row=2)

lb_km = tkinter.Label(text="Km")
lb_km.grid(column=3, row=2)


# buttons
def miles_to_km():
    good = True
    for i in entry.get():
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            good = False
            break

    if good:
        lb_result.config(text=str(float(entry.get()) * 1.61))


btn_calculate = tkinter.Button(text="Calculate", command=miles_to_km)
btn_calculate.grid(column=2, row=3)

window.mainloop()
