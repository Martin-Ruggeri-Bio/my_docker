class Persona():
    def __init__(self, nombre=""):
        self.nombre = nombre

    def __str__(self):
        return "Nombre : %s" % self.nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value


if __name__ == '__main__':
    persona = Persona("Juan")
    print(persona)
