from tkinter import *

class Semafor():

    def __init__(self, master):

        #dodamo gumbe (lambdo dodamo zato, da nam ni potrebno
                       #za vsak gumb pisati svoje funkcije)
        zelena = Button(master, text='zelena', command=lambda: self.pobarvaj('zelena'))
        zelena.grid(row=0, column=0)
        
        rumena = Button(master, text='rumena', command=lambda: self.pobarvaj('rumena'))
        rumena.grid(row=0, column=1)
        
        rdeca = Button(master, text='rdeča', command=lambda: self.pobarvaj('rdeča'))
        rdeca.grid(row=0, column=2)


        #dodamo platno
        self.platno = Canvas(master, width=100, height=100, background='red')
        self.platno.grid(row=1, column=1)


    def pobarvaj(self, barva):
        '''Spremeni barvo platna'''
        if barva == 'zelena':
            self.platno.config(background='green')
        elif barva == 'rumena':
            self.platno.config(background='yellow')
        elif barva == 'rdeča':
            self.platno.config(background='red')
    
root = Tk()
aplikacija = Semafor(root)
root.mainloop()
