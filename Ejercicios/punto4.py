# Diccionario para almacenar el inventario
inventario = {
    'dairy': {},
    'cleaning': {},
    'grain': {}
}

def registrar_producto():
        grupo = input("Ingrese el grupo al que pertenece el producto (dairy/cleaning/grain): ").lower()
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if producto in inventario[grupo]:
            inventario[grupo][producto] += cantidad
        else:
            inventario[grupo][producto] = cantidad

def mostrar_inventario():
        print(f"{'Nombre':<20}{'Existencias':<15}")
        print("-" * 35)
        for grupo, productos in inventario.items():
            for producto, cantidad in productos.items():
                print(f"{producto:<20}{cantidad:<15}")
        input("Presione Enter para regresar al menú...") 

def funcion4():
    while True:
        print("---- Sitema de inventario. Ingrese una opcion: ----")
        print("1. Agregar Producto")
        print("2. Ver reporte inventario")
        print("3. Salir")
        
        opcion = input("Ingrese la opción deseada (1/2/3): ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    funcion4()