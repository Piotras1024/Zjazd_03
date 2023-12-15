class Auto:
    def __init__(self, kolor, kondycja, wiek=0):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2024 - wiek

    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
        elif tryb == 'normal':
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
        else:
            print('brak zmian')

    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
        return zasieg


moje_auto = Auto('white', 3, 12)
auto_sasiada = Auto('black', 2, 5)

print(moje_auto.kolor)
moje_auto.kolor = 'black'
print(moje_auto.kolor)
print(auto_sasiada.kolor)
print(moje_auto.zasieg())
moje_auto.ustaw_tryb('eco')
print(moje_auto.zasieg())