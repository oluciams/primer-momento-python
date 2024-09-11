"""
Elabore un programa para la Universidad de Florida 
que calcule los primeros 100 números de la siguiente
serie 5, 8, 13, 21, ... sin mostrar el 13, y
muestre la lista del resultado de los números.
"""

serie = []
numero1 = 5
numero2 = 8

serie.append(numero1)
serie.append(numero2)

while len(serie) < 8:
    siguiente = numero1 + numero2

    if siguiente == 13:
        numero1, numero2 = numero2, siguiente 
        continue

    serie.append(siguiente)    

    numero1, numero2 = numero2, siguiente

print(serie)
