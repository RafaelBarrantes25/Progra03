import random
import time

def escoger_carta():
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    elección_palos = random.randint(0,3)
    elección_números = random.randint(0,12)

    return elección_números


def fascistas_cartas():

    valor = 0
    turno = True
    while turno:
        time.sleep(2)
        if valor == 21:
            print("Consiguió 21")
            turno = False
        elif valor < 21:
            print("Agarra carta")
            valor += escoger_carta()
            print(valor)
        else:
            print("El valor se pasó de 21")
            turno = False
    print("Hola eduardo")

fascistas_cartas()