"""
	importacion de Archivos Externos
	Esta funcion nos permite 
"""

try:
	from Curso.modulos.funcionesMatematicas import*
	
	print(Sumar(3,5))
	
	print(Restar(15,9))
Except:
	print("""Este programa a sido colocado dentro de un try ya que aqui se usa importacion de archivos
	y no existe esa ruta por tanto solo se lo deja como muestra.
	Cabe recalcar que en la funcion a la que se llama, existen creadas dos funciones una de suma y otra de resta
	las cuales piden 2 parametros (numeros) dentro de su codigo.
	""")
