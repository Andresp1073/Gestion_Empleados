class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = ''

    def crear_documento(self):
        f = open(self.nombre, 'x')
        f.close()

    def optener_informacion(self, nombre_documento):
        f = open(nombre_documento, 'r')
        self.contenido = f.read()

    def agregar_empleado_documento(self, nombre_documento,empleado):
        f = open(nombre_documento , 'a')
        f.write(empleado + "\n")
        f.close()
        

