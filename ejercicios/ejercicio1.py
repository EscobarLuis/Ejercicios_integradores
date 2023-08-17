def ingresar_numero():
    while True:
        try:
            dato = int(input("Ingrese un numero: "))
        except:
            print("ERROR. Vuelva a ingresar el dato.")
        else:
            return dato

def calcular_mcd(num1, num2):
    mcd = 0
    min = num1
    
    if num1 > num2:
        min = num2
    
    for i in range(1, min):
        if (num1 % i == 0) and (num2 % i == 0):
            mcd = i
    
    return mcd



def main():
    numero1 = ingresar_numero()
    numero2 = ingresar_numero()

    print (f"El mcd entre {numero1} y {numero2} es:  {calcular_mcd(numero1, numero2)}")


if __name__ == "__main__":
    main()