from empleado import Empleado
from jefe import Jefe
from area import Area
import tools as tl

def main():
    while True:
        tl.menu()
        op = input("Por favor ingrese una opción: ")

        if op == "1":
            while True:
                print("""
¿Qué tipo de empleado quiere registrar?
1. Jefe
2. Empleado simple
3. Salir de registro de empleados
""")

                ope = input("Ingrese una opción: ")

                if ope == "1":
                    print("Registrando jefe")
                    datos = tl.datos_empleado()
                    if datos:
                        nombre, apellido, edad, salario, dni, fecha_vinculacion = datos
                        asignar_jefe = input("¿Desea asignar un jefe a este jefe? (s/n): ").lower()
                        jefe_asignado = ""
                        if asignar_jefe == "s":

                            tl.mostrar_jefes()
                            try:
                                indice_jefe = int(input("Seleccione el índice del jefe: "))
                            except ValueError:
                                print("Entrada no válida. Se asignará 'Sin asignar'.")
                            else:
                                try:
                                    with open('./archivos/jefes.txt', "r") as f:
                                        jefes = f.readlines()
                                    if 0 <= indice_jefe < len(jefes):
                                        jefe_datos = jefes[indice_jefe].strip().split(",")
                                        jefe_asignado = f"{jefe_datos[0]} {jefe_datos[1]}"
                                    else:
                                        print("Índice de jefe inválido. Se asignará 'Sin asignar'.")
                                except FileNotFoundError:
                                    print("Archivo de jefes no encontrado. Se asignará 'Sin asignar'.")

                        asignar_area = input("¿Desea asignar un área a este jefe? (s/n): ").lower()
                        area_asignada = ""
                        if asignar_area == "s":
                            tl.mostrar_areas()
                            try:
                                indice_area = int(input("Seleccione el índice del área: "))
                            except ValueError:
                                print("Entrada no válida. Se asignará 'Sin asignar'.")
                            else:
                                try:
                                    with open('./archivos/areas.txt', "r") as f:
                                        areas = f.readlines()
                                    if 0 <= indice_area < len(areas):
                                        area_datos = areas[indice_area].strip().split(",")
                                        area_asignada = area_datos[0]
                                    else:
                                        print("Índice de área inválido. Se asignará 'Sin asignar'.")
                                except FileNotFoundError:
                                    print("Archivo de áreas no encontrado. Se asignará 'Sin asignar'.")

                        jefe = Jefe(
                            nombre=nombre,
                            apellido=apellido,
                            edad=edad,
                            salario=salario,
                            dni=dni,
                            fecha_vinculacion=fecha_vinculacion,
                            jefe=jefe_asignado,
                            area=area_asignada
                        )
                        # Guardar la información del jefe
                        tl.agregar_empleado_documento('./archivos/jefes.txt', jefe.enviar_informacion())
                        print(f"Jefe {jefe.obtener_nombre_completo()} registrado exitosamente.")
                elif ope == "2":
                    print("Registrando empleado simple")
                    datos = tl.datos_empleado()
                    if datos:
                        nombre, apellido, edad, salario, dni, fecha_vinculacion = datos
                        empleado = Empleado(nombre, apellido, edad, salario, dni, fecha_vinculacion)
                        tl.agregar_empleado_documento('./archivos/empleados.txt', empleado.enviar_informacion())
                        print(f"Empleado {empleado.obtener_nombre_completo()} registrado exitosamente.")
                elif ope == "3":
                    print("Saliendo del registro de empleados")
                    break
                else:
                    print("Opción inválida, intente de nuevo")

        elif op == "2":
            print("Registrando Área")
            nombre_area = input("Ingrese el nombre del área: ")
            descripcion_area = input("Ingrese la descripción del área: ")
            area = Area(nombre_area, descripcion_area)
            # Guardar la información del área
            tl.agregar_empleado_documento('./archivos/areas.txt', area.enviar_informacion())
            print(f"Área {area.nombre} registrada exitosamente.")

        elif op == "3":
            print("Consultando información del área")
            tl.mostrar_areas()

        elif op == "4":
            print("Consultando información del empleado")
            tl.mostrar_empleados()

        elif op == "5":
            print("Asignando Área a Empleado")
            tl.asignar_area()

        elif op == "6":
            print("Asignando Jefe a Empleado")
            tl.asignar_jefe()

        elif op == "7":
            print("Saliendo del sistema....")
            break
        else:
            print('Opción inválida, ingrese nuevamente')

if __name__ == "__main__":
    main()
