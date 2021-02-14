import tkinter

def clicked():
    win = tkinter.Toplevel()
    win.wm_title("Warning")
    b = tkinter.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)
    b = tkinter.Button(win, text="Cancel", command=win.destroy)
    b.grid(row=1, column=1)

window = tkinter.Tk()
window.geometry('900x500')

label = tkinter.Label(window, text='Enter a number', font=('Ariel Bold', 10))
label.grid(column=0, row=0, columnspan=1)
label2 = tkinter.Label(window, text='Enter a number', font=('Ariel Bold', 10))
label2.grid(column=0, row=1, columnspan=1)
button = tkinter.Button(window, text='1st Number', fg='green', bg='grey', command=clicked)
button2 = tkinter.Button(window, text='2nd Number', fg='green', bg='grey', command=clicked)
button.grid(column=1,row=0)
button2.grid(column=1,row=1)
# If you are using grid, dont use pack on same object
#label.pack()
#label2.pack()
window.mainloop()