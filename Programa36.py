"""
En este programa vamos a usar herencias multiples
"""
class ClaseA(): # Definimos la primer clase (ClaseA)

    def __int__(self, par1, par2): # Iniciamos el metodo constructor para la primera clase
        self.parametro1 = par1
        self.parametro2 = par2

class ClaseB (): # Definimos la segunda clase (ClaseB)

    def __int__(self,par3, par4, par5): # Iniciamos el metodo constructor para la segunda clase
        self.parametro3 = par3
        self.parametro4 = par4
        self.parametro5 = par5

class ClaseX(ClaseB, ClaseA): #Definimos la tercera clase como (ClaseX) con herencia de la clase B y la Clase A
    pass

ClaseX1 = ClaseX() #Creamos un objeto de la clase ClassX

