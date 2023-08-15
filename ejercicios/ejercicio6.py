class Persona():
    def __init__(self, nombre=None, edad=None, dni=None)->None:
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni

    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else:
            print("El nombre no es valido.")
        
    
    @edad.setter
    def edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un numero entero mayor que 0.")
        
    
    @dni.setter
    def dni(self, dni):
        if dni > 0:
            self._dni = dni
        else:
            print("El dni debe ser un numero entero mayor que 0.") 
        
    
    def mostrar(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}, dni: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
    
def main():
    
    #creamo una persona parametrizados
    persona2 = Persona("Juan", 20, 321546)
    #creamos una persona sin datos
    persona1 = Persona()

    persona1.mostrar() 
    persona2.mostrar()

    persona1.nombre="Antonia"
    persona1.edad=14
    persona1.dni=1234684

    persona1.mostrar()

if __name__ == "__main__":
    main()
