def es_primo(numero):

    for i in range(2, numero):
        if numero % i == 0 and i != numero:
            return False
    return True


def calcular_primos(num):

    primos = []
    for i in range(2, num):
        if es_primo(i):
            primos.append(i)

    return primos


def calcular_factores_primos(numero):
    factores_primos = {}
    primos = calcular_primos(numero)
    for num in primos:
        while numero > 1:
            if (numero % num) != 0:
                break
            numero = numero / num
            if num not in factores_primos.keys():
                factores_primos[num] = 1
            else:
                factores_primos[num] = factores_primos[num] + 1

    return factores_primos


def factores(fac1, fac2):
    
    factores_final= []
    for key1 in fac1:
        if key1 not in fac2: 
            factores_final.append(key1 ** fac1[key1])
        else:
            if fac1[key1] >= fac2[key1]:
                factores_final.append(key1 ** fac1[key1])
            else:
                factores_final.append(key1 ** fac2[key1])
    
    for key2 in fac2:
        if key2 not in fac1: 
            factores_final.append(key1 ** fac2[key1])
    
    return factores_final

def calcular_mcm(num1, num2):
    
    factores_primos1 = calcular_factores_primos(num1)
    factores_primos2 = calcular_factores_primos(num2)

    factores_multiplicar = factores(factores_primos1, factores_primos2)

    resultado = 1
    
    for i in factores_multiplicar:
        resultado = resultado * i
    
    return resultado



def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
       
    print (f'El mcm entre {numero1} y {numero2} es: {calcular_mcm(numero1, numero2)}')


if __name__ == '__main__':
    main()
