##Imports

import random
import time


##Funciones

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

    #for número in range(len(lista)): (Versión Rafael)
    for número in lista:
    #Versión Ian (Creo que gasta menos recursos, no me haga caso, ni siquiera sé si funciona)
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


##Juego

def juego(lista_fascistas):
    """
    Esto corre el juego
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

juego([])
