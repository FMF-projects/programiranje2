from tkinter import *
from math import *
from datetime import *

class Ura():

    def __init__(self, master):
    
        self.zacetni_cas = datetime.now()

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
        self.min = self.platno.create_line(150, 150, 150, 40, width=3)
        self.ura = self.platno.create_line(150, 150, 150, 80, width=5)
        
        self.kot = 0
        
        self.premakni()
        
    def premakni(self):
        '''premakne kazalec na nov položaj'''
        self.kot += 6
        x = 150 + 140 * cos(radians(self.kot))
        y = 150 + 140 * sin(radians(self.kot))
        #sekunde = self.zacetni_cas.second()
        #trenutni = datetime.now()
        #if trenutni.second() - sekunde == 1:
        self.platno.coords(self.sek, 150, 150, x, y)
        
        self.platno.after(1000, self.premakni)        


root = Tk()
aplikacija = Ura(root)
root.mainloop()
