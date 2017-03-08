from tkinter import *
from math import *

class Krozenje():

    def __init__(self, master):

        self.platno = Canvas(master, width=600, height=600, background='black')
        self.platno.grid(row=0, column=0)

        #uvozimo slike
        self.sonce = PhotoImage(file="sonce.ppm")
        self.zemlja = PhotoImage(file="zemlja.ppm")
        self.luna = PhotoImage(file="luna.ppm")
        
        #postavimo slike na platno
        self.id_sonce = self.platno.create_image(300, 300, image=self.sonce)
        self.id_zemlja = self.platno.create_image(500, 300, image=self.zemlja)
        self.id_luna = self.platno.create_image(550, 300, image=self.luna)

        #definiramo kota
        self.kot_zemlja = 0
        self.kot_luna = 0

        self.premakni()


    def premakni(self):
        '''izračuna novo stanje elementov'''
        self.kot_zemlja += 0.1
        self.kot_luna += 0.8
            
        
        x_zemlja = 300 + 200 * cos(self.kot_zemlja)
        y_zemlja = 300 + 200 * sin(self.kot_zemlja)

        x_luna = 300 + 200 * cos(self.kot_zemlja) + 50 * cos(self.kot_luna)
        y_luna = 300 + 200 * sin(self.kot_zemlja) + 50 * sin(self.kot_luna)

        self.platno.coords(self.id_zemlja, x_zemlja, y_zemlja)
        self.platno.coords(self.id_luna, x_luna, y_luna)

        self.platno.after(50, self.premakni)



root = Tk()
aplikacija = Krozenje(root)
root.mainloop()
