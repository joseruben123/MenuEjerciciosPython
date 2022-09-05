"""
    En este programa vamos a usar el método de clase __str__ (conversion a string)
    Para proceder a crear el programa vamos a usar un código de un programa antes visto
"""

class Curso():

    def __init__(self, nom, cred, prof):    # Este es el estado inicial del objeto
        self.nombre = nom  # aqui asignamos nom al atributo nombre
        self.creditos = cred
        self.profesion = prof
        self.__imparticion = "Presencial"  #Esta propiedad esta encapsulada por tanto no se puede acceder desde afuera

    def MostrarDatos(self):
        dat = "nombre : {0} / Creditos: {1} / Modo de imparticion : {2} "
        docenteAsignado = self.__VerificarDocentes()
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        if docenteAsignado:
            print("Existe docente asignado...")
        else:
            print("no es necesario asignar un docente...")

    def __VerificarDocentes(self):
        print("Verificando si existe docente asignado")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False
    def __str__(self): #Esta funcion nos permite mostrar lo que se va imprimir al imprimir el objeto como tal
        texto = "nombre: {0} - creditos : {1} "
        return texto.format(self.nombre, self.creditos)




curso1 = Curso("Matematicas", 5, "Ingenieria Software") # Definimos nuestro primer objeto
print(curso1) #Esta linea me estaria imprimiendo la info que se tiene dentro del metodo __str__
