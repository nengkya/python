from Tkinter import *

top = Tk()

L1 = Label(top, text = "User Name") #top = master window top
L1.pack(side = TOP)

E1 = Entry(top, bd = 10) #bd = border line of entry field
E1.pack(side = TOP)

top.mainloop()
