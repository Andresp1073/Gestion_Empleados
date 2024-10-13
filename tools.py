from empleado import Empleado
from jefe import Jefe
from area import Area

def menu():
    print("""
Bienvenido a su sistema de gestión de empleados
¿Qué quiere hacer el día de hoy?
1. Registrar empleado
2. Registrar Área
3. Consultar información de Área
4. Consultar información de Empleado
5. Asignar Área a Empleado
6. Asignar Jefe a Empleado
7. Salir del sistema
""")

def datos_empleado():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    while True:
        try:
            edad = int(input("Ingresa la edad: "))
            break
        except ValueError:
            print("Edad inválida. Debe ser un número.")
    while True:
        try:
            salario = float(input("Ingrese el salario: "))
            break
        except ValueError:
            print("Salario inválido. Debe ser un número.")
    while True:
        try:
            dni = int(input("Ingrese el DNI: "))
            break
        except ValueError:
            print("DNI inválido. Debe ser un número.")
    fecha_vinculacion = input("Ingresar fecha de vinculación (dd/mm/yyyy): ")
    return nombre, apellido, edad, salario, dni, fecha_vinculacion

def agregar_empleado_documento(nombre_documento, empleado):
    with open(nombre_documento, 'a') as f:
        f.write(empleado + "\n")

def mostrar_empleados():
    print("   | Nombre | Apellido | Edad | Salario | DNI | Fecha Vinculación | Jefe | Área")
    print("-------------------------------------------------------------------------------")

    try:
        with open("./archivos/empleados.txt", "r") as f:
            empleados = f.readlines()
    except FileNotFoundError:
        empleados = []

    for i, empleado in enumerate(empleados):
        print(f"| {i} | {empleado.strip()}")
        print("-------------------------------------------------------------------------------")

def mostrar_jefes():
    print("   | Nombre | Apellido | Edad | Salario | DNI | Fecha Vinculación | Área")
    print("-------------------------------------------------------------------------------")

    try:
        with open("./archivos/jefes.txt", "r") as f:
            jefes = f.readlines()
    except FileNotFoundError:
        jefes = []

    for i, jefe in enumerate(jefes):
        print(f"| {i} | {jefe.strip()}")
        print("-------------------------------------------------------------------------------")

def mostrar_areas():
    print("Áreas del sistema")
    print("--------------------------------------------------------------")
    try:
        with open("./archivos/areas.txt", "r") as f:
            areas = f.readlines()
    except FileNotFoundError:
        areas = []

    for i, area in enumerate(areas):
        datos = area.strip().split(",")
        print(f"Área {i}")
        print(f"Nombre: {datos[0]}")
        print(f"Descripción: {datos[1]}")
        print("-------------------------------------------------------------")

def asignar_jefe(ruta_jefes='./archivos/jefes.txt', ruta_empleados='./archivos/empleados.txt'):
    print("Asignar Jefe a Empleado")
    mostrar_empleados()
    try:
        indice_empleado = int(input("Seleccione el índice del empleado al que asignar un jefe: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        return

    try:
        with open(ruta_empleados, "r") as f:
            empleados = f.readlines()
    except FileNotFoundError:
        print("Archivo de empleados no encontrado.")
        return

    if indice_empleado < 0 or indice_empleado >= len(empleados):
        print("Índice de empleado inválido.")
        return

    empleado_datos = empleados[indice_empleado].strip().split(",")
    empleado_dni = empleado_datos[4]

    
    mostrar_jefes()
    try:
        indice_jefe = int(input("Seleccione el índice del jefe: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        return

    try:
        with open(ruta_jefes, "r") as f:
            jefes = f.readlines()
    except FileNotFoundError:
        print("Archivo de jefes no encontrado.")
        return

    if indice_jefe < 0 or indice_jefe >= len(jefes):
        print("Índice de jefe inválido.")
        return

    jefe_datos = jefes[indice_jefe].strip().split(",")
    nombre_jefe = f"{jefe_datos[0]} {jefe_datos[1]}"

    
    jefe = Jefe(
        nombre=jefe_datos[0],
        apellido=jefe_datos[1],
        edad=int(jefe_datos[2]),
        salario=float(jefe_datos[3]),
        dni=jefe_datos[4],
        fecha_vinculacion=jefe_datos[5],
        area=jefe_datos[6] if len(jefe_datos) > 6 else "",
        jefe=jefe_datos[7] if len(jefe_datos) > 7 else ""
    )

    
    empleado = Empleado(
        nombre=empleado_datos[0],
        apellido=empleado_datos[1],
        edad=int(empleado_datos[2]),
        salario=float(empleado_datos[3]),
        dni=empleado_datos[4],
        fecha_vinculacion=empleado_datos[5]
    )

    
    jefe.agregar_empleado_existen(empleado)
    

def asignar_area(ruta_areas='./archivos/areas.txt', ruta_empleados='./archivos/empleados.txt'):
    print("Asignar Área a Empleado")
    mostrar_empleados()
    try:
        indice_empleado = int(input("Seleccione el índice del empleado al que asignar un área: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        return

    
    try:
        with open(ruta_empleados, "r") as f:
            empleados = f.readlines()
    except FileNotFoundError:
        print("Archivo de empleados no encontrado.")
        return

    if indice_empleado < 0 or indice_empleado >= len(empleados):
        print("Índice de empleado inválido.")
        return

    empleado_datos = empleados[indice_empleado].strip().split(",")
    empleado_dni = empleado_datos[4]

    
    mostrar_areas()
    try:
        indice_area = int(input("Seleccione el índice del área: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        return

    try:
        with open(ruta_areas, "r") as f:
            areas = f.readlines()
    except FileNotFoundError:
        print("Archivo de áreas no encontrado.")
        return

    if indice_area < 0 or indice_area >= len(areas):
        print("Índice de área inválido.")
        return

    area_datos = areas[indice_area].strip().split(",")
    area_nombre = area_datos[0]

    
    empleado = Empleado(
        nombre=empleado_datos[0],
        apellido=empleado_datos[1],
        edad=int(empleado_datos[2]),
        salario=float(empleado_datos[3]),
        dni=empleado_datos[4],
        fecha_vinculacion=empleado_datos[5]
    )

    
    empleado.asignar_area(area_nombre)
    print(f"Área '{area_nombre}' asignada al empleado {empleado.obtener_nombre_completo()}.")
