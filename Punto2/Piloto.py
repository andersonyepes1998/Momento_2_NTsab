class Piloto:
    def __init__(self):
        self.__nombre = None
        self.__salarioAnual = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    
    @property
    def salarioAnual(self):
        return self.__salarioAnual

    @salarioAnual.setter
    def salarioAnual(self, dato):
        self.__salarioAnual = dato

    