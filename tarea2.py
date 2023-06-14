numero=int(input("Ingrese algun numero:"))
i=0
numero2 = []
for x in range(2, numero+1, 1):
    i=numero%x
    if i == 0:
        i=numero/x
        numero2.append(i)  
if len(numero2) != 1 :
    print(f",{numero2}")
else:
    print("El numero no es perfecto")