class Piloto:
    def __init__(self):
        self.__nombre = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

   
