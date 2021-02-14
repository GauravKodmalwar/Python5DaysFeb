import tkinter

window = tkinter.Tk()
def validate():
    global label
    value = state.get()
    label.configure(text=value)

state = tkinter.BooleanVar()
state.set(False)
# Radiobutton value should be unique and var/variable used to store value
rad1 = tkinter.Radiobutton(window, text='Red', value=1, var=state)
rad2 = tkinter.Radiobutton(window, text='Orange', value=2, var=state)
rad3 = tkinter.Radiobutton(window, text='Green', value=3, var=state)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
button = tkinter.Button(window, text="OK", command=validate)
label = tkinter.Label(window)
label.grid(column=1, row=2)
button.grid(column=2,row=2)
window.geometry('500x300')
window.mainloop()