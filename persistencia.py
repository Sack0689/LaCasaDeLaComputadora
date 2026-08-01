import json

#datos={"usuario": "Ana", "nivel": 5, "punto": 1500}

def menu():
    print("------ M E N Ú  O P C I O N E S -------")
    print("1. Guardar información en el archivo")
    print("2. Leer información del archivo")
    print("3. Salir")

def guardar_informacion(datos):    
    try:
    #Guardar en disco 
        with open("progreso.json","a", encoding="utf-8") as archivo:
            json.dump(datos,archivo)
            print("Datos guardado correctamente....")
    except IOError:
        print("Error: No se puede escribir en el disco (permisos denegado o disco lleno)")
        #leer la información del archivo

def crear_datos(usuario,nivel,punto):
    datos= leer_informacion()
    datos={"usuario":usuario,
          "nivel": nivel,
          "punto": punto}
    guardar_informacion(datos)

def leer_informacion():
    try:
        with open("progreso.json","r") as archivo:
            datos_cargados= json.load(archivo)
            print("Archivo cargado con éxito")
            return archivo
    except FileNotFoundError:
        print("El archivo progreso.json no existe...")

    except json.JSONDecodeError:
        print("El archivo existe pero no se puede leer o esta dañado")

    except Exception as e:
        print(f"Ocurrio un error inesperado {e}")        

if __name__=="__main__":
    menu()
    opcion=int(input("Dame una opcion: "))
    if opcion == 1:
        leer_informacion()
    elif opcion == 2:
         nombre=input("Dame el usuario a guardar: ")
         nivel=int(input("Dame el nivel del jugador: "))
         puntaje=float(input("Dame el puntaje del jugador: "))
         crear_datos(nombre, nivel, puntaje)

    elif opcion == 3:
         print("Opción Salir......")

    else: 
        print("Opcion no valida....")
        

