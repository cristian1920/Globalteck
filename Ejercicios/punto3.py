def funcion3():
    entrada_usuario = input("Ingrese una lista de números separados por comas: ")
    lista_entrada = [int(num) for num in entrada_usuario.split(",")]

    diccionario = {}

    for num in lista_entrada:
        if num in diccionario:
            diccionario[num].append(num)
        else:
            diccionario[num] = [num]

    lista_salida = list(diccionario.values())

    return lista_salida