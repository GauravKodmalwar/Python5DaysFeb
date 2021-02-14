import tkinter

window = tkinter.Tk()

T = tkinter.Text(window, height = 5, width = 52)
T.insert(tkinter.END, 'Hello, all. welcome')
T.pack()
window.geometry('500x200')
window.mainloop()