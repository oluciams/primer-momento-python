"""
Elabore un programa para el Éxito que determine el salario
de los 1897 empleados de su compañía, teniendo en cuenta
las comisiones y la seguridad social que debe pagar,
e imprima el listado de la información. 
"""
empleados = []

for i in range(2):
    nombre = input("Digita el Nombre del empleado: ")
    salario = int(input("Digita el salario del empleado: "))

    comisiones = salario * 2/100
    salud = salario * 4/100
    pension = salario * 4/100
    seguridadSocial = salud + pension

    totalPagar = salario + comisiones - seguridadSocial

    empleados.append({
      "nombre": nombre,
      "salario": salario,
      "comisiones": comisiones,
      "seguridadSocial": seguridadSocial,
      "totalPagar": totalPagar
    })


    print("\n****Lista de empleados****\n")
    print(f"Nombre \t Salario \t Comisiones \t Seguridad Social \t Total a pagar")
    for empleado in empleados: 
      print(f"{empleado['nombre']} \t $ {empleado['salario']:.2f} \t $ {empleado['comisiones']:.2f} \t $ {empleado['seguridadSocial']:.2f} \t \t $ {empleado['totalPagar']:.2f}")