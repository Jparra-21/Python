import random
from array import *
fila = [[],[],[]]
mayor = -1
menor = 101
suma = 0
for i in range(3):
    for x in range(3):
        fila[i].insert(x, random.randint(0, 100))
        suma=suma+fila[i][x]
        if mayor < fila[i][x]:
            mayor=fila[i][x]
        elif menor > fila[i][x]:
            menor=fila[i][x] 
print("El numero mayor es", mayor)
print("El numero menor es", menor)
print("La suma total es", suma)
print("El promedio es", int(suma/(len(fila)*3)))
print("La diagonal principal es: ", end="")
for i in range(3):
    print(fila[i][i], end="-")
print("\n",fila)

