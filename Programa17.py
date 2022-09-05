"""
	uso de condicional IF con tuplas o listas
	validando los elementos de las tuplas o listas
"""

print("------ Cursos -------")

print("Matematicas -- Fisica -- Ciencias -- Sociales -- Quimica -- Biología -- Calculo ")

curso = input("Ingrese el curso al cual desea tener acceso, de los cursos detallados anteriormente......")

cursos = ["Matematicas", "Fisica", "Ciencias", "Sociales", "Quimica", "Biología", "Calculo"] # Creacion de lista con los nombres de los cursos

if curso in cursos: #Validacion con un if ; Si el curso ingresado por teclado esta contenido en la lista cursos
	print(" curso {0} a sido seleccionado..... ".format(curso)) # Si la validacion es correcta se imprime este mensaje
else:
	print("El curso que as ingresado no se encuentra en la lista de cursos que disponemos.........") # Else, que nos ejecuta si la validacion anterior no es correcta.