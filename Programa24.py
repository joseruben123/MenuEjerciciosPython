"""
	funcion del RAISE
	Esta funcion nos permite lanzar de forma intencional excepciones en python
	es decir nosotros mismo creamos la excepcion
"""

def evaluarNota(nota):

	if nota < 0:
		raise ZeroDivisionError ("No se permiten valores negativos") #El mensaje colocado aqui es personalizado, cuando se ejecuta esta excepcion entonces ya cae el programa.
	
	elif nota >= 9:
		print("Excelente")
	
	elif nota >=11 :
		print("Aprobado")

	else:
		print("Desaprobado...")

evaluarNota(5)
