import tkinter

window = tkinter.Tk()

state = tkinter.BooleanVar() # Not python but tkinter boolean variable
state.set(True)
chk = tkinter.Checkbutton(text='select', var=state)
chk.pack()
window.geometry('300x200')
window.mainloop()