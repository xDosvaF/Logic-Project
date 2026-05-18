nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
grado = input("Escribe tu grado académico: ")

class Usuario():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

Usuario1 = Usuario(nombre,edad,grado)

print(f"""
        DATOS DEL ESTUDIANTE \n
        NOMBRE: {Usuario1.nombre} 
        EDAD: {Usuario1.edad} 
        GRADO: {Usuario1.grado}
      """)

activo = True
while activo:
    opcion = input("")

    if opcion == "Estudiar":
        Usuario1.estudiar()
    
    else:
        print("No existe esa acción")
