import random
import string
opcion=int(input("Presione [1] para grabar un MPN.\nPresione [2] Para buscar un MPN.\nPresione [3] para imprimir MPN.\nPresione [4] para salir.\n "))
empresa=['Huaweii', 'HP']
MPN=[]
modelo=[]
precio=[]
def grabar (empresa_mpn, modelo_1, costo):
    MPN1=str(random.randint(100000, 999999))
    if empresa_mpn == 'HP':
        MPN1+="-"+empresa_mpn[0]+str(random.randint(1, 9))*2+"-"+str(random.randint(1, 9))
    else:
        MPN1+="-"+random.choice(string.ascii_uppercase)+str(random.randint(1, 9))*2     
    print(MPN1, modelo_1)
    MPN.append(MPN1)         
    modelo.append(modelo_1)
    precio.append(costo)
def buscar (mpn_busqueda):
    for i in range(len(MPN)):
        if mpn_busqueda == MPN[i]:
            if precio[i]>= 500:
                print("El MPN es: ",MPN[i])
                print("El modelo es: ",modelo[i])
                print("Su precio es de: $",precio[i]," pesos")
            else:
                print("Producto sin stock")    
def imprimir(modelo_imprimir):
    for i in range(len(MPN)):
        if modelo_imprimir == MPN[i]:
            print("El MPN es: ",MPN[i],"\n----------")
            print("El modelo es: ",modelo[i],"\n----------")
            print("Su precio es de: $",precio[i]," pesos","\n----------")
      
while opcion >= 1 and opcion <= 3:
    try:
        if opcion == 1:
            print("Grabar")
            empresa_mpn=str(input("Ingrese la empresa del producto Huaweii o HP\n"))
            modelo_1=str(input("Ingrese nombre completo del producto incluyendo la marca\n"))
            costo=int(input("Ingrese e lcosto del producto en $\n"))
            grabar(empresa_mpn, modelo_1, costo)
        elif opcion == 2:
            print("Buscar")
            mpn_busqueda=str(input("Ingrese el MPN del producto que desea buscar\n"))
            buscar(mpn_busqueda)
        elif opcion == 3:
            print("Imprimir")
            modelo_imprimir=str(input("Ingrese el MPN del producto que desea imprimir\n"))
            imprimir(modelo_imprimir)
        salir=int(input("Presione [1] para continuar\nPresione [2] para salir.\n "))
        if salir == 2:
            opcion = 4
        else:
            opcion=int(input("Presione [1] para grabar un MPN.\nPresione [2] Para buscar un MPN.\nPresione [3] para imprimir MPN.\nPresione [4] para salir.\n "))
    except:
        print("Ingrese Nuevamente al programa")
print("Usted Salio del Programa ")                   