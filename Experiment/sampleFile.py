import tkinter

window = tkinter.Tk()
window.title("Hello GUI")
label = tkinter.Label(window, text='Enter a number')
label.pack()
# pack is used to add widgets to occupy all the width
# grid is used for table like structure with row, column
# place is used to add widgets with position

# widgets - an elements in the GUI like Label, Button, Entry, Text, Check, Radio, List, Menues
# Label

window.mainloop()