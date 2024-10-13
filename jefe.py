from empleado import Empleado

class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, salario, dni, fecha_vinculacion, area=None, jefe=None):
        super().__init__(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        self.jefe = jefe if jefe else ""  
        self.area = area if area else ""  
        self.empleados_a_cargo = []

    def agregar_empleado_existen(self, empleado_agregar):
        """Asigna este jefe al empleado existente basado en su DNI."""
        empleado_dni = empleado_agregar.dni  

        try:
            with open("./archivos/empleados.txt", "r") as f:
                empleados = f.readlines()
        except FileNotFoundError:
            print("Archivo de empleados no encontrado.")
            return

        for i, empleado in enumerate(empleados):
            datos = empleado.strip().split(",")
            if datos[4] == empleado_dni:
                datos[6] = self.obtener_nombre_completo()  
                empleados[i] = ",".join(datos) + "\n"
                print(f"Jefe {self.obtener_nombre_completo()} asignado al empleado {datos[0]} {datos[1]}.")  
                break
        else:
            print(f"No se encontró un empleado con DNI: {empleado_dni}")

        with open("./archivos/empleados.txt", "w") as fw:
            fw.writelines(empleados)

    def asignar_area_empleado(self, empleado_dni, area_nombre):
        """Asigna un área a un empleado existente basado en su DNI"""
        print(f"Buscando empleado con DNI: {empleado_dni}")  

        try:
            with open("./archivos/empleados.txt", "r") as f:
                empleados = f.readlines()
        except FileNotFoundError:
            print("Archivo de empleados no encontrado.")
            return

        empleado_encontrado = False
        for i, empleado in enumerate(empleados):
            datos = empleado.strip().split(",")
            print(f"Verificando empleado: {datos[0]} {datos[1]}, DNI: {datos[4]}")  
            if datos[4] == empleado_dni:
                print(f"Empleado encontrado: {datos[0]} {datos[1]}")  
                datos[7] = area_nombre  
                empleados[i] = ",".join(datos) + "\n"
                empleado_encontrado = True
                print(f"Área '{area_nombre}' asignada al empleado {datos[0]} {datos[1]}.")  
                break

        if not empleado_encontrado:
            print(f"No se encontró un empleado con DNI: {empleado_dni}")

        with open("./archivos/empleados.txt", "w") as fw:
            fw.writelines(empleados)
            if empleado_encontrado:
                print("Archivo 'empleados.txt' actualizado.")  

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
        return datos  

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
