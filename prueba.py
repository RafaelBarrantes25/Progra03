import random


def juego1():
    print("Juego 1")


def juego2():
    print("Juego 2")


def juego3():
    print("Juego 3")


def escoger_juego(n_veces):
    juegos = [juego1, juego2, juego3]
    indice = random.randint(0, len(juegos) - 1)
    juego = juegos[indice]
 
    for _ in range(n_veces):
        juego()

escoger_juego(3)