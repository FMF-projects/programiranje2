from tkinter import *
from math import *
from datetime import *

class Ura():

    def __init__(self, master):

        self.platno = Canvas(master, width=300, height=300)
        self.platno.grid(row=0, column=0)

        self.platno.create_oval(10, 10, 290, 290)

        #vstavimo številke
        kot = -pi/3
        for i in range(1, 13):
            x = 130 * cos(kot)
            y = 130 * sin(kot)
            self.platno.create_text(150 + x, 150 + y, text=str(i))
            kot += pi/6

        #vstavimo kazalce
        self.sek = self.platno.create_line(150, 150, 150, 10)
        self.min = self.platno.create_line(150, 150, 150, 40, width=3)
        self.ura = self.platno.create_line(150, 150, 150, 80, width=5)
        
        self.kot = 0
        
        self.premakni()
        
    def premakni(self):
        '''premakne kazalec na nov položaj'''
        zdaj = datetime.now()
        ura = zdaj.hour
        minuta = zdaj.minute
        sekunda = zdaj.second
        
        x_s = 150 + 140 * cos((sekunda / 60) * 2 * pi - pi/2)
        y_s = 150 + 140 * sin((sekunda / 60) * 2 * pi - pi/2)
        
        x_m = 150 + 110 * cos((minuta/ 60) * 2 * pi - pi/2)
        y_m = 150 + 110 * sin((minuta/ 60) * 2 * pi - pi/2)
        
        x_u = 150 + 70 * cos((ura/ 12) * 2 * pi - pi/2)
        y_u = 150 + 70 * sin((ura/ 12) * 2 * pi - pi/2)
        
        self.platno.coords(self.sek, 150, 150, x_s, y_s)
        self.platno.coords(self.min, 150, 150, x_m, y_m)
        self.platno.coords(self.ura, 150, 150, x_u, y_u)
        
        self.platno.after(200, self.premakni)        

root = Tk()        
aplikacija = Ura(root)
root.mainloop()
