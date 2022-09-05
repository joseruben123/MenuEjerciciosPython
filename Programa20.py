"""
	Sentencias break, pass y continue : que nos permiten realizar diferentes funciones
	break: Permite salir de un bucle cuando se cumple una condicion
	pass: permite omitir codigo que aun no se termina o ya no es necesario
	continue: omite una parte del bucle cuando se cumple una condicion y continua con el resto
"""

	# ============EJERCICIO CON LA SENTENCIA BREAK========================

for numero in range (1 , 6):
	if numero == 4:
		break
	print("EL numero es : {} ".format(numero))

print("Bucle terminado............\n \n Ejercicio con sentencia Continue")


	# ============EJERCICIO CON LA SENTENCIA CONTINUE========================

for numero in range(1, 10):
	if numero ==5:
		continue
	print("El numero es : {0}".format(numero))

print("Bucle terminado........... \n\n")

# ============EJERCICIO CON LA SENTENCIA PASS========================

for numero in range(1, 10):
	if numero == 5:
		# Aqui no pasa nada y el bucle sigue trabajando 
		pass
	else:
		print("EL siguiente numero es mayor a 3...")

	print("El numero es : {0}".format(numero))

print("Bucle terminado...........")

def ContarNum():
	pass



