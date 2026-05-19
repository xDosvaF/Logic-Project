class Persona():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def hablar(self):
        print(f"{self.nombre} empezó a hablar")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, notas, universidad):
        super().__init__(nombre, edad, sexo)
        self.notas = notas
        self.universidad = universidad

class Empleado(Persona):
    def __init__(self, nombre, edad, sexo,trabajo,salario):
        super().__init__(nombre, edad, sexo)
        self.trabajo = trabajo
        self.salario = salario


Esteban = Empleado("Esteban",18, "Masculino","Desarrollador","Q5000")

Esteban.hablar()
print(Esteban.salario)