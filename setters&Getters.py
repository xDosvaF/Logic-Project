class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,new__nombre):
        self.__nombre = new__nombre

dalto = Persona("Lucas", 21)
nombre = dalto.get_nombre()

print(nombre)

dalto.set_nombre("Esteban")
nombre = dalto.get_nombre()

print(nombre)