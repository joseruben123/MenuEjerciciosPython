"""
    Principio de sustitucion entre clases
    usamos parte del codigo del programa anterior
"""

class Persona(): #Creamos un clase llamada Persona

    def __init__(self, apePat, apeMat, names):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = names

    def mostrarNombreCompleto (self):
        textoMostrar = "{0} {1} {2}"
        return textoMostrar.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def Datos(self):
        print(self.mostrarNombreCompleto())

class Estudiante (Persona): #Creacion de una nueva clase estudiante con herencia de la clase Personas

    def __init__(self, apePat, apeMat, names, prof):
        super().__init__(apePat, apeMat, names) #En esta linea llamamos al constructor de la clase Personas
        self.profesion = prof

    def Datos(self): # Creacion de metodo con sobreescritura del metodo de la clase anterior
        super().Datos()  #Llamamos al metodo Datos de la clase padre
        print("Profesion: {0}".format(self.profesion))  #Imprimimos el dato de la profesion


estud1 = Estudiante("Torres", "Lopez", "Juan", "Ing. Software") #Creacion del primer objeto tomando como instancias 4 argumentos.

print(isinstance(estud1, Estudiante)) #Con este metodo podemos demostrar o comprobar si el objeto creado es parte de una instancia o no




