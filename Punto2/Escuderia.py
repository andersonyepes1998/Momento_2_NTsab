from Piloto import Piloto


class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__casaMotor = None
        self.__pilotoPrincipal = Piloto()
        self.__pilotoSuplente = Piloto()
        self.__costoAnual = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property
    def casaMotor(self):
        return self.__casaMotor

    @casaMotor.setter
    def casaMotor(self, dato):
        self.__casaMotor = dato

    @property
    def pilotoPrincipal(self):
        return self.__pilotoPrincipal

    @pilotoPrincipal.setter
    def pilotoPrincipal(self, dato):
        self.__pilotoPrincipal = dato

    @property
    def pilotoSuplente(self):
        return self.__pilotoSuplente

    @pilotoSuplente.setter
    def pilotoSuplente(self, dato):
        self.__pilotoSuplente = dato

    @property
    def costoAnual(self):
        return self.__costoAnual

    @costoAnual.setter
    def costoAnual(self, dato):
        self.__costoAnual = dato