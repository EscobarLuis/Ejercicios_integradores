from ejercicio7 import Cuenta
from ejercicio6 import Persona


class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
    
    def es_titular_valido(self):

        return super().persona.es_mayor_de_edad() and super().persona.edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: Titular no valido.")


    def mostrar(self):
        print(f"Cuenta Joven {self.bonificacion} ")
    

def main():
    
    titular = Persona("Juan", 23, 123456)    
    cuentaJo = CuentaJoven(titular, 100, 2)

    cuentaJo.mostrar()
    cuentaJo.retirar(50)
    cuentaJo.mostrar()


if __name__ == "__main__":
    main()