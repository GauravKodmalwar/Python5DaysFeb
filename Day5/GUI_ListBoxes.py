import tkinter
# list boxes for multiple option

def randomFunction():
    pass
window = tkinter.Tk()
list1 = tkinter.Listbox(window, selectmode=tkinter.MULTIPLE, height=10, width=15, bg='grey')
list1.insert(1, 'Basic Training')
list1.insert(2, 'Data structure')
list1.insert(3, 'Functions')
list1.insert(4, 'Classes')
list1.insert(5, 'GUI')
list1.grid(column=0, row=1)
button = tkinter.Button(window, text='greet', fg='green', bg='grey', command=randomFunction)
button.grid(column=1, row=1)
window.geometry('500x300')
window.mainloop()