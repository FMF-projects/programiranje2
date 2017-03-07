from tkinter import *

class Torta():

    def __init__(self, master):
        
        #dodamo vnosno polje
        self.vnos = Entry(master)
        self.vnos.grid(row=0, column=0)
        
        narisi_gumb = Button(master, text='Nariši', command=self.narisi)
        narisi_gumb.grid(row=0, column=1)
        
        #tortni diagram
        self.platno = Canvas(master, width=250, height=250)
        self.platno.grid(row=1, column=0)
        
    
    def narisi(self):
        '''nariše tortni diagram'''     
        barve = ['yellow','red','orange','blue','green','cyan',
                'black','gray', 'magenta']
        podatki = self.vnos.get()
        podatki = podatki.split()
        vsota = sum(list(map(int, podatki)))
        
        b = 0
        zacetek = 0
        for i in podatki:
            delez = (360 * int(i)) / vsota
            izsek = self.platno.create_arc(40, 40, 240, 240, 
                    start=zacetek, extent=delez, fill=barve[b])
            zacetek += delez
            
            if b != (len(barve) - 1):
                b += 1
            else:
                b = 0

root = Tk()
aplikacija = Torta(root)
root.mainloop()
        
