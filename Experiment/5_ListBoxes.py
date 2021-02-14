import tkinter

window = tkinter.Tk()

list = tkinter.Listbox(window, height = 10, width = 15, bg = "grey",
                  activestyle = 'dotbox', font = "Helvetica", fg = "yellow")
list.insert(1, 'Basic Training')
list.insert(2, 'Data Structure')
list.insert(1, 'Functions')
list.insert(4, 'Input/Output and Classes')
list.insert(5, 'Regex and Tkinter')
list.pack()
window.geometry('500x300')
window.mainloop()