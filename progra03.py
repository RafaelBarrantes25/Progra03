print("Hola Eduardo")

import time as t
def repetir_infinito(palabra):
    """
    Esto repite una palabra indefinidamente
    E: Un texto
    S: Un texto infinito
    R: Texto tipo str
    """
    while len(palabra) > 0:
        print(palabra)
        t.sleep(0.5)

repetir_infinito("NWord")
