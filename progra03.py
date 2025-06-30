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


def movimiento_p(lista):
    """
    Esto hace los movimientos de los anarquistas
    E: Una lista con todas las posiciones
    S: Una lista con todas las posiciones
    R: Lista tipo list. Los últimos dos elementos son la liebre, los primeros 6 los perros
    """
    if lista == [0, 1]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Este\n2. Sur-Este\n3. Sur\n")

        if nueva_posición == '1':
            return [0, 2]
            
        elif nueva_posición == '2':
            return [1, 2]
            
        elif nueva_posición == '3':
            return [1, 1]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)

    elif lista == [0, 2]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Este\n2. Sur\n")
                               
        if nueva_posición == '1':
            return [0, 3]
            
        elif nueva_posición == '2':
            return [1, 2]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
            
        
    elif lista == [0, 3]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Sur-Este\n2. Sur\n")
                               
        if nueva_posición == '1':
            return [1, 4]
            
        elif nueva_posición == '2':
            return [1, 3]

        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [1, 0]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Nor-Este\n2. Este\n3. Sur-Este\n")
                               
        if nueva_posición == '1':
            return [0, 1]
            
        elif nueva_posición == '2':
            return [1, 1]
            
        elif nueva_posición == '3':
            return [2, 1]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [1, 1]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Este\n3. Sur\n")
                               
        if nueva_posición == '1':
            return [0, 1]
            
        elif nueva_posición == '2':
            return [1, 2]
            
        elif nueva_posición == '3':
            return [2, 1]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [1, 2]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Nor-Este\n3. Este\n" +
                               "4. Sur-Este\n5. Sur\n")

        if nueva_posición == '1':
            return [0, 2]
            
        elif nueva_posición == '2':
            return [0, 3]
            
        elif nueva_posición == '3':
            return [1, 3]
            
        elif nueva_posición == '4':
            return [2, 3]
            
        elif nueva_posición == '5':
            return [2, 2]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
    
    elif lista == [1, 3]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Este\n3. Sur\n")
                               
        if nueva_posición == '1':
            return [0, 3]
            
        elif nueva_posición == '2':
            return [1, 4]
            
        elif nueva_posición == '3':
            return [2, 3]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [1, 4]:
        return lista
        leer("Tu amigo no puede moverse desde ahí\n")
                               
        
    elif lista == [2, 1]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Nor-Este\n3. Este\n")
                               
        if nueva_posición == '1':
            return [1, 1]
            
        elif nueva_posición == '2':
            return [1, 2]
            
        elif nueva_posición == '3':
            return [2, 2]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [2, 2]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Este\n")
                               
        if nueva_posición == '1':
            return [1, 2]
            
        elif nueva_posición == '2':
            return [2, 3]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)
        
    elif lista == [2, 3]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Nor-Este\n")
                               
        if nueva_posición == '1':
            return [1, 3]
            
        elif nueva_posición == '2':
            return [1, 4]
            
        else:
            leer('Creo que esa no es una opción\n')
            movimiento_p(lista)


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

    mover = ''
    fin = 0

    while fin == 0:
        tablero(posiciones)
        
        posición1 = [posiciones[0], posiciones[1]]
        posición2 = [posiciones[2], posiciones[3]]
        posición3 = [posiciones[4], posiciones[5]]
        posición4 = [posiciones[6], posiciones[7]]

        while mover != 1 and mover != 2 and mover != 3:
            mover = input("¿A cuál de tus compañeros vas a mover?\n" +
                          "1. 🐕\n2. 🐩\n3. 🌭\n")

            if mover == '1':
                mover = 1
            
            elif mover == '2':
                mover = 2
            
            elif mover == '3':
                mover = 3
            
            else:
                leer('Responda bien con 1, 2 o 3.\nPor favor.\n\n')
    
        if mover == 1:
            movido = movimiento_p(posición1)

        elif mover == 2:
            movido = movimiento_p(posición2)
        
        elif mover == 3:
            movido = movimiento_p(posición3)
            
        if(movido == posición1 or movido == posición2
           or movido == posición3):
            leer('\nCreo que deberíamos intentar otro movimiento\n')
               
        elif movido == posición4:
            leer('\nNo, debemos acercarnos sigilosamente a él\n')
            
        else:
            if mover == 1:
                posición1 = movido
                
            elif mover == 2:
                posición2 = movido
                
            elif mover == 3:
                posición3 = movido
            
        posiciones = posición1 + posición2 + posición3 + posición4
        mover = ''


anarquistas_contra_fascistas()
