import Tkinter

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg = "yellow", height = 250, width = 300)

coord = 0, 0, 240, 210
C.create_arc(coord, start = 0, extent = 180, fill = "purple")

C.pack()
top.mainloop()
