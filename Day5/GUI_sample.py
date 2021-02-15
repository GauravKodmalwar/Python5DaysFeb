# GUI - Graphical User Interface (Front End)
import tkinter

window = tkinter.Tk()
window.geometry('800x500')

# widgets ==> different elements like Label, Button, Radio, Frame
for i in range(10):
    label = tkinter.Label(window, text="Hello,")
    label.grid(column=0, row=i)
    #label.pack(side=tkinter.TOP) # pack is loading that label into window
#help(label.pack)
#label.grid(column=1, row=0) # loading widgets at table or grid structure

#label2 = tkinter.Label(window, text=" Pythoner")
#label2.pack(side=tkinter.BOTTOM) # pack is loading that label into window
#label2.grid(column=10, row=5)
#label2.grid()

window.mainloop()