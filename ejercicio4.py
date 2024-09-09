"""
Elabore un programa para un Hospital que determine,
y muestre el nivel de Leucemia de 803 pacientes clasificando
su puntaje si esta inferior a 10 no tiene Leucemia; si esta entre 11 y 40,
nivel bajo de Leucemia; si esta entre 40 y 69, nivel moderado de Leucemia,
si esta entre 70 y 100, nivel grave de Leucemia.
"""

pacientes= 6

for i in range(pacientes):

    puntajeLeucemia = int(input("Digite el puntaje de Leucemia: \n"))

    if(puntajeLeucemia >= 1 and puntajeLeucemia <= 10):
      print(f"Puntaje de leicemia: {puntajeLeucemia}. No tiene Leucemia")
    elif(puntajeLeucemia >= 11 and puntajeLeucemia <= 40):
        print(f"Puntaje de leicemia: {puntajeLeucemia}. Nivel bajo de Leucemia")
    elif(puntajeLeucemia >= 41 and puntajeLeucemia <= 69):
        print(f"Puntaje de leicemia: {puntajeLeucemia}. Nivel moderado de Leucemia")
    elif(puntajeLeucemia >=70 and puntajeLeucemia <= 100):
        print(f"Puntaje de leicemia: {puntajeLeucemia}. Nivel Grave de Leucemia")
    else:
        print("No existe Puntaje de leucemia, ingrese un valor correcto")
    