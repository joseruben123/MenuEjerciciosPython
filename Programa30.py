"""
    En este programa vamos a encapsular metodos o funciones de las clases para que solo puedan ser llamadas o usadas
    desde adentro de la clase.
    Para ello reutilizaremos el codigo del ejericio anterior....
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

curso1 = Curso("Matematicas", 5, "Ingenieria Software") # Definimos nuestro primer objeto
print(curso1.nombre) #Imprimimos el atributo nombre del primer objeto
curso1.__imparticion = "Virtual" #Aqui se demuestra que no se puede acceder desde afuera a atributos encapsulados
curso1.MostrarDatos()

