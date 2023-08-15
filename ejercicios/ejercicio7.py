from ejercicio6 import Persona 

class Cuenta():
    
    def __init__(self, titular, cantidad = 0):
        """""Contructor de Cuenta: recibe Persona y opcional la cantidad numero """
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        self._titular.mostrar()
    
    @property
    def cantidad(self):
        return self._cantidad

    @titular.setter
    def tutilar(self, nombre = None, edad = 0, dni = 0):
        self._titular.nombre = nombre
        self._titular.edad = edad
        self._titular.dni = dni
    
    def retirar(self, monto):
        if monto > 0: 
            self._cantidad -= monto
        else:
            print ("El monto a retirar debe ser positivo o cero.")
    
    def ingresar(self, monto):
        if monto > 0: 
            self._cantidad += monto
        else:
            print ("El monto a ingresar debe ser positivo o cero.")
    
    def mostrar(self):
        
        print(f"titular: nombre: {self._titular.nombre}, edad: {self._titular.edad},dni: {self._titular.dni}, cantidad: {self._cantidad}")


def main():
        
    persona1 = Persona("Jose", 20, 258465)
    cuenta1 = Cuenta(persona1, 500)
    
    cuenta1.mostrar()
    cuenta1.ingresar(100)
    cuenta1.mostrar()
    cuenta1.retirar(800)
    cuenta1.mostrar()

 




if __name__ == "__main__":
    main()


