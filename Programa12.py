"""
	En este programa se va a trabajar con funciones
	las funciones son instrucciones que realizan un proceso
	Su principal funcion es quenos ayudan a evitar repetir codigo
"""

def Saludar(): #Definir una funcion para que imprima el nombre apellido y el numero del programa
	print("Jonas")
	print("Ramirez")
	print("Programa 12")
	return "hola"

print(Saludar()) #Imprimimos la funcion saludar

def evaluarSueldoMinimo(sueldo): #Creacion de una funcion para evaluar el sueldo minimo con condicionales dentro de su codigo
	if sueldo >= 425:
		print("Cumples con el sueldo minimo")
	else:
		print("Ganas menos que el sueldo minimo")

evaluarSueldoMinimo(300) #Evaluar si sueldo de 300 cumple la condicion
evaluarSueldoMinimo(1200) #Evalur si 1200 cumple la condicion