class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def presentacion(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def presentacion(self):
        print(f"Estoy cursando {self.grado}")

Esteban = Estudiante("Esteban Godoy",18, "1er año de Ingeniería en Sistemas")

Persona.presentacion(Esteban)
Esteban.presentacion()