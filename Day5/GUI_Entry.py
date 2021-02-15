import tkinter

def randomFunction():
    global label
    entered = entry.get()
    label.configure(text=entered)

window = tkinter.Tk()
label = tkinter.Label(window, text="")
label.grid(column=0, row=2)
entry = tkinter.Entry(window, width=20)
entry.grid(column=0, row=1)

button = tkinter.Button(window, text='greet', fg='green', bg='grey', command=randomFunction)
button.grid(column=1, row=1)
window.geometry('500x300')
window.mainloop()