class Persona():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def hablar(self):
        print(f"{self.nombre} empezó a hablar")

class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f"mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, sexo,habilidad, salario, empresa):
        Persona.__init__(self,nombre,edad,sexo)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f"{super().most}")


Esteban = EmpleadoArtista("Esteban",18, "Masculino","Desarrollador","Q5000", "Google")

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(Esteban, Persona)
print(herencia)
print(instancia)