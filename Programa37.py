"""
En este programa vamos hacer uso del polimorfismo el nombre se desprende de :
 poli (muchas) y morfos (formas)
"""

class Estudiante (): # Creamos la clase estudiante


    def Describir(self): #añadimos un metodo describir a la clase.
        print("Soy un buen estudiante........") #Esta es la impresion resultante al llamar al metodo describir

class Docente(): # Creamos la clase docente


    def Describir (self): #añadimos un metodo describir a la clase.
        print("Yo me dedico a enseñar cursos en youtube.....") #Esta es la impresion resultante al llamar al metodo describir

class Trabajador (): # Creamos la clase Trabajador

    def Describir (self): #añadimos un metodo describir a la clase.
        print("Trabajo dentro de una gran empresa...") #Esta es la impresion resultante al llamar al metodo describir

def DescribirPersona(persona): # Creamos un funcion externa a las clases con 1 argumento donde colocaremos el objeto creado.
    persona.Describir() #Esta es la impresion resultante al llamar al metodo describir


docent1 = Estudiante()  # Si en la creacion de este objeto cambiamos una clase u otro entonces la impresion sera diferente de la funcion

DescribirPersona(docent1)
