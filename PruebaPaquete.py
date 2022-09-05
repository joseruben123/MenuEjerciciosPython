"""
Paquetes :
son directorios o carpetas donde se almacenan modulos relacionados entre si

¿Para que sirven?
para organizar mejor el codigo y poder reutilizarlo mejor (modularizacion y reutilizacion)

¿Como se crea un paquete?
crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es convertir un directorio en un modulo (paquete)
que contiene otros modulos, y esto lo hace para poder importarlos.

"""
# para la ejecucion de este codigo se creo un paquete en pycharm con el nombre paquete1 y ahi se creo un archivo .py con el nombre que indica
# para poder subirlo aqui en GitHub quedo esto obsoleto porque faltaria la ruta que pediria el archivo al ser ejecutado

from paquete1.funcionesNumericas import*   # Esta linea importa las funciones del archivo funcionesNumericas
from paquete1.funcionesCadena import *    # Esta linea importa las funciones del archivo funcionesCadena


print(multiplicar(5, 6))

print(ContarLetras("HolaMundo"))
