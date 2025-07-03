
loop = True
while loop:
    volver_a_jugar = input("¿Quiere jugar de nuevo?\n1. Sí\n2. No\n")
    if volver_a_jugar == "1":
        loop = False
        break
    elif volver_a_jugar == "2":
        loop = False
        print("Hola")
        jugar = False
    else:
        print("Esa no es una opción.")

