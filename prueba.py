import time
def leer(texto):
    """
    Esto hace que un texto vaya apareciendo poco a poco en pantalla
    E: Un texto
    S: Un texto
    R: Texto tipo str
    """
    for letras in texto:
        print(letras, end="", flush=True)
        time.sleep(0.025)
hola = 4
leer(f"hola {hola}")
