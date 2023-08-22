class Persona():
    def __init__(self, nombre=None, edad=None, dni=None)->None:
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    # Con el decorador @property declaro un getter
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    # Con el decorador @atributo.setter declaro un setter
    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self.__nombre = nombre
        else:
            print("El nombre no es valido.")
        
    
    @edad.setter
    def edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un numero entero mayor que 0.")
        
    
    @dni.setter
    def dni(self, dni):
        if dni > 0:
            self.__dni = dni
        else:
            print("El dni debe ser un numero entero mayor que 0.") 
        
    
    def mostrar(self):
        #al usar self.nombre estoy llamando al getter 
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

    print (f'{persona1.nombre} es mayor de edad') if persona1.es_mayor_de_edad() else  print (f'{persona1.nombre} NO es mayor de edad')

if __name__ == "__main__":
    main()
