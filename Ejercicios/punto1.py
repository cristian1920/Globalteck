def funcion1():
    numero = int(input("Ingrese el número: "))
    terminos = int(input("Ingrese el número de términos: "))
    
    resultado = 0
    numero_str = str(numero)

    for i in range(1, terminos + 1):
        repeticion = int(numero_str * i)
        resultado += repeticion

    print('El resultado de la operacion es: '+ str(resultado))
    input("Presione Enter para regresar al menú...")  # Esperar hasta que el usuario presione Enter
