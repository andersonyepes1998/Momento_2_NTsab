class Coctel:
    def __init__(self):
        self.__nombre = None
        self.__precio = None
        self.__grados = None

    # ======= geters =======
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def grados(self):
        return self.__grados

    # ===== Setters ========
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @grados.setter
    def grados(self, grados):
        self.__grados = grados
