from empleado import Empleado
from jefe import Jefe
from area import Area
from manejo_archivos import ManejoArchivos
import tools as tl
# Registrar empleados

while True: 
    tl.menu()
    op = input("Por favor ingrese una opcion: ")

    if op == "1":
        while True:

            print("""
                    Que tipo de empleado queire registrar
                    1. Jefe
                    2. Empleado simple
                    3. Salir de registro de empleados
                    """)
        
            ope = input("Ingrese una opcion: ")

            if ope == "1":
                print("Registrando jefe")
                
                n,a,e,s,dni,fv = tl.datos_empleado()
                print("Deseas ")
                jefe = Empleado(n,a,e,s,dni,fv)

            elif ope == "2":
                print("Registrando empleado simple")

                n,a,e,s,dni,fv = tl.datos_empleado()
                empleado_r = Empleado(n,a,e,s,dni,fv)

                tl.agregar_empleado_documento('archivos/empleados.txt', empleado_r.enviar_informacion())

            elif ope == "3":
                print("Saliendo del registro de empleados")
                break
            else:
                print("Opcion invalida intente de nuevo")
        
    elif op == "2":
        print("Registrando Area")
    elif op == "3":
        print("Consultando infromacion del area")
    elif op == "4":
        print("Consultando infromacin del empleado")
    elif op == "5":
        print("Saliendo del sistema....")
        break
    else:
        print('Opcion invalida ingrese nuevamente')
    
