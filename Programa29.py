"""
    En este programa vamos hacer uso de una funcion de las clases
    la cual es el encapsulamiento
    para continuar con este programa vamos a reutilizar el codigo del programa anterior y añadiremos nuevos atributos

"""
class Curso():

    def __init__(self, nom, cred, prof):    # Este es el estado inicial del objeto
        self.nombre = nom  # aqui asignamos nom al atributo nombre
        self.creditos = cred
        self.profesion = prof
        self.__imparticion = "Presencial"  #Esta propiedad esta encapsulada por tanto no se puede acceder desde afuera

    def MostrarDatos(self):
        dat = "nombre : {0} / Creditos: {1} / Modo de imparticion : {2} "
        print(dat.format(self.nombre, self.creditos, self.__imparticion))

curso1 = Curso("Matematicas", 5, "Ingenieria Software") # Definimos nuestro primer objeto
print(curso1.nombre) #Imprimimos el atributo nombre del primer objeto
curso1.__imparticion = "Virtual" #Aqui se demuestra que no se puede acceder desde afuera a atributos encapsulados
curso1.MostrarDatos()


