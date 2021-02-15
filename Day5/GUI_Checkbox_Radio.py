import tkinter

window = tkinter.Tk()
# widgets variables
def clicked():
    global state, label
    label.configure(text=state.get())

state = tkinter.BooleanVar()
state.set(True)
check1 = tkinter.Checkbutton(text='English', var=state)
check2 = tkinter.Checkbutton(text='Hindi')
check3 = tkinter.Checkbutton(text='French')
label = tkinter.Label(window, text="")
label.pack()
button = tkinter.Button(window, text='greet', fg='green', bg='grey', command=clicked)
button.pack()
check1.pack()
check2.pack()
check3.pack()

# Radio
state2 = tkinter.BooleanVar()
#state2.set(True)
state3 = tkinter.BooleanVar()
radio = tkinter.Radiobutton(window, text='Male', value=1, var=state2)
radio2 = tkinter.Radiobutton(window, text='Female', value=2, var=state3)
#radio2.deselect()
#radio.deselect()
radio.pack()
radio2.pack()
window.geometry('500x300')
window.mainloop()