"""
    En este programa vamos a usaar el constructor __init__(self) de las clases
    el cual traera consigo unos atributos base ya inicializados desde un principio
"""
class Curso():

    def __init__(self, nom, cred, prof):    # Este es el estado inicial del objeto
        self.nombre = nom  # aqui asignamos nom al atributo nombre
        self.creditos = cred
        self.profesion = prof



curso1 = Curso("Matematicas", 5, "Ingenieria Software") # Definimos nuestro primer objeto
print(curso1.nombre) #Imprimimos el atributo nombre del primer objeto

curso2 = Curso("Fisica", 6, "Ingenieria Civil") # Definimos nuestro segundo objeto
print(curso2.nombre) #Imprimimos el atributo nombre del segundo objeto
