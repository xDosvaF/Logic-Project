class Animal():
    def comer():
        print("Está comiendo")

class Mamifero(Animal):
    def amamantar():
        print("Está amamantando")

class Ave(Animal):
    def volar():
        print("Está volando")

class Murcielago(Mamifero, Ave):
    pass

Murcielago.volar()
Murcielago.comer()
Murcielago.amamantar()