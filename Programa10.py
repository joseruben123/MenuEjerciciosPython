"""
	En este programa vamos hacer uso del input.
	lo que nos permitira ingresar datos por teclado
"""

nombre = input("Ingrese su nombre :  ") # Lo que pedimos en esta linea es un nombre por tanto lo dejamos en tipo string 

edad = int(input("Ingrese su edad :  ")) #Convertimos la cadena que nos devuelve el input a int(entero)

sueldo = float(input("Ingrese su sueldo :  ")) #Convertimos la cadena que nos devuelve el input a float(decimal)

edadFutura = edad + 20 #Creamos una variable en la cual se aloja el valor entero que ingresamos por teclado mas 20 unidades.

	# Las lineas a continuacion son de impresion de la informacion

print("Hola ",nombre)

print("Tu edad es: ",edad)

print("Tu edad dentro de 20 años sera :  ", edadFutura)

print("Tu sueldo es :  ",sueldo)


