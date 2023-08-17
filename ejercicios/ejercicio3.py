def calcular_frecuencia(cadena):
    """La funcion recive una cadena y cuenta la cantidad de veces
        que aparece cada palabra. La funcion retorna un diccionario con el 
        conteo final donde la clave es la palabra y el valor las apariciones."""
    conteo = {}
    
    for palabra in cadena.split():
        if palabra not in conteo.keys():
            conteo[palabra] = 1
        else:
            conteo[palabra] = conteo[palabra] + 1
    
    return conteo


def main():
    dato = input("Ingrese la cadena a analizar: ")
    resultado = calcular_frecuencia(dato)

    print (f"Conteo final: {resultado}")

if __name__ == "__main__":
    main()