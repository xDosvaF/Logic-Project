class A:
    def hablar(self):
        print("Hola desde A")

class B:
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    pass 

d = D()

print(D.mro())