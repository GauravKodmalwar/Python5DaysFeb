import tkinter

window = tkinter.Tk()
menubar = tkinter.Menu(window)
# Add menu
file = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='File', command=None) # not linked with any function
file.add_command(label='File Open', command=None)
file.add_command(label='File Save', command=None)
file.add_separator() # Adding a seperator or horizontal line
file.add_command(label='Exit', command=window.destroy) # default function
window.geometry('500x300')
window.config(menu=menubar) # Additional step for linking menu
window.mainloop()