"""
En este programa vamos a ver la relacion entre clases
"""
class Pais(): #Creacion de Clase Pais

    def __init__(self, nom, pre):  # Iniciamos el metodo constructor para esta clase
        self.nombre = nom
        self.presidente = pre

    def __str__(self): #Este metodo lo colocamos para que al momento de imprimir el objeto se imprima ko que esta dentro de este metodo.
        texto = "PAIS  :  {0}   - PRESIDENTE :  {1}"
        return texto.format(self.nombre, self.presidente)



class Ciudad(): #Creacion de Clase ciudad

    def __init__(self, nom, hab, pai):  # Iniciamos el metodo constructor para esta clase
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self):  #Este metodo lo colocamos para que al momento de imprimir el objeto se imprima ko que esta dentro de este metodo.
        texto = "Ciudad :  {0}   - #Habitantes :  {1}"
        return texto.format(self.nombre, self.habitantes)


class Urbanizacion (): #Creacion de Clase Urbanizacion

    def __init__(self, nom, ciud): # Iniciamos el metodo constructor para esta clase
        self.nombre = nom
        self.ciudad = ciud

    def __str__(self):  #Este metodo lo colocamos para que al momento de imprimir el objeto se imprima ko que esta dentro de este metodo.
        texto = "Urbanizacion : {0}  "
        return texto.format(self.nombre, self.ciudad)

pais1 = Pais("Ecuador", "Guillermo Lazzo")
print(pais1)

ciudad1 = Ciudad("Quito", 580000, pais1)
print(ciudad1)

urba1 = Urbanizacion("Ceibos", ciudad1)
print(urba1)
