from tkinter import *
from math import *
from datetime import *

class Ura():

    def __init__(self, master):

        self.platno = Canvas(master, width=300, height=300)
        self.platno.grid(row=0, column=0)

        self.platno.create_oval(10, 10, 290, 290)

        #vstavimo številke
        kot = 0
        stevila = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
        for i in stevila:
            x = 130 * cos(radians(kot))
            y = 130 * sin(radians(kot))
            self.platno.create_text(150 + x, 150 + y, text=str(i))
            kot += 30

        #vstavimo kazalce
        self.sek = self.platno.create_line(150, 150, 150, 10)
        self.min = self.platno.create_line(150, 150, 150, 10, width=3)
        self.ura = self.platno.create_line(150, 150, 150, 10, width=5)
        
        def premakni(self):
            '''premakne kazalec na nov položaj'''
            #trenutne koordinate
            x, y, z, w = self.platno.coords(self.sek)
            kot = radians(6)
            self.platno.coords(self.sek, 150, 150, z + cos(kot), w + sin(kot))


root = Tk()
aplikacija = Ura(root)
root.mainloop()
