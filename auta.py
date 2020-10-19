class Osobak():
    def __init__(self,znacka, spotreba, nadrz):
        self.znaka = znacka
        self.spotreba = spotreba
        self.nadrz = nadrz
        self.najeto = 0
        self.vnadrzi = 0

    def natankuj(self, mnozstvi):
        vysledek = self.vnadrzi + mnozstvi
        if vysledek <= self.nadrz:
            self.vnadrzi = vysledek
            return vysledek
        else:
            return None

    def jed(self, vzdalenost):
        vnadrzi = self.vnadrzi - self.spotreba/100 * vzdalenost
        if vnadrzi > 0:
            self.vnadrzi = vnadrzi
            self.najeto += vzdalenost
            return vnadrzi
        else:
            return None


class Nakladak(Osobak):
    def __init__(self,znacka, spotreba, nadrz, nosnost):
        self.znaka = znacka
        self.spotreba = spotreba
        self.nadrz = nadrz
        self.nosnost = nosnost
        self.najeto = 0
        self.vnadrzi = 0
    


cerveny = Osobak('ABC-123', 8, 42)
modry = Nakladak('XYZ-547', 6.7, 35, 1800)

cerveny.natankuj(30)
modry.natankuj(20)

print(cerveny.vnadrzi)
cerveny.jed(100)
print(cerveny.vnadrzi)
print(cerveny.najeto)

print(modry.vnadrzi)
modry.jed(250)
print(modry.vnadrzi)
print(modry.najeto)