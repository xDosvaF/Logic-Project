
# Atributo Privado
class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"
    
    def _hablar():
        print("Hola estoy protegido")

# Atributo MUY Privado
class MiClase2:
    def __init__(self):
        self.__atributo_privado = "Valor"
    
    def __hablar():
        print("Hola soy muy privado jsjsjs")

objeto = MiClase()
objeto2 = MiClase2()

print(objeto._atributo_privado)
print(objeto2.__atributo_privado)
