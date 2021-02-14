import tkinter

window = tkinter.Tk()

txt = tkinter.Entry(window, width=20)
txt.grid(column=0, row=1)

def clicked():
    global label
    output = 'Welcome, ' + txt.get()
    label.configure(text=output)

button = tkinter.Button(window, text='Greet', fg='green', bg='grey', command=clicked)
button.grid(column=0, row=2)
label = tkinter.Label(window)
label.grid(column=1, row=1)
window.geometry('900x500')
window.mainloop()