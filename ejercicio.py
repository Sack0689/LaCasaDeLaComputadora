class Videojuego:
    def __init__(self, x, y, z, zz):
        self.titulo=x
        self.precio=y
        self.stock=z # 4
        self.genero=zz
    
    def mostrar_info(self):
        print(f"-----{self.titulo}----")
        print(f"Género: {self.genero}")
        print(f"Precio: {self.precio}")
        print(f"Stock disponible: {self.stock}")

    def vender(self, cantidad):
        #Reducir el stock solo si hay suficiente cantidad disponible
        if self.stock>=cantidad:
            self.stock=self.stock-cantidad
            print("Venta realizada...")
        else:
            print(f"No hay suficientes piezas se pueden vernder maximo: {self.stock}")
        

    def reabastecer(self, cantidad):
        self.stock=self.stock+cantidad
    
def menu():
    print("Menu")
    print("1. Venta")
    print("2. reabastecer")
    print("3. Muestra información")
   
#juego1=Videojuego("Residen Evil",500,25,"Terror")

#juego1.mostrar_info()
#juego1.vender(4)
#juego1.mostrar_info()


juego1=Videojuego("Residen Evil",500,12,"terror")
while True:
   
    menu()
    opcion=input("selecciona una opcion: ").strip()
    if opcion=='1':
        cant=int(input("que cantidad necesitas: "))
        juego1.vender(cant)
    elif opcion=='2':
         cant=int(input("cantidad a reabastecer: "))  
         juego1.reabastecer(cant)
    elif opcion=='3':
        juego1.mostrar_info()
    else:
        print("Opcion no valida....")