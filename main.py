import sys
import os
# Agregar la ruta de la carpeta "ejercicios" al sys.path
ejercicios_dir = os.path.join(os.path.dirname(__file__), "Ejercicios")
sys.path.append(ejercicios_dir)
# Importar las funciones desde los archivos correspondientes
from punto1 import funcion1
from punto2 import funcion2
from punto3 import funcion3
from punto4 import funcion4

def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Ejecutar función 1")
    print("2. Ejecutar función 2")
    print("3. Ejecutar función 3")
    print("4. Ejecutar función 4")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada (1/2/3/4/5): ")

        if opcion == '1':
            funcion1()  
        elif opcion == '2':
            salida = funcion2()
            print("Salida:", salida) 
            input("Presione Enter para regresar al menú...") 
        elif opcion == '3': 
            salida3 = funcion3()
            print("Salida:", salida3)
            input("Presione Enter para regresar al menú...") 
        elif opcion == '4':
            funcion4()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()