"""
Elabore un programa para la facultad de Ingeniería que pida 400 números
e indique si ese número es par o impar; me muestre un listado y 
me indique cuantos son pares y cuantos son impares.
"""
cantidad= 4
numeros = []
numerosPares = 0
numerosImpares = 0  

for i in range(cantidad): 
    numero = int(input("Digite un numero entero positivo: \n"))    
    numeros.append(numero)

    if(numero%2 == 0):        
        print(f"El número {numero}: Es numero Par")
        numerosPares = numerosPares + 1
    else:
        print(f"El número {numero}: Es numero Impar")
        numerosImpares = numerosImpares +1
    
print("**Lista de numeros**")
for numero in numeros:
  print(numero)

print(f"El total de numeros pares es: {numerosPares}")
print(f"El total de numeros impares es: {numerosImpares}")

