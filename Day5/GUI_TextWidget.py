import tkinter

window = tkinter.Tk()
window.title("Hello")
text = tkinter.Text(window, height=5, width=40)
text.insert(tkinter.END, 'Hello, all. Congratuations, completing training')
text.pack()
#text.tag_add("hello", "1.0")
#text.tag_config('Hello', background='yellow')
window.geometry('500x300')
window.mainloop()