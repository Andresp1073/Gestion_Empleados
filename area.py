class Area:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def enviar_informacion(self):
        return f"{self.nombre},{self.descripcion}"
