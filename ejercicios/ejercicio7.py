from ejercicio6 import Persona 

class Cuenta():
    
    def __init__(self, titular, cantidad = 0):
        """""Contructor de Cuenta: recibe Persona y opcional la cantidad numero """
        self._persona = titular
        self._cantidad = cantidad

    @property
    def persona(self):
        return self._persona
    
    @property
    def cantidad(self):
        return self._cantidad

    @persona.setter
    def persona(self, titular):
        self._persona = titular
    
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
        
        print(f"titular: nombre: {self.persona.nombre}, edad: {self.persona.edad},dni: {self.persona.dni}, cantidad: {self.cantidad}")


def main():
        
    persona1 = Persona("Jose", 20, 258465)
    cuenta1 = Cuenta(persona1, 500)
    persona2 = Persona("Maria", 20, 1235846)
    
    cuenta1.mostrar()
    cuenta1.ingresar(100)
    cuenta1.mostrar()
    cuenta1.persona = persona2
    cuenta1.retirar(800)
    cuenta1.mostrar()

 




if __name__ == "__main__":
    main()


