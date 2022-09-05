"""
 La programacion orientada a objetos consiste en transladar la naturaleza de los
 objetos de la vida real a codigo de programacion (en algun lenguaje de programacion)

 Los objetos de la realidad tienen caracteristicas (atributos o propiedades) y
 funcionalidades o comportamientos (funciones o metodos)

 Ventajas:
 - Modularizacion (division en pequeñas partes ) de un programa completo
 - Codigo fuente muy reutilizado
 - Codigo fuente mas facil de incrementar en el futuro y mantener
 - Si existe un error en una pequeña parte del codigo el programa completo no debe fallar necesariamente, Ademas, es mas facil de corregir esos fallos.
 - Encapsulamiento Ocultamiento del funcionamiento interno de un  objeto.

"""

class Persona():
    #A continuacion las lineas de codigo daran atributos a este objeto
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # Aqui se colocaran las funcionalidades de este objeto persona

    def despertar(self):
        print("buen dia....")
        self.despierta = True


persona1 = Persona()

persona1.apellidos = "Aguilar Villavicencio"
print(persona1.apellidos)

persona1.despertar()
print(persona1.despierta)

print("\n\n")
# Creamos otro objeto como persona2
persona2 = Persona()

persona2.apellidos = "Gomez Fajardo"
print(persona2.apellidos)
print(persona2.despierta)