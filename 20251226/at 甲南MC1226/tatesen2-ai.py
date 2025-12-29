from tkinter import *

root = Tk()
w = Canvas(root, width=900, height=400)
w.pack()

for i in range(100):
    x = i * 9
    c = "#FF0000" if i % 2 == 0 else "#0000FF"
    w.create_line(x, 0, x, 400, fill=c)

root.mainloop()
