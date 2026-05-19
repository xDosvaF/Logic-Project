class Persona():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def hablar(self):
        print(f"{self.nombre} empezó a hablar")

class Empleado(Persona):
    def __init__(self, trabajo, salario):
        self.trabajo = trabajo
        self.salario = salario

Esteban = Empleado("Esteban",18, "Masculino")
Esteban = Empleado("Desarrollador","Q5000")

Esteban.hablar()