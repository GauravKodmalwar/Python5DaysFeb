import tkinter

window = tkinter.Tk()
# Creating Menubar
menubar = tkinter.Menu(window)

# Adding File Menu and commands
file = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=window.destroy)

window.config(menu=menubar)
window.mainloop()