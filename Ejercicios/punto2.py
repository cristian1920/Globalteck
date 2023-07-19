def funcion2():
    entrada_usuario = input("Ingrese una lista de números separados por comas: ")
    lista_entrada = [int(num) for num in entrada_usuario.split(",")]

    lista_salida = []

    for num in lista_entrada:
        if num > 1000:
            break
        if num % 5 == 0 and num <= 600:
            lista_salida.append(num)

    return lista_salida

