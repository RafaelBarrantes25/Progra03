import random
import time


def escoger_carta():
    palos = ["picas", "corazones", "diamantes", "tréboles"]
    números = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]

    elección_palos = palos[random.randint(0, 3)]
    elección_números = números[random.randint(0, 10)]

    return elección_números, elección_palos


def asignar_primeras(lista, lista_p):
    """
    Se usa para asignar las cartas iniciales al jugador y a los fascistas
    E: lista vacía
    S: la lista con 2 cartas iniciales
    R: no deberían haber
    """

    valor = 0
    valor_obtenido, palo_obtenido = escoger_carta()

    if valor < 21:
        if valor_obtenido == 1:
            lista += [11]
            lista_p += [palo_obtenido]
        else:
            lista += [valor_obtenido]
            lista_p += [palo_obtenido]

    return lista, lista_p


def convertir_as(lista):
    """
    Los as son 11 por defecto
    si la lista se pasa de 21, busca los as y los convierte en 1 hasta que tenga menos de 21
    """

    for valor in range(0, len(lista)-1):
        if lista[valor] == 11 and contar(lista) > 21:
            lista[valor] = 1

    return lista


def contar(lista):
    """
    Suma los valores de las cartas
    E: la lista de cartas
    S: la suma de todas las cartas
    R: no deberían haber
    """
    contador = 0
    for valor in range(0, len(lista)):
        if type(lista[valor]) == str:
            contador += 10
        else:
            contador += lista[valor]
    return contador


def turno_jugador(lista_j, lista_p_j, número):
    """
    Le pide al jugador si quiere agarrar otra carta o no
    E: un input
    S: True o False
    R: la respuesta del jugador debe ser una opción válida
    """
    while True:
        respuesta = input("¿Quiere agarrar otra carta?\n1. Sí\n2. No\n\n")

        if respuesta == "1":
            número += 1
            asignar_primeras(lista_j, lista_p_j)
            if lista_j[número] == 11 or lista_j[número] == 1:
                print(
                    f"La nueva carta del jugador es un as de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta, número
            else:
                print(
                    f"La nueva carta del jugador es un {lista_j[número]} de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta, número
        elif respuesta == "2":
            return lista_j, lista_p_j, respuesta, número
        else:
            print("Esa no es una opción")


def cpu1(lista_f, lista_p_f):
    """
    Ejecuta el turno de la cpu 1
    - Agarra carta si tiene 18 o menos
    - 50/50 si tiene 19 o 20
    - No agarra si tiene 21 o más
    """
    valor = contar(lista_f)

    if valor <= 18:
        asignar_primeras(lista_f, lista_p_f)
        print("Los fascistas agarraron una carta.")
        return lista_f, lista_p_f, 1
    elif valor == 19 or valor == 20:
        aleatorio = random.randint(1, 2)
        if aleatorio == 1:
            asignar_primeras(lista_f, lista_p_f)
            print("Los fascistas agarraron una carta.")
            return lista_f, lista_p_f, 1
        else:
            print("Los fascistas no agarraron otra carta.")
            return lista_f, lista_p_f, 2
    else:
        print("Los fascistas no agarraron otra carta")
        return lista_f, lista_p_f, 2


def cpu2(lista_f, lista_p_f):
    """
    Ejecuta el turno de la cpu 2
    - Agarra carta si tiene 15 o menos
    - No agarra si tiene 16 o más
    """
    valor = contar(lista_f)

    if valor <= 15:
        asignar_primeras(lista_f, lista_p_f)
        print("Los fascistas agarraron una carta.")
        return lista_f, lista_p_f, 1
    else:
        print("Los fascistas no agarraron otra carta")
        return lista_f, lista_p_f, 2


def cpu3(lista_f, lista_p_f):
    """
    Ejecuta el turno de la cpu 3
    - Agarra carta si tiene 15 o menos
    - 50/50 si tiene entre 16 y 19
    - No agarra si tiene 20 o 21
    """
    valor = contar(lista_f)

    if valor <= 15:
        asignar_primeras(lista_f, lista_p_f)
        print("Los fascistas agarraron una carta.")
        return lista_f, lista_p_f, 1
    elif valor >= 16 and valor <= 19:
        aleatorio = random.randint(1, 2)
        if aleatorio == 1:
            asignar_primeras(lista_f, lista_p_f)
            print("Los fascistas agarraron una carta.")
            return lista_f, lista_p_f, 1
        else:
            print("Los fascistas no agarraron otra carta.")
            return lista_f, lista_p_f, 2
    else:
        print("Los fascistas no agarraron otra carta")
        return lista_f, lista_p_f, 2


def cpu4(lista_f, lista_p_f):
    """
    Ejecuta el turno de la cpu 4
    No agarra cartas, se queda con las iniciales
    """
    print("Los fascistas no agarraron otra carta")
    return lista_f, lista_p_f, 2


def resultados(lista_j, lista_p_j, lista_f, lista_p_f, puntos_j, puntos_f):
    """
    Revisa si alguno ganó o perdió y devuelve los puntos
    1 punto: 21 suave, cualquier combinación
    1 punto: black jack, figura y as
    2 punto: 5 menores, 21 o menos con 5 cartas sin figuras
    3 puntos: 5 de rombos, si primera carta es 5 de rombos
    4 puntos: doble as, 2 as
    5 puntos: triple 7
    E: las listas de cartas
    S: los puntos y cuál ganó
    R: no deberían haber
    """

    victoria_j = 0  # Se usa para comprobar qué victoria tuvo
    victoria_f = 0

    puntos_j_n = 0  # Mete los puntos nuevos en una variable distinta
    puntos_f_n = 0  # antes de sumarlos para saber cuál ganó

    verificar_figuras = 0  # Para ver si cumple 5 menores

    if contar(lista_j) == 21:
        puntos_j_n, victoria_j = resultados_aux(lista_j, lista_p_j, puntos_j)

    if contar(lista_f) == 21:
        puntos_f_n, victoria_f = resultados_aux(lista_f, lista_p_f, puntos_f)

    if contar(lista_j) < 21:
        if len(lista_j) == 5:
            for carta in range(5):
                if type(lista_j[carta]) != str:
                    verificar_figuras += 1

        if verificar_figuras == 5:
            puntos_j_n = 2
            victoria_j = 2
        else:
            puntos_j_n = 1
            victoria_j = 1
    verificar_figuras = 0

    if contar(lista_f) < 21:
        if len(lista_f) == 5:
            for carta in range(5):
                if type(lista_f[carta]) != str:
                    verificar_figuras += 1

        if verificar_figuras == 5:
            puntos += 2
            victoria_f = 2
        else:
            puntos_f_n = 1
            victoria_j = 1

    if contar(lista_j) > 21:
        victoria_j = 0
    if contar(lista_f) > 21:
        victoria_f = 0

    puntos_f += puntos_f_n
    puntos_j += puntos_j_n

    return puntos_j, puntos_f, victoria_j, victoria_f


def resultados_aux(lista, lista_p, puntos):
    """
    Función auxiliar de resultados para que no quede gigante
    """
    aces = 0
    verificar_figuras = 0

    if lista[0:3] == [7, 7, 7]:
        puntos += 5
        return puntos, 6

    for carta in range(0, len(lista)-1):
        if lista[carta] == 1 or lista[carta] == 11:
            aces += 1

    if aces == 2:
        puntos += 4
        return puntos, 5

    if lista[0] == 5 and lista_p[0] == "diamantes":
        puntos += 3
        return puntos, 4

    if len(lista) == 5:
        for carta in range(0, len(lista)):
            if type(lista[carta]) != str:
                verificar_figuras += 1

        if verificar_figuras == 5:
            puntos += 2
            return puntos, 2

    if len(lista) == 2:
        puntos += 1
        return puntos, 3

    puntos += 1
    return puntos, 8


def imprimir_finales(lista_j, lista_p_j, lista_f, lista_p_f):
    """
    Imprime la lista de cartas finales
    E: las listas de cartas
    S: las cartas finales
    R: no deberían haber
    """
    print()
    print("Las cartas del jugador son:")
    print()
    for carta in range(0, len(lista_j)):
        if lista_j[carta] == 1 or lista_j[carta] == 11:
            print(f"As de {lista_p_j[carta]}")
        else:
            print(f"{lista_j[carta]} de {lista_p_j[carta]}")

    print()
    print("Las cartas de los fascistas son:")
    print()
    for carta in range(0, len(lista_f)):
        if lista_f[carta] == 1 or lista_f[carta] == 11:
            print(f"As de {lista_p_f[carta]}")
        else:
            print(f"{lista_f[carta]} de {lista_p_f[carta]}")


def mensaje_victoria(victoria_j, victoria_f, puntos_j, puntos_f):
    """
    Imprime el mensaje de victoria y muestra los puntos
    E: victoria de cada uno y los puntos
    S: mensaje de victoria y puntos
    R: no
    """

    if victoria_j == 0:
        print("El jugador se pasó de 21, no gana puntos.")
    elif victoria_j == 1:
        puntos_j -= 1
        print("El jugador tuvo menos de 21, no gana puntos.")
    elif victoria_j == 2:
        print("El jugador ganó con 5 o más cartas sin figuras. Gana 2 puntos.")
    elif victoria_j == 3:
        print("El jugador ganó con Black Jack. Gana 1 punto.")
    elif victoria_j == 4:
        print("El jugador ganó con un 5 de rombos como primera carta. Gana 3 puntos.")
    elif victoria_j == 5:
        print("El jugador ganó con Doble As. Gana 4 puntos.")
    elif victoria_j == 6:
        print("El jugador ganó con triple 7. Gana 5 puntos.")
    elif victoria_j == 8:
        print("El jugador ganó con 21 sin ningún bonus. Gana 1 punto.")
    else:
        print("Error01")

    print()

    if victoria_f == 0:
        print("Los fascistas se pasaron de 21, no ganaron puntos.")
    elif victoria_f == 1:
        puntos_f -= 1
        print("Los fascistas tuvieron menos de 21, no ganan puntos.")
    elif victoria_f == 2:
        print("Los fascistas ganaron con 5 o más cartas sin figuras. Ganan 2 puntos.")
    elif victoria_f == 3:
        print("Los fascistas ganaron con Black Jack. Ganan 1 punto.")
    elif victoria_f == 4:
        print(
            "Los fascistas ganaron con un 5 de rombos como primera carta. Ganan 3 puntos.")
    elif victoria_f == 5:
        print("Los fascistas ganaron con Doble As. Ganan 4 puntos.")
    elif victoria_f == 6:
        print("Los fascistas ganaron con triple 7. Ganan 5 puntos.")
    elif victoria_f == 8:
        print("Los fascistas ganaron con 21 sin ningún bonus. Ganan 1 punto.")
    else:
        print("Error02")

    print()

    print("Puntos anarquistas   |   Puntos fascistas")
    print(f"     {puntos_j}                    {puntos_f} ")
    print()
    print()

    return puntos_f, puntos_j


def fin_del_juego(puntos_j, puntos_f):
    """
    Imprime el mensaje al terminar el juego
    E: los puntos de los dos jugadores
    S: el mensaje de fin del juegp
    R: no hay
    """
    if puntos_f > puntos_j:
        print(
            f"Los anarquistas ganaron con {puntos_j} puntos.\nLos fascistas perdieron con {puntos_f} puntos.")
    elif puntos_f == puntos_j:
        print(
            f"Ambos bandos tuvieron {puntos_j} puntos. Quedaron en un empate.")
    else:
        print(
            f"Los fascistas ganaron con {puntos_f} puntos.\nLos anarquistas perdieron con {puntos_j} puntos.")


def juego(lista_f=[], lista_p_f=[], lista_j=[], lista_p_j=[]):
    """
    Ejecuta el juego
    E: las listas de cartas de las distintas funciones
    S: el juego
    R: no deberían haber restricciones
    """
    puntos_f = 0
    puntos_j = 0

    jugar = True
    while jugar:
        número = 1  # Se usa para imprimir la última carta de la lista
        lista_j = []
        lista_f = []
        lista_p_f = []
        lista_p_j = []
        victoria_j = 0
        victoria_f = 0
        if lista_j == []:
            for carta in range(2):
                lista_j, lista_p_j = asignar_primeras(lista_j, lista_p_j)
                lista_f, lista_p_f = asignar_primeras(lista_f, lista_p_f)

        if lista_f[1] == 11 or lista_f[1] == 1:
            print(
                f"La segunda carta de los fascistas es un as de {lista_p_f[1]}")
        else:
            print(
                f"La segunda carta de los fascistas es un {lista_f[1]} de {lista_p_f[1]}")
        print()
        if lista_j[1] == 11 or lista_j[1] == 1:
            print(
                f"La segunda carta del jugador es un as de {lista_p_j[1]}")
        else:
            print(
                f"La segunda carta del jugador es un {lista_j[1]} de {lista_p_j[1]}")

        print()
        perfiles = [cpu1, cpu2, cpu3, cpu4]
        índice = random.randint(0, 3)
        perfil = perfiles[índice]

        while True:

            lista_j, lista_p_j, respuesta, número_n = turno_jugador(
                lista_j, lista_p_j, número)
            lista_f, lista_p_f, respuesta_f = perfil(lista_f, lista_p_f)

            if respuesta == "1":
                número = número_n
            if respuesta == "2" and respuesta_f == 2:
                break

        lista_j = convertir_as(lista_j)
        lista_f = convertir_as(lista_f)

        imprimir_finales(lista_j, lista_p_j, lista_f, lista_p_f)

        print()

        print(f"Las cartas del jugador suman {contar(lista_j)}")

        print()

        print(f"Las cartas de los fascistas suman {contar(lista_f)}")

        puntos_j, puntos_f, victoria_j, victoria_f = resultados(
            lista_j, lista_p_j, lista_f, lista_p_f, puntos_j, puntos_f)

        puntos_f, puntos_j = mensaje_victoria(
            victoria_j, victoria_f, puntos_j, puntos_f)

        
        loop = True
        while loop:
            volver_a_jugar = input("¿Quiere jugar de nuevo?\n1. Sí\n2. No\n")
            if volver_a_jugar == "1":
                loop = False
                break
            elif volver_a_jugar == "2":
                loop = False
                fin_del_juego(puntos_j, puntos_f)
                jugar = False
            else:
                print("Esa no es una opción.")


juego()
