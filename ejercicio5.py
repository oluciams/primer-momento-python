"""
Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable,
registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso,
si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.
"""
cabinas = 6

for i in range(cabinas):

    puntos = input("Digite puntaje de la cabina: ")

    match puntos:
      case '2':
          print(f"Puntaje de la cabina fue de {puntos}: Tiene un funcionamiento defectuoso")
      case '3':
          print(f"Puntaje de la cabina fue de {puntos}: Tiene un funcionamiento moderado")
      case '4':
          print(f"Puntaje de la cabina fue de {puntos}: Tiene un funcionamiento óptimo")
      case _:
          print(f"Puntaje de la cabina fue de {puntos}: No hay tipo de funcionamiento asignado")