class Perro:
    def __init__(self, nombre1,raza1):
        self.nombre=nombre1
        self.raza=raza1
    
    def ladrar(self):
        return f"¡{self.nombre} dice Guau!"
    
mi_perro=Perro("Toby","Pitbull")
gato=Perro("Luna","Siames")



print(mi_perro.nombre)
print(gato.ladrar())