from ejercicio3 import calcular_frecuencia

def buscar_mas_repetida(diccionario):
    """La funcion recive un diccionario que contiene como key una palabra y 
       como valor la cantidad de apariciones. Retorna una tupla con la palabra 
       que mas se repite y la cantidad de repeticiones."""
    
    lista_max = [] 
    repeticiones = 0

    for clave, valor in diccionario.items():
        if valor > repeticiones:
            repeticiones = valor
            lista_max.clear()
            lista_max.append(clave)
            lista_max.append(valor)
        elif valor == repeticiones:
            lista_max.append(clave)
            lista_max.append(valor)
    
    return tuple(lista_max)

def main():
    dato = input("Ingrese una cadena de texto: ")
    
    frecuencia = calcular_frecuencia(dato)

    max_repetida = buscar_mas_repetida(frecuencia)

    print (type(max_repetida))
    print(f"La palabra mas repetida es: {max_repetida}")


if __name__ == "__main__":
    main()