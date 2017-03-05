############################################################
# CATALANOVA ŠTEVILA
############################################################
def catalan(n):
    '''vrne število načinov, na katere lahko gnezdimo n parov oklepajev'''

    if n == 0:
        return
    c = [1]
    yield 1

    for i in range(1,n):
        vsota = 0
        for j in range(i):
            vsota += c[j] * c[i - j - 1]
        c.append(vsota)
        yield vsota


#catalan brez parametra:
def catalan2(n=None): #privzeta vrednost
    '''vrne število načinov, na katere lahko gnezdimo n parov oklepajev'''

    if n == 0:
        return
    c = [1]
    yield 1

    i = 1
    while True:
        if n is not None and i >= n:
            break
        else:
            vsota = 0
            for j in range(i):
                vsota += c[j] * c[i - j - 1]
            c.append(vsota)
            i += 1
            yield vsota


############################################################
# MERITVE TEŽE
############################################################
class Oseba():

    def __init__(self, ime):
        self.ime = ime
        self.meritve = []

    def __repr__(self):
        return '({0}:{1})'.format(self.ime, self.meritve)
        
    def dodaj_meritev(self, dan, teza):
        '''Doda meritev k izbrani osebi.'''
        self.meritve.append((dan, teza))

    def teza_na_dan(self, dan):
        '''Vrne težo osebe na določen dan.'''
        meritve = self.meritve
        if meritve == []:
            return None
        pred_dan = []
        po_dan = []
        for (i,j) in meritve:
            if i == dan:
                return j
            else: #razdelimo meritve na tiste pred in po danem dnevu
                if i < dan:
                    pred_dan.append((i,j))
                else:
                    po_dan.append((i,j))
        if pred_dan == []:
            return po_dan[0][1]
        elif po_dan == []:
            return pred_dan[-1][1]
        else:
            return (pred_dan[-1][1] + po_dan[0][1]) / 2

#janez = Oseba('Janez')
#janez.dodaj_meritev(2,87)
#janez.dodaj_meritev(4,88)
#janez.dodaj_meritev(5,89)
#print (janez.teza_na_dan(1))

def preberi_podatke(ime_datoteke):
    '''Prebere vsebino datoteke in vrne seznam Oseb.'''
    f = open(ime_datoteke, "r")
    meritve = []
    for vrstica in f:
        if vrstica[0] != '*':
            meritve.append(Oseba(vrstica))
        else:
            podatki = vrstica.split()
            meritve[-1].dodaj_meritev(int(podatki[1]), float(podatki[2]))
    f.close() #datoteko moramo po uporabi vedno zapreti 
    return meritve

#print (preberi_podatke("tehtanje.txt"))

def najtezji_prostovoljec(ime_datoteke, dan):
    '''Vrne najtežjega prostovoljca na določen dan.'''
    podatki = preberi_podatke(ime_datoteke)
    najtezji = None
    naj_teza = 0
    for oseba in podatki:
        podatki_oseba = oseba.meritve
        if podatki_oseba == []:
            continue
        teza = 0
        for (d, t) in podatki_oseba:
            if d == dan and t > teza:
                teza = t
        if teza > naj_teza:
            naj_teza = teza
            najtezji = oseba
    if najtezji == None:
        return None
    else:
        return najtezji.ime
        
#print(najtezji_prostovoljec("tehtanje.txt", 2))


############################################################
# REDKI POLINOMI
############################################################
class Polinom():

    def __init__(self, koeficienti=None):
        if koeficienti == None:
            self.koef = {}
        elif type(koeficienti) == dict:
            self.koef = koeficienti
        else:
            k = {}
            for stop, koef in koeficienti:
                k[stop] = koef
            self.koef = k

    def __repr__(self):
        return str(self.koef)

    def vrednost(self, x):
        '''Izracuna vrednost polinoma v dani tocki'''
        y = 0
        for clen in self.koef:
            y += (x ** clen) * self.koef[clen]
        return y
        
#p = Polinom({341: 1, 82: -2, 0: 35})
#print(p.vrednost(1))
        
    def __add__(p, q):
        '''Sešteje dva redka polinoma'''
        #bolje bi bilo, če bi najprej dodala vse iz p in potem seštevala
        vsota = {}
        for i in p.koef:
            if i in q.koef:
                vsota[i] = p.koef[i] + q.koef[i]
            else:
                vsota[i] = p.koef[i]
                
        for j in q.koef:
            if j in vsota:
                continue
            else:
                vsota[j] = q.koef[j]
        
        rezultat = {}
        for clen in vsota:
            if vsota[clen] != 0:
                rezultat[clen] = vsota[clen]
        return rezultat
    
#print(Polinom({1: 1, 0: 2}) + Polinom({1: -1, 0: -2}))


############################################################
# ŠKRIPCI
############################################################
class Utez():
    def __init__(self, masa):
        self.masa = masa

    def __repr__(self):
        'Utez({0})'.format(self.masa)
        
class Skripec():
    def __init__(self, l, d):
        self.levo = l
        self.desno = d
        
    def __repr__(self):
        'Skripec({0},{1})'.format(self.levo, self.desno)

#print(Skripec(Skripec(Utez(2),Utez(4)),Skripec(Utez(3),Skripec(Utez(2), Utez(1)))))