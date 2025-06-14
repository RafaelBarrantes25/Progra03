import random
import time

def escoger_carta():
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    elección_palos = random.randint(0,3)
    elección_números = random.randint(0,12)

    print(f"Salió el {números[elección_números]} de {palos[elección_palos]}")

escoger_carta()