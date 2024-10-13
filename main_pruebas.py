from empleado import Empleado
from jefe import Jefe
from area import Area
import tools as tl

def menu():
    print("""
    Bienvenido a su sistema de gestión de empleados
    ¿Qué quiere hacer el día de hoy?
    1. Registrar empleado
    2. Registrar Área
    3. Consultar información de área
    4. Consultar información de empleado
    5. Asignar Área a Empleado
    6. Asignar Jefe a Empleado
    7. Salir del sistema
    """)

def datos_empleado():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    try:
        edad = int(input("Ingresa la edad: "))
    except ValueError:
        print("Edad inválida. Debe ser un número.")
        return None
    try:
        salario = int(input("Ingrese el salario: "))
    except ValueError:
        print("Salario inválido. Debe ser un número.")
        return None
    try:
        dni = int(input("Ingrese el DNI: "))
    except ValueError:
        print("DNI inválido. Debe ser un número.")
        return None
    fecha_vinculacion = input("Ingresar fecha de vinculación (dd/mm/yyyy): ")
    return nombre, apellido, edad, salario, dni, fecha_vinculacion

def registrar_empleado():
    datos = datos_empleado()
    if datos:
        nombre, apellido, edad, salario, dni, fecha_vinculacion = datos
        empleado = Empleado(nombre, apellido, edad, salario, dni, fecha_vinculacion)
        # Guardar el empleado en el archivo con jefe y área como "Sin asignar"
        with open("./archivos/empleados.txt", "a") as f:
            f.write(f"{empleado.nombre},{empleado.apellido},{empleado.edad},{empleado.salario},{empleado.dni},{empleado.fecha_vinculacion},Sin asignar,Sin asignar\n")
        print(f"Empleado {empleado.obtener_nombre_completo()} registrado exitosamente.")

def registrar_area():
    nombre_area = input("Ingrese el nombre del área: ")
    descripcion_area = input("Ingrese la descripción del área: ")
    area = Area(nombre_area, descripcion_area)
    # Guardar el área en el archivo
    with open("./archivos/areas.txt", "a") as f:
        f.write(f"{area.nombre},{area.descripcion}\n")
    print(f"Área {area.nombre} registrada exitosamente.")

def consultar_area():
    with open("./archivos/areas.txt", "r") as f:
        areas = f.readlines()
    if not areas:
        print("No hay áreas registradas en el sistema.")
        return
    print("Áreas registradas:")
    for area in areas:
        print(area.strip())

def consultar_empleado():
    with open("./archivos/empleados.txt", "r") as f:
        empleados = f.readlines()
    if not empleados:
        print("No hay empleados registrados en el sistema.")
        return
    print("Empleados registrados:")
    for empleado in empleados:
        print(empleado.strip())

def asignar_area():
    # Mostrar áreas disponibles
    with open("./archivos/areas.txt", "r") as f:
        areas = [linea.strip().split(",") for linea in f.readlines()]

    if not areas:
        print("No hay áreas registradas en el sistema.")
        return

    print("Áreas disponibles:")
    for idx, area in enumerate(areas):
        print(f"{idx}: {area[0]} - {area[1]}")

    try:
        indice_area = int(input("Seleccione el área por índice: "))
        if not (0 <= indice_area < len(areas)):
            print("Índice de área inválido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return

    area_nombre = areas[indice_area][0]

    # Mostrar empleados
    tl.mostrar_empleados()

    try:
        indice_empleado = int(input("Ingresar índice del empleado para asignar el área: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return

    with open("./archivos/empleados.txt", "r") as f:
        empleados = f.readlines()

    if not (0 <= indice_empleado < len(empleados)):
        print("Índice de empleado inválido.")
        return

    empleado_datos = empleados[indice_empleado].strip().split(",")
    empleado_dni = str(empleado_datos[4])

    # Mostrar jefes
    with open("./archivos/jefes.txt", "r") as f:
        jefes = f.readlines()

    if not jefes:
        print("No hay jefes registrados para asignar áreas.")
        return

    print("Seleccione un jefe que realizará la asignación del área:")
    for idx, jefe_linea in enumerate(jefes):
        jefe_info = jefe_linea.strip().split(",")
        print(f"{idx}: {jefe_info[0]} {jefe_info[1]}")

    try:
        indice_jefe_asignacion = int(input("Seleccione el jefe por índice: "))
        if not (0 <= indice_jefe_asignacion < len(jefes)):
            print("Índice de jefe inválido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return

    jefe_info = jefes[indice_jefe_asignacion].strip().split(",")
    jefe = Jefe(
        nombre=jefe_info[0],
        apellido=jefe_info[1],
        edad=jefe_info[2],
        salario=jefe_info[3],
        dni=jefe_info[4],
        fecha_vinculacion=jefe_info[5]
    )

    # Asignar el área
    jefe.asignar_area_empleado(empleado_dni, area_nombre)
    print(f"Área '{area_nombre}' asignada al empleado {empleado_datos[0]} {empleado_datos[1]} por el jefe {jefe.nombre} {jefe.apellido}.")

def asignar_jefe():
    # Mostrar jefes disponibles
    with open("./archivos/jefes.txt", "r") as f:
        jefes = [linea.strip().split(",") for linea in f.readlines()]

    if not jefes:
        print("No hay jefes registrados en el sistema.")
        return

    print("Jefes disponibles:")
    for idx, jefe in enumerate(jefes):
        print(f"{idx}: {jefe[0]} {jefe[1]} - DNI: {jefe[4]}")

    try:
        indice_jefe = int(input("Seleccione el jefe por índice: "))
        if not (0 <= indice_jefe < len(jefes)):
            print("Índice de jefe inválido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return

    jefe_info = jefes[indice_jefe]
    jefe = Jefe(
        nombre=jefe_info[0],
        apellido=jefe_info[1],
        edad=jefe_info[2],
        salario=jefe_info[3],
        dni=jefe_info[4],
        fecha_vinculacion=jefe_info[5]
    )

    # Mostrar empleados
    tl.mostrar_empleados()

    try:
        indice_empleado = int(input("Ingresar índice del empleado para asignar el jefe: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return

    with open("./archivos/empleados.txt", "r") as f:
        empleados = f.readlines()

    if not (0 <= indice_empleado < len(empleados)):
        print("Índice de empleado inválido.")
        return

    empleado_datos = empleados[indice_empleado].strip().split(",")
    empleado = Empleado(
        nombre=empleado_datos[0],
        apellido=empleado_datos[1],
        edad=empleado_datos[2],
        salario=empleado_datos[3],
        dni=empleado_datos[4],
        fecha_vinculacion=empleado_datos[5]
    )

    # Asignar el jefe al empleado
    empleado.asignar_jefe(jefe.obtener_nombre_completo())
    print(f"Jefe '{jefe.obtener_nombre_completo()}' asignado al empleado '{empleado.obtener_nombre_completo()}'.")
    
def main():
    while True:
        menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                registrar_empleado()
            elif opcion == 2:
                registrar_area()
            elif opcion == 3:
                consultar_area()
            elif opcion == 4:
                consultar_empleado()
            elif opcion == 5:
                asignar_area()
            elif opcion == 6:
                asignar_jefe()
            elif opcion == 7:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
