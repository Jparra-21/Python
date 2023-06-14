opcion=int(input("Presione [1] para calcular el IVA.\nPresione [2] Para calcular el descuento.\nPresione [3] para calcular IMC.\nPresione [4] para salir.\n "))
def Calcular_IVA (precio):
    iva=precio*0.19
    return(iva)
def Descuento (precio, des):
    des=precio*(des/100)
    des=precio-des
    return(des)
def Calcular_IMC(estatura, peso):
    imc=peso/estatura**2
    imc2=[18.5, 24.9, 29.9, 34.9, 39.4, 40]
    imc3=["Bajo Peso", "Adecuado", "Sobrepeso", "Obesidad grado 1", "Obesidad grado 2", "Obesidad Grado 3"]
    for i in range(len(imc2)):
        if imc <= imc2[i]:
            imc_3=imc3[i]
            break
    print("Su IMC es de: ", round(imc, 1))
    print("Lo que corresponde a un nivel: ", imc_3)             
while opcion >= 1 and opcion <= 3:
    try:
        if opcion == 1:
            print("IVA")
            precio=int(input("Ingrese el valor del producto que desea calcular el IVA:\n"))
            print("El IVA a pagar por su producto es :", Calcular_IVA(precio))
        elif opcion == 2:
            print("Descuento")
            precio=int(input("Ingrese el valor del producto que desea calcular el Descuento:\n"))
            des=int(input("Ingrese el descuento que desea aplicar:\n"))
            print("El precio a pagar por su producto es :", Descuento(precio, des))
        elif opcion == 3:
            print("IMC")
            estatura=float(input("Ingrese su estatura en metros:\n"))
            peso=float(input("Ingrese su peso en KG:\n"))
            Calcular_IMC(estatura, peso)
        salir=int(input("Presione [1] para continuar\nPresione [2] para salir.\n "))
        if salir == 2:
            opcion = 4
        else:
            opcion=int(input("Presione [1] para calcular el IVA.\nPresione [2] Para calcular el descuento.\nPresione [3] para calcular IMC.\nPresione [4] para salir.\n "))
    except:
        print("Ingrese Nuevamente al programa")
print("Usted Salio del Programa ")                   