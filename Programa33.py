"""
En este programa vamos a tratar ejemplos acerca de la herencia de las clases en python
"""

class Persona(): #Creamos un clase llamada Persona

    def __init__(self, apePat, apeMat, names):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = names

    def mostrarNombreCompleto (self):
        textoMostrar = "{0} {1} {2}"
        return textoMostrar.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Estudiante (Persona): #Creacion de una nueva clase estudiante con herencia de la clase Personas

    def __init__(self, apePat, apeMat, names, prof):
        super().__init__(apePat, apeMat, names) #En esta linea llamamos al constructor de la clase Personas
        self.profesion = prof


estud1 = Estudiante("Torres", "Lopez", "Juan", "Ing. Software") #Creacion del primer objeto tomando como instancias 4 argumentos.
print(estud1.mostrarNombreCompleto())
