f = open('archivos/empleados.txt', 'r')

empleados = f.readlines()

f.close()

#print(empleados)

# Mostrar infromacion del documento empleados

print('   |DNI|Nombre|Apellido|Edad|Salario|Fecha de vinculación|')
for index, empleado in enumerate(empleados): 
    print("-----------------------------------------------------")
    print(f"{index}|  {empleado}")

# Seleccionar empleados

print("""Ingrese la lista de empleados a vincular por medio de la posocion de la lista 
      Tomando en cuenta el siguient formato: 
      empleado 1 en posiion 1 y empeado n en posicion n se ingresaria de la siguiente forma
      1,2,3,n.....""")

index_e = input("Ingre lista de indices de empleados a vincular: ")

index_e = index_e.split(",")

#print(type(index_e[0]))

empleados_seleccionados = []

for index, empleado in enumerate(empleados):
    for indice in index_e:
        if index == int(indice):
            empleados_seleccionados.append(empleado)

# mostrar empleados seleccioandos: 

print('   |DNI|Nombre|Apellido|Edad|Salario|Fecha de vinculación|')
for index, empleado in enumerate(empleados_seleccionados): 
    print("-----------------------------------------------------")
    print(f"{index}|  {empleado}")
