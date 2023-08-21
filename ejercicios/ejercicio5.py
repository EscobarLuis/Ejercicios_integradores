def get_int():
    while True:
        try:
            dato = int(input("Ingrese un numero: "))
            return dato
        except ValueError:
            print("ERROR: Tipo de dato incorrecto.")


def get_int_recursiva():

    try:
        dato = int(input("Ingrese un numero: "))
        return dato
    except ValueError:
        print("ERROR: Tipo de dato incorrecto.")
        get_int_recursiva()


def main():
    
    print(f'Usted ingreso el numero: {get_int()}')

    print(f'Usted ingreso el numero: {get_int_recursiva()}')

if __name__ == "__main__":
    main()
