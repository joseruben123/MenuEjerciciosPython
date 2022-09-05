"""
	En esta función vamos a crear un menu de opciones para todos los programas que se an creado.
"""

print("""

	opcion ( 1 )  , para imprimir mi primer HOLA MUNDO
	opcion ( 2 )  , para iniciar el programa de uso de variables
	opcion ( 3 )  , para iniciar el programa de conversiones
	opcion ( 4 )  , para iniciar el programa de numeros, operaciones matematicas y conversiones
	opcion ( 5 )  , para iniciar el programa de concatenacion
	opcion ( 6 )  , para iniciar el programa de funciones de cadenas
	opcion ( 7 )  , para iniciar el programa de tuplas
	opcion ( 8 )  , para iniciar el programa de Listas
	opcion ( 9 )  , para iniciar el programa de Diccionarios
	opcion ( 10 ) , para iniciar el programa de Lectura de datos por teclado
	opcion ( 11 ) , para iniciar el programa de Estructuras condicionales IF - ELIF - ELSE
	opcion ( 12 ) , para iniciar el programa de funciones
	opcion ( 13 ) , para iniciar el programa de Operadores Logicos (AND,OR,NOT)
	opcion ( 14 ) , para iniciar el programa de Operador ternario
	opcion ( 15 ) , para iniciar el programa de funcion Range 
	opcion ( 16 ) , para iniciar el programa de Bucle for 
	opcion ( 17 ) , para iniciar el programa de IF con tuplas y Listas
	opcion ( 18 ) , para iniciar el programa de Factorial de un numero
	opcion ( 19 ) , para iniciar el programa de Bucle While
	opcion ( 20 ) , para iniciar el programa de Sentencias Break, continue y pass
	opcion ( 21 ) , para iniciar el programa de Generadores yield
	opcion ( 22 ) , para iniciar el programa de Generadores yield from 
	opcion ( 23 ) , para iniciar el programa de Excepciones bloques( TRY, EXCEPT , FINALLY)
	opcion ( 24 ) , para iniciar el programa de Sentencia RAISE
	opcion ( 25 ) , para iniiar el programa sobre Modulos e importacion de archivos
	opcion ( 26 ) , para iniciar el programa sobre paquetes de archivo __init__.py
	opcion ( 27 ) , para iniciar el programa sobre programación orientada a objetos (POO) 
	opcion ( 28 ) , para iniciar el programa sobre contruccion de clases
	opcion ( 29 ) , para iniciar el programa sobre encapsulamiento de variables
	opcion ( 30 ) , para iniciar el programa sobre encapsulamiento de metodos
	opcion ( 31 ) , para iniciar el programa sobre metodos accesores (GET ySET)
	opcion ( 32 ) , para iniciar el programa sobre metodo de clase __str__(self)
	opcion ( 33 ) , para iniciar el programa sobre Herencia con metodo super().
	opcion ( 34 ) , para iniciar el programa sobre sobre escritura de metodos
	opcion ( 35 ) , para iniciar el programa sobre principio de sustitucion entre clases
	opcion ( 36 ) , para iniciar el programa sobre herencia multiple
	opcion ( 37 ) , para iniciar el programa sobre polimorfismo
	opcion ( 38 ) , para iniciar el programa sobre relacion entre clases
	==================================
	opcion ( 0 )   SALIR 
	==================================

""")

valor = True

while valor:
	opcion = int(input("Ingrese la opción....... "))
	
	if opcion == 0:
		break

	while opcion not in range(1, 39):
		
		opcion = int(input("Ingrese la opción correcta: "))

	namePrograma = "Programa"+str(opcion)+".py"

	exec(open(namePrograma).read())




