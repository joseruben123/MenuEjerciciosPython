"""
Uso dela función raise ; Que nos sirve para crear nuestras propias excepciones
"""

def evaluarNota(nota):

    if nota < 0:
        raise ZeroDivisionError ("No se pueden colocar números negativos") #Aqui definimos nuestra propia excepcion...
    elif nota >= 16:
        print("Exelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado.....")



evaluarNota(-4)

print("este es el fin del programa.............")
