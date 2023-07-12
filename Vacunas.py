import random, string
opcion=int(input("Presione [1] para grabar datos de un ciudadano.\nPresione [2] Para buscar datos de un ciudadano.\nPresione [3] para imprimir certificado de vacunacion.\nPresione [4] para salir.\n "))
ciudadanos=[]
def grabar (rut_ciudadano, Lote_vacuna, año_vacuna, mes_vacuna, dia_vacuna, vacuna_administrada):
    fecha_vacuna=""
    if rut_ciudadano not in ciudadanos and rut_ciudadano < 30000000:
        print("Rut Correcto.")
        digito_verificador=str(input("Ingrese su digito verificador sin guion.\n"))
        rut_ciudadano=[str(rut_ciudadano)+"-"+digito_verificador]
        ciudadanos.append(rut_ciudadano)
    if rut_ciudadano in ciudadanos:
        if Lote_vacuna >= 2023:
            Lote=""
            for i in range(3):
                Lote+=random.choice(string.ascii_uppercase)
            Lote_vacuna=Lote+str(Lote_vacuna)
            rut_ciudadano.append(Lote_vacuna)
        else:
            print("Fecha de lote Incorrecta.")
        if año_vacuna > 2020:
            print("Fecha de vacuna valida.")
            dia_vacuna=str(dia_vacuna)
            mes_vacuna=str(mes_vacuna)
            año_vacuna=str(año_vacuna)
            fecha_vacuna=dia_vacuna+"/"+mes_vacuna+"/"+año_vacuna
            rut_ciudadano.append(fecha_vacuna)
        elif mes_vacuna >= 12 and año_vacuna == 2020:
            if dia_vacuna > 24:
                print("Fecha de vacuna valida.")
                dia_vacuna=str(dia_vacuna)
                mes_vacuna=str(mes_vacuna)
                año_vacuna=str(año_vacuna)
                fecha_vacuna=dia_vacuna+"/"+mes_vacuna+"/"+año_vacuna
                rut_ciudadano.append(fecha_vacuna)
        else:
            print("Fecha de vacuna invalida.") 
        salir=int(input("Presione [1] para continuar\nPresione [2] para salir.\n "))
        if salir == 2:
            opcion = 4       
    else: 
        print("Rut no valido.")
    rut_ciudadano.append(vacuna_administrada)           
    print(ciudadanos, rut_ciudadano, fecha_vacuna, vacuna_administrada)
def buscar (busqueda_rut):
    for i in range(len(ciudadanos)):
        for x in range(4):    
            if busqueda_rut == ciudadanos[i][x]:
                print(ciudadanos[i])    
def imprimir(imprimir_vacuna):
    for i in range(len(ciudadanos)):
        for x in range(4):    
            if imprimir_vacuna == ciudadanos[i][x]:
                print("CERTIFICADO DE VACUNACION")
                print("-------------------------")
                for a in ciudadanos[i]:
                    print(a)
                print("---------------------------")
      
while opcion >= 1 and opcion <= 3:
    try:
        if opcion == 1:
            print("Grabar")
            rut_ciudadano=int(input("Ingrese el rut del ciudadano sin puntos y sin digito verificador\n"))
            Lote_vacuna=int(input("Ingrese el año del lote de la vacuna\n"))
            año_vacuna=int(input("Ingrese año de la vacunacion(YYYY).\n"))
            mes_vacuna=int(input("Ingrese mes de la vacunacion(MM).\n"))
            dia_vacuna=int(input("Ingrese dia de la vacunacion(DD).\n"))
            vacuna_administrada=str(input("Ingrese el nombre de la vacuna administrada\n"))
            grabar(rut_ciudadano, Lote_vacuna, año_vacuna, mes_vacuna, dia_vacuna, vacuna_administrada)
        elif opcion == 2:
            print("Buscar")
            busqueda_rut=str(input("Ingrese el rut que desea buscar con digito verificador.\n"))
            buscar(busqueda_rut)
        elif opcion == 3:
            print("Imprimir")
            imprimir_vacuna=str(input("Ingrese el RUT del ciudadano con digito verificador que desa imprimir\n"))
            imprimir(imprimir_vacuna)
        salir=int(input("Presione [1] para continuar\nPresione [2] para salir.\n "))
        if salir == 2 and len(ciudadanos) > 2:
            opcion = 4
        else:
            opcion=int(input("Presione [1] para grabar datos de un ciudadano.\nPresione [2] Para buscar datos de un ciudadano.\nPresione [3] para imprimir certificado de vacunacion.\nPresione [4] para salir.\n "))    
    except:
        print("ERROR de datos: Ingrese Nuevamente al programa")
print("Usted Salio del Programa ")                   
