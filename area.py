class Area:

    def __init__(self, nombre, decripcion):
        self.nombre = nombre
        self.descripcion = decripcion
        self.lista_empleados = []

    def agregar_empelado(self, empleado):
        self.lista_empleados.append(empleado)

    def enviar_informacion(self):
        datos = self.nombre + "," +self.descripcion

        f = open('./archivos/areas.txt', "a")
        f.write(datos + "\n")
        f.close()