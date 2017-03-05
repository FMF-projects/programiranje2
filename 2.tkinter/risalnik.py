from tkinter import *

class Risalnik():

    def __init__(self, master):

        self.platno = Canvas(master, width=300, height=300)
        self.platno.grid(row=1, column=0)

        #nastavimo glavni menu
        glavni_menu = Menu(master)
        master.config(menu=glavni_menu)

        #nastavimo podmenije
        risalnik_menu = Menu(glavni_menu, tearoff=0)
        glavni_menu.add_cascade(label="Risalnik", menu=risalnik_menu)

        barva_menu = Menu(glavni_menu, tearoff=0)
        glavni_menu.add_cascade(label="Barva", menu=barva_menu)

        debelina_menu = Menu(glavni_menu, tearoff=0)
        glavni_menu.add_cascade(label="Debelina", menu=debelina_menu)

        #dodamo izbire v menuje
        risalnik_menu.add_command(label="Končaj", command=self.koncaj)
        risalnik_menu.add_command(label="Počisti", command=self.pocisti)

        self.barva = StringVar(value='black')
        self.debelina = IntVar(value=1)
                               
        #če želimo, da je poleg zadnje izbrane izbire kljukica
        barva_menu.add_radiobutton(label="črna", variable=self.barva, value='black')
        barva_menu.add_radiobutton(label="modra", variable=self.barva, value='blue')
        barva_menu.add_radiobutton(label="rdeča", variable=self.barva, value='red')
        barva_menu.add_radiobutton(label="zelena", variable=self.barva, value='green')
        
        debelina_menu.add_radiobutton(label="1", variable=self.debelina, value=1)
        debelina_menu.add_radiobutton(label="2", variable=self.debelina, value=2)
        debelina_menu.add_radiobutton(label="3", variable=self.debelina, value=3)
        debelina_menu.add_radiobutton(label="4", variable=self.debelina, value=4)

        #create_line(.... fill = self.barva.get(), width=self.debelina.get())

        self.platno.bind("<Button-1>", self.klik)
        self.platno.bind("<B1-Motion>", self.premik)


    def koncaj(self):
        '''zapre aplikacijo'''
        root.destroy()
    
    def pocisti(self):
        '''pocisti platno'''
        self.platno.delete('all')
    
    def klik(self, event):
        self.tocka = (event.x, event.y)

    def premik(self, event):
        if self.tocka is not None:
            (x, y) = self.tocka
            self.platno.create_line(x, y, event.x, event.y, 
                                fill=self.barva.get(), width=self.debelina.get())
            self.tocka = (event.x, event.y)
            

root = Tk()
aplikacija = Risalnik(root)
root.mainloop()
