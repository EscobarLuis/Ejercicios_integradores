def get_int():
    while True:
        try:
            dato = int(input("Ingrese un numero: "))
            return dato
        except ValueError:
            print ("ERROR: Tipo de dato incorrecto.")

def main():
    print(f'Usted ingreso el numero: {get_int()}') 
if __name__ == "__main__":
    main()
