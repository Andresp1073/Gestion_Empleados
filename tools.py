def menu():

    print("""
        Bienvenido a su sistema de gestion de empleados
      Que quiere hacer el dia de hoy 
      1. Registrar empleado
      2. Registrar Area
      3. Consultar informacion de area
      4. Consultar informacion de empleado
      5. Salir del sistema   

      """)
    
def datos_empleado():
    nombre =  input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad =  int(input("Ingresa la edad: "))
    salario = int(input("Ingrese el salario: "))
    dni = int(input("Ingrese el DNI: "))
    fecha_vinculacion =  input("Ingresar fecha de vinculacion: ")
    return nombre, apellido, edad, salario, dni, fecha_vinculacion

def agregar_empleado_documento(nombre_documento,empleado):
    f = open(nombre_documento , 'a')
    f.write(empleado + "\n")
    f.close()


def mostrar_empleados():
    print("   |Nombre|Apellido|Edad|Salario|DNI|Fecha vinculacion|Jefe|Area")
    print("--------------------------------------------------------------")

    f = open("./archivos/empleados.txt", "r")

    empleados = f.readlines()
    f.close()

    for i,empleado in enumerate(empleados):
        print(f"|{i}| {empleado}")
        print("--------------------------------------------------------")

def motrar_jefes():
    print("   |Nombre|Apellido|Edad|Salario|DNI|Fecha vinculacion|Area")
    print("--------------------------------------------------------------")

    f = open("./archivos/jefes.txt", "r")

    jefes = f.readlines()
    f.close()

    for i,jefe in enumerate(jefes):
        print(f"|{i}| {jefe}")
        print("--------------------------------------------------------")

def mostrar_areas():
    print("Areas del sistema")
    print("--------------------------------------------------------------")
    f = open("./archivos/areas.txt", "r")

    areas = f.readlines()
    f.close()

    for i, area in enumerate(areas):
        datos = area.split(",")
        print(f"Area {i}")
        print(f"Nombre: {datos[0]}")
        print(f"Descripcion: {datos[1]}")
        print("-------------------------------------------------------------")