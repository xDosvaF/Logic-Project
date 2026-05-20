class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Woouf"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(perro)

x: int = 10
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

print(saludar(x))