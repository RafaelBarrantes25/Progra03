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
       Perros: lista[0] hasta lista[5]. Liebre [lista[6],lista[7]]
    """
    matriz = []
    fila = []
    i = 0

    #Fila 0
    while i < 9:
        if i == 2 or i == 6:
            #Falta pulir
            """
            if([lista[0]] + [lista[1]] == [0, 1] or [lista[2]] + [lista[3]] == [0, 1] or
               [lista[4]] + [lista[5]] == [0, 1] or [lista[0]] + [lista[1]] == [0, 3] or
               [lista[2]] + [lista[3]] == [0, 3] or [lista[4]] + [lista[5]] == [0, 3]):
                   fila += ["🐶"]
                   i += 1
 
            elif [lista[6]] + [lista[7]] == [0, 1] or [lista[6]] + [lista[7]] == [0, 3]:
                fila += ["🐰"]
                i += 1
 
            else:
            """
            fila += ["🛑"]
            i += 1

        elif i == 3 or i == 5:
            fila += ["--"]
            i += 1

         elif i == 4:
            #Falta pulir
            """
            if(lista[0] + lista[1] == [0, 2] or lista[2] + lista[3] == [0, 2] or
               lista[4] + lista[5] == [0, 2]):
                   fila += ["🐶"]
                   i += 1
 
             elif lista[6] + lista[7] == [0, 2]:
                 fila += ["🐰"]
                 i += 1
 
             else:
             """
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
        if i == 0 or i == 4 or i == 8:
            fila += ["🛑"]
            i += 1

        elif i == 2 or i == 6:
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
        if i == 2 or i == 6:
            #Falta pulir
            """
            if([lista[0]] + [lista[1]] == [0, 1] or [lista[2]] + [lista[3]] == [0, 1] or
               [lista[4]] + [lista[5]] == [0, 1] or [lista[0]] + [lista[1]] == [0, 3] or
               [lista[2]] + [lista[3]] == [0, 3] or [lista[4]] + [lista[5]] == [0, 3]):
                   fila += ["🐶"]
                   i += 1

            elif [lista[6]] + [lista[7]] == [0, 1] or [lista[6]] + [lista[7]] == [0, 3]:
                fila += ["🐰"]
                i += 1

            else:
            """
            fila += ["🛑"]
            i += 1

        elif i == 3 or i == 5:
            fila += ["--"]
            i += 1

        elif i == 4:
            #Falta pulir
            """
            if(lista[0] + lista[1] == [0, 2] or lista[2] + lista[3] == [0, 2] or
               lista[4] + lista[5] == [0, 2]):
                   fila += ["🐶"]
                   i += 1

            elif lista[6] + lista[7] == [0, 2]:
                fila += ["🐰"]
                i += 1

            else:
            """
            fila += ["⬜"]
            i += 1

        else:
            fila += ["  "]
            i += 1

    matriz += fila
    tablero = ""
    i = 0

    while i < len(matriz):
        tablero += matriz[i]
        i += 1

    print(tablero)
    return matriz


##21 luego de la manifestación

def escoger_carta():
    """
    Esto ¿escoge una carta?
    E:
    S:
    R:
    """
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,10,11]

    elección_palos = palos[random.randint(0,3)]
    elección_números = números[random.randint(0,10)]

    return elección_números,elección_palos


def fascistas_cartas(lista):
    """
    Si, hace algo
    E: 
    S: 
    R: 
    """
    valor = 0
    valor_obtenido, palo_obtenido = escoger_carta()

    for número in range(len(lista)):
        valor += lista[número]

    if valor == 21:
        print("Tiene 21")

    else:
        if valor < 21:
            if valor_obtenido == 1:
                lista += [11]
                print(lista)

            else:
                lista += [valor_obtenido]
                print(lista)

        else:

            for número in range(len(lista)):
                if lista[número] == 11:
                    lista[número] = 1
                    print(lista)

    print(lista)
    return lista


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

leer("Hola, me llamo Ian y esto es una prueba para ver si la función leer funciona.\n\n")
tablero([0, 1, 1, 0, 2, 1, 1, 4])


##Juego

def anarquistas_contra_fascistas():
    """
    Esto corre el juego de anarquistas contra fascistas
    E: Ninguna
    S: La ejecución del juego
    R: Ninguna
    """
    #Lore()

def veintiuno(lista_fascistas):
    """
    Esto corre el juego de 21 luego de la manifestación
    E: Una lista
    S: La ejecución del juego
    R: La lista debe ser vacía
    """
    if lista_fascistas == []:
        lista = []

    else:
        lista = lista_fascistas

    lista_fascistas = fascistas_cartas(lista)

    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)

anarquistas_contra_fascistas()
veintiuno([])
