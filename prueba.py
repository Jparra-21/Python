clavija = 16
jugadores = int(input("Ingrese numeros de jugadores."))
i=1
while clavija != 1:
    while i < jugadores+1:
        print(f"jugador n: {i}")
        juego = int(input("saque un numero de clavijas."))
        if juego <= 3 and juego >= 1:
            clavija=clavija-juego
            i+=1
            print(f"Quedan {clavija} Clavijas")
            if clavija <= 1:
                jugadores=0
                if i <=3:
                    i=1
        else:
            print("Ingrese nuevamente las clavijas que quiere sacar.")
    if i > jugadores:
        i=1      
print(f"Jugador n° {i} perdio la partida. Quedan {clavija}")                

    