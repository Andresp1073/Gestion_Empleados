class Empleado:
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = str(edad)
        self.salario = str(salario)
        self.dni = str(dni)
        self.fecha_vinculacion = fecha_vinculacion
        self.jefe = "Sin asignar"
        self.area = "Sin asignar"

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def enviar_informacion(self):
        atributos = [
            self.nombre,
            self.apellido,
            self.edad,
            self.salario,
            self.dni,
            self.fecha_vinculacion,
            self.jefe,
            self.area
        ]
        datos = ",".join(atributos)
        return datos  # Retornamos la cadena en lugar de escribir en el archivo

    def asignar_jefe(self, nombre_jefe):
        """Asigna un jefe al empleado y actualiza el archivo de empleados."""
        self.jefe = nombre_jefe
        # Actualizar el archivo empleados.txt
        try:
            with open("./archivos/empleados.txt", "r") as f:
                empleados = f.readlines()
        except FileNotFoundError:
            print("Archivo de empleados no encontrado.")
            return

        with open("./archivos/empleados.txt", "w") as f:
            for empleado in empleados:
                datos = empleado.strip().split(",")
                if datos[4] == self.dni:
                    datos[6] = nombre_jefe  # Asignar jefe
                    f.write(",".join(datos) + "\n")
                else:
                    f.write(empleado)

    def asignar_area(self, area_nombre):
        """Asigna un área al empleado y actualiza el archivo de empleados."""
        self.area = area_nombre
        # Actualizar el archivo empleados.txt
        try:
            with open("./archivos/empleados.txt", "r") as f:
                empleados = f.readlines()
        except FileNotFoundError:
            print("Archivo de empleados no encontrado.")
            return

        with open("./archivos/empleados.txt", "w") as f:
            for empleado in empleados:
                datos = empleado.strip().split(",")
                if datos[4] == self.dni:
                    datos[7] = area_nombre  # Asignar área
                    f.write(",".join(datos) + "\n")
                else:
                    f.write(empleado)
