"""
	En este programa se va a usar las excepciones de python
	las excepciones son errores en tiempo de ejecucion (durante la ejecucion de un programa)
	entre estas funciones tenemos Except, try, finally
"""

numero1 = 10
numero2= 2

	#A continuacion vamos a intentar dividir el numero1 para el numero2

try:
	print( numero1/numero2 ) 	#Esto nos devuelve un error: division by zero
except ZeroDivisionError:
	print("no se puede dividir entre 0") 	#Esta linea de codigo imprimira si el intento de correr la linea de codigo anterior no se puede correr

finally: 		#Esta funcion nos sirve para ejecutar un codigo siempre asi se pueda o no ejecutar el codigo dentro del try.
	print("yo siempre aparezco....")

print("Aqui termina este programa.....")