"""
    Uso de los metods get y set
"""
class Cuenta():
    def __init__(self,pro ,sal ,mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Metodo Get

    def get_saldo(self):
        return self.__saldo

    def get_propietario(self):
        return self.__propietario

    def get_moneda(self):
        return self.__moneda

    def set_Moneda(self,moneda):
        self.__moneda = moneda

cuenta1 = Cuenta("Ramiro Fuente", 14800, "Soles")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())

cuenta1.set_Moneda("Dolares")
print(cuenta1.get_moneda())
