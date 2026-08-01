class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Método público de inserción
    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    # Método privado recursivo
    def _insertar(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izquierda = self._insertar(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._insertar(nodo.derecha, dato)
        return nodo

    # 1. Recorrido Preorden: Raíz -> Izquierda -> Derecha
    def preorden(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    # 2. Recorrido Enorden: Izquierda -> Raíz -> Derecha (Los muestra ordenados)
    def enorden(self, nodo):
        if nodo:
            self.enorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.enorden(nodo.derecha)

    # 3. Recorrido Postorden: Izquierda -> Derecha -> Raíz
    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.dato, end=" ")


# Programa principal
arbol = ArbolBinario()

while True:
    print("\n--- MENÚ ÁRBOL BINARIO ---")
    print("1. Insertar Nodo")
    print("2. Recorrido en Preorden")
    print("3. Recorrido en Enorden")
    print("4. Recorrido en Postorden")
    print("5. Salir")
    
    opcion = input("Dame tu opción: ")

    if opcion == "1":
        num = int(input("Dame un número: "))
        arbol.insertar(num)
        print(f"-> Nodo {num} insertado correctamente.")

    elif opcion == "2":
        print("\nRecorrido Preorden:")
        if arbol.raiz is None:
            print("El árbol está vacío.")
        else:
            arbol.preorden(arbol.raiz)
            print() # Salto de línea al terminar

    elif opcion == "3":
        print("\nRecorrido Enorden:")
        if arbol.raiz is None:
            print("El árbol está vacío.")
        else:
            arbol.enorden(arbol.raiz)
            print() # Salto de línea al terminar

    elif opcion == "4":
        print("\nRecorrido Postorden:")
        if arbol.raiz is None:
            print("El árbol está vacío.")
        else:
            arbol.postorden(arbol.raiz)
            print() # Salto de línea al terminar

    elif opcion == "5":
        print("Programa terminado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")