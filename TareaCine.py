ciclo=1
total=0
while ciclo == 1:
    try:
        cliente=int(input("¿Usted pertenece al duoc?\nPresione [1] si pertenece al Duoc \nPresione [0] si no pertenece al Duoc\n")) 
        entrada=int(input("¿Que entrada desea?\nPresione [1] para estreno $4.800 \nPresione [2] para entrada normal $2.900\n"))
        centrada=int(input("¿Cuantas entradas desea?: "))
        if entrada == 1:
             total=4800*centrada
        else:
            total=2900*centrada
        if cliente == True:
            total=total*0.7
        comida=int(input("¿Desea Agregar palomitas/bebida a su pedido?\nPresione [0] si no quiere\nPresione [1] si quiere\n"))
        if comida == 1:
            palomita=int(input("¿Que palomitas desea llevar?\nPresione [0] si no desea Palomitas\nPresione [1] si desea palomitas pequeñas $2.500\nPresione [2] Si desea palomitas mediana $4.500\nPresione [3] si desea palomitas grandes $7.800\n"))                
            if palomita == 0:
                print("Usted no lleva cabritas")
            if palomita == 1:
                print("Usted Selecciono Palomitas pequeñas")
                total+=2500
            if palomita == 2:
                print("Usted Selecciono Palomitas medianas")
                total+=4500   
            if palomita == 3:
                print("Usted Selecciono Palomitas Grandes")    
                total+=7800
            bebida=int(input("¿Que bebida desea llevar?\nPresione [0] si no desea bebida\nPresione [1] si desea bebida pequeña $1.000\nPresione [2] Si desea bebida mediana $1.250\nPresione [3] si desea bebida grande $2.000\n"))
            if bebida == 0:
                print("Usted no lleva bebida")
                if bebida == 1:
                    print("Usted Selecciono bebida pequeña")
                    total+=1000
                if bebida == 2:
                    print("Usted Selecciono bebida mediana")
                    total+=1250   
                if bebida == 3:
                    print("Usted Selecciono bebida Grande")    
                    total+=2000
        ciclo=int(input("¿Si desea salir?. Presione 0 si no presione cualquier tecla y pulse enter. "))    
    except:
        print("Opcion erronea, ingrese nuevamente")
print("El total a pagar es $",total)
vuelto=int(input("¿Con Cuanto $ desea cancelar?\n"))
if vuelto >= total:
    vuelto-=total
    print("Su vuelto es de $")
else:
    print("Dinero insuficiente")    
