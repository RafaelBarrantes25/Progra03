##Imports

import random
import time


##Anarquistas contra fascistas: La lucha continua

def tablero(lista):
    """
    Esto crea e imprime el tablero
    E: Una lista
    S: Una matriz
    R: Lista tipo list (Son las posiciones de los perros y la liebre)
       Perros: lista[0] hasta lista[5]. Liebre: [lista[6],lista[7]].
    """
    matriz = []
    fila = []
    i = 0

    #Fila 0
    while i < 9:
        if i == 2:
            if [lista[0]] + [lista[1]] == [0, 1]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [0, 1]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [0, 1]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [0, 1]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 6:
            if [lista[0]] + [lista[1]] == [0, 3]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [0, 3]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [0, 3]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [0, 3]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 3 or i == 5:
            fila += ["--"]
            i += 1

        elif i == 4:
            if [lista[0]] + [lista[1]] == [0, 2]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [0, 2]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [0, 2]:
                fila += ["🌭"]
                i += 1

            elif lista[6] + lista[7] == [0, 2]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["⬜"]
                i += 1

        else:
            fila += ["  "]
            i += 1

    fila += ["\n"]
    matriz += fila
    fila = []
    i = 0

    #Fila 1
    while i < 9:
        if i == 0:
            fila += ["  "]
            i += 1

        elif i == 1 or i == 5:
            fila += ["⤢ "]
            i += 1

        elif i == 3 or i == 7:
            fila += [" ⤡"]
            i += 1

        elif i == 8:
            i += 1

        else:
            fila += [" ↕"]
            i += 1

    fila += ["\n"]
    matriz += fila
    fila = []
    i = 0


    #Fila 2
    while i < 9:
        if i == 0:
            if [lista[0]] + [lista[1]] == [1, 0]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [1, 0]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [1, 0]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [1, 0]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 4:
            if [lista[0]] + [lista[1]] == [1, 2]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [1, 2]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [1, 2]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [1, 2]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        if i == 8:
            if [lista[0]] + [lista[1]] == [1, 4]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [1, 4]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [1, 4]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [1, 4]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 2:

            if [lista[0]] + [lista[1]] == [1, 1]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [1, 1]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [1, 1]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [1, 1]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["⬜"]
                i += 1

        elif i == 6:
            if [lista[0]] + [lista[1]] == [1, 3]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [1, 3]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [1, 3]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [1, 3]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["⬜"]
                i += 1

        else:
            fila += ["--"]
            i += 1

    fila += ["\n"]
    matriz += fila
    fila = []
    i = 0

    #Fila 3
    while i < 9:
        if i == 0:
            fila += ["  "]
            i += 1
        elif i == 1 or i == 5:
            fila += ["⤡ "]
            i += 1

        elif i == 3 or i == 7:
            fila += [" ⤢"]
            i += 1

        elif i == 8:
            i += 1

        else:
            fila += [" ↕"]
            i += 1

    fila += ["\n"]
    matriz += fila
    fila = []
    i = 0


    #Fila 4
    while i < 9:
        if i == 2:
            if [lista[0]] + [lista[1]] == [2, 1]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [2, 1]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [2, 1]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [2, 1]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 6:
            if [lista[0]] + [lista[1]] == [2, 3]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [2, 3]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [2, 3]:
                fila += ["🌭"]
                i += 1

            elif [lista[6]] + [lista[7]] == [2, 3]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["🛑"]
                i += 1

        elif i == 3 or i == 5:
            fila += ["--"]
            i += 1

        elif i == 4:
            if [lista[0]] + [lista[1]] == [2, 2]:
                fila += ["🐕"]
                i += 1

            elif [lista[2]] + [lista[3]] == [2, 2]:
                fila += ["🐩"]
                i += 1

            elif [lista[4]] + [lista[5]] == [2, 2]:
                fila += ["🌭"]
                i += 1

            elif lista[6] + lista[7] == [2, 2]:
                fila += ["🐰"]
                i += 1

            else:
                fila += ["⬜"]
                i += 1

        else:
            fila += ["  "]
            i += 1

    fila += ["\n"]
    matriz += fila
    tablero = ""
    i = 0

    while i < len(matriz):
        tablero += matriz[i]
        i += 1

    print(tablero)
    return matriz


def movimiento(lista):
    """
    Esto hace los movimientos de los anarquistas
    E: Una lista con todas las posiciones
    S: Una lista con todas las posiciones
    R: Lista tipo list. Los últimos dos elementos son la liebre, los primeros 6 los perros
    """
    mover = input("¿A cuál de tus compañeros vas a mover?\n" +
                  "1. 🐕\n2. 🐩\n3. 🌭\n")


##Funciones auxiliares

def leer(texto):
    """
    Esto hace que un texto vaya apareciendo poco a poco en pantalla
    E: Un texto
    S: Un texto
    R: Texto tipo str
    """
    for letras in texto:
        print(letras,end="",flush=True)
        time.sleep(0.025)


##Pruebas


##Juego

def anarquistas_contra_fascistas():
    """
    Esto corre el juego de anarquistas contra fascistas
    E: Ninguna
    S: La ejecución del juego
    R: Ninguna
    """
    #Lore()

    posiciones = [0, 1, 1, 0, 2, 1, 1, 4]

    tablero(posiciones)

    seguir = ""

    while seguir != "N" and seguir != "n":
        movimiento(posiciones)

        seguir = input("¿Seguir?\n") #Solo para pruebas


anarquistas_contra_fascistas()
