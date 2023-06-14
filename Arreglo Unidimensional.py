import random
import statistics as stats
rango = []
mayor = -1
menor = 101
suma = 0
for i in range(10):
    rango.append(random.randint(0, 100))
    suma=suma+rango[i]
    if mayor < rango[i]:
        mayor=rango[i]
    elif menor > rango[i]:
        menor=rango[i]     
print("El numero mayor es", mayor)
print("El numero menor es", menor)
print("El promedio es", round(stats.mean(rango)))
print("La suma total es", suma)
print(rango)
