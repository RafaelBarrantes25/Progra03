# Imports

import random
import time


# Anarquistas contra fascistas: La lucha continua

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

    # Fila 0
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

            elif [lista[6]] + [lista[7]] == [0, 2]:
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

    # Fila 1
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

    # Fila 2
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

    # Fila 3
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

    # Fila 4
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

            elif [lista[6]] + [lista[7]] == [2, 2]:
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

    leer("\nVista del dron:\n\n")
    print(tablero)
    return matriz


def lore():
    """
    Esto narra el lore del juego
    E: Ninguna
    S: Mucho texto
    R: Ninguna
    """
    leer("Hola de nuevo compañero anarquista, ya hace más de un mes que"
         + " vencimos\na los fascistas en nuestra carrera para decidir"
         + " las políticas de\nnuestro nuevo mundo. Aunque por " +
         "supuesto te llamamos porque tenemos una\nnueva misión.\n")

    input("\nPRESIONA ENTER PARA CONTINUAR\n")

    leer("Si bien la gran mayoría de los fascistas que vencimos" +
         " admitieron\nla derrota, recientemente de nuestra red de " +
         "información nos llegó\nla noticia de que un fascista radical"
         + " está perturbando la paz por\nla zona de San Ramón y " +
         "Palmares de Alajuela.\n")

    input("\nPRESIONA ENTER PARA CONTINUAR\n")

    leer("El plan es que enviaremos a Rafael, Ian y Eduardo allí para" +
         " que traten de\ncapturarlo pacíficamente mientras tú los " +
         "guías con ayuda de un dron\nfuturista. Pero te advierto que " +
         "como buenos anarquistas\nno van a retroceder, literalmente.\n"
         )

    input("\n¿Estás listo?\n1. ¡Vamos!\n2. Sí\n")

    leer("\nQue bueno\n\nEn tu pantalla saldrá el mapa del distrito " +
         "donde está el fascista junto\ncon su ubicación representada "
         + "por una liebre (🐰). Además de las ubicaciones\nde nuestros"
         + " compañeros representadas de la siguiente manera:\n" +
         "🐕: Rafael\n🐩: Ian\n🌭: Eduardo\n\nBuena suerte.\n")

    input("\nPRESIONA ENTER PARA CONTINUAR\n")


def movimiento_p(lista):
    """
    Esto hace los movimientos de los anarquistas
    E: Una lista
    S: Una lista
    R: Lista tipo list. La lista tiene la posición de uno de los perros
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
            return movimiento_p(lista)

    elif lista == [0, 2]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Este\n2. Sur\n")

        if nueva_posición == '1':
            return [0, 3]

        elif nueva_posición == '2':
            return [1, 2]

        else:
            leer('Creo que esa no es una opción\n')
            return movimiento_p(lista)

    elif lista == [0, 3]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Sur-Este\n2. Sur\n")

        if nueva_posición == '1':
            return [1, 4]

        elif nueva_posición == '2':
            return [1, 3]

        else:
            leer('Creo que esa no es una opción\n')
            return movimiento_p(lista)

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
            return movimiento_p(lista)

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
            return movimiento_p(lista)

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
            return movimiento_p(lista)

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
            return movimiento_p(lista)

    elif lista == [1, 4]:
        leer("\nTu amigo no puede moverse desde ahí\n")
        return lista

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
            return movimiento_p(lista)

    elif lista == [2, 2]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Este\n")

        if nueva_posición == '1':
            return [1, 2]

        elif nueva_posición == '2':
            return [2, 3]

        else:
            leer('Creo que esa no es una opción\n')
            return movimiento_p(lista)

    elif lista == [2, 3]:
        nueva_posición = input("\n¿A dónde quieres moverlo?\n" +
                               "1. Norte\n2. Nor-Este\n")

        if nueva_posición == '1':
            return [1, 3]

        elif nueva_posición == '2':
            return [1, 4]

        else:
            leer('Creo que esa no es una opción\n')
            return movimiento_p(lista)


def posibilidad(lista1, lista2, lista3, lista4):
    """
    Esto revisa si la liebre (lista 4) tiene posibilidades de \
    movimiento
    E: 4 listas
    S: True or False
    R: Listas tipo list de longitud 2
    """
    if (lista4 == [0, 2] and
       (lista1 == [0, 1] or lista1 == [1, 2] or lista1 == [0, 3]) and
       (lista2 == [0, 1] or lista2 == [1, 2] or lista2 == [0, 3]) and
       (lista3 == [0, 1] or lista3 == [1, 2] or lista3 == [0, 3])):
        return False

    elif (lista4 == [1, 4] and
          (lista1 == [0, 3] or lista1 == [1, 3] or lista1 == [2, 3]) and
          (lista2 == [0, 3] or lista2 == [1, 3] or lista2 == [2, 3]) and
          (lista3 == [0, 3] or lista3 == [1, 3] or lista3 == [2, 3])):
        return False

    elif (lista4 == [2, 2] and
          (lista1 == [2, 1] or lista1 == [1, 2] or lista1 == [2, 3]) and
          (lista2 == [2, 1] or lista2 == [1, 2] or lista2 == [2, 3]) and
          (lista3 == [2, 1] or lista3 == [1, 2] or lista3 == [2, 3])):
        return False

    else:
        return True


def final(bando):
    """
    Esto da el final del juego según quien haya ganado
    E: Un texto ('anarquista' o 'fascista')
    S: Un número
    R: Texto tipo str. Todo en minúsculas
    """
    if bando == 'anarquista':
        leer("\nFelicidades!\n" +
             "Hemos logrado capturar al fascista de manera pacífica\n" +
             "No creo que cause más problemas de aquí en adelante.\n" +
             "Tanto trabajo merece su recompensa.\n")

        jugar21 = ''
        while jugar21 == '':
            jugar21 = input("\n¿Te animas a unas partidas de 21?\n" +
                            "1. Si\n2. No\n")

            if jugar21 == '1':
                transición(1)
                jugar21 = 'S'

            elif jugar21 == '2':
                leer("\nBueno, la próxima será...\n" +
                     "La próxima será. Adiós.\n")
                jugar21 = 'N'

            else:
                leer("\nLa verdad no te entendí, ¿me lo repites?\n")

    elif bando == 'fascista':
        time.sleep(1)
        leer("\nLamentablemente el fascista se nos escapó, pero eso no" +
             " importa.\nUno de nuestros compañeros vio hacia donde" +
             " se fue.\nAún estamos a tiempo de seguirlo y atraparlo." +
             "\n¡NO DEBEMOS RENDIRNOS!\n\n")

        seguir = 'a'

        while seguir != '':
            seguir = input("¿Quieres intentarlo de nuevo?\n" +
                           "1. Si\n2. No\n")
            if seguir == '1':
                leer("\nBien, posicionemonos rápidamente e " +
                     "intentemos capturarlo de nuevo.\n")
                time.sleep(1)
                return 0

            elif seguir == '2':
                leer("\nOh...\nEntiendo... Supongo que tienes cosas" +
                     " que hacer.\nSi quieres volver a ayudarnos," +
                     " aquí estaremos en la lucha por el futuro.")
                return 1

            else:
                leer("\nLo siento, no entendí, ¿Si o no?\n\n")

    else:
        print('Error: Final no dado correctamente')


# Funciones auxiliares

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


def pertenece(lista1, lista2):
    """
    Esto dice si una lista está dentro de otra lista
    E: Dos listas
    S: True or False
    R: Ambas tipo list. lista2 es una lista de listas
    """
    if type(lista1) != list or type(lista2) != list:
        print('Error: No es list en pertenece')

    for listas in lista2:
        if type(listas) != list:
            print('Error: Elementos lista2 no son listas en pertenece')

        elif lista1 == listas:
            return True

    return False


# Juego

def anarquistas_contra_fascistas():
    """
    Esto corre el juego de anarquistas contra fascistas
    E: Ninguna
    S: La ejecución del juego
    R: Ninguna
    """
    lore()

    posiciones_válidas = [[0, 1], [0, 2], [0, 3],
                          [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                          [2, 1], [2, 2], [2, 3]]

    octágonos = [[0, 1], [0, 3], [1, 0], [1, 2], [1, 4], [2, 1], [2, 3]]

    cuadrados = [[0, 2], [1, 1], [1, 3], [2, 2]]

    capturada = 0

    posiciones = [0, 1, 1, 0, 2, 1, 1, 4]

    fin = 0

    while fin == 0:
        fin_perros = 0
        mover = ''
        posición1 = [posiciones[0], posiciones[1]]
        posición2 = [posiciones[2], posiciones[3]]
        posición3 = [posiciones[4], posiciones[5]]
        posición4 = [posiciones[6], posiciones[7]]

        tablero(posiciones)

        if (posición4[1] <= posición1[1] and posición4[1] <= posición2[1]
           and posición4[1] <= posición3[1]):
            fin = final('fascista')
            if fin == 0:
                posiciones = [0, 1, 1, 0, 2, 1, 1, 4]
                posición1 = [posiciones[0], posiciones[1]]
                posición2 = [posiciones[2], posiciones[3]]
                posición3 = [posiciones[4], posiciones[5]]
                posición4 = [posiciones[6], posiciones[7]]
                tablero(posiciones)

            elif fin == 1:
                fin_perros = 1
                transición(2)

        elif capturada == 1:
            fin = final('anarquista')
            fin_perros = 1

        # Movimiento perros
        while fin_perros != 1:
            while mover != 1 and mover != 2 and mover != 3:
                mover = input("¿A cuál de tus compañeros vas a mover?\n"
                              + "1. 🐕\n2. 🐩\n3. 🌭\n")

                if mover == '1':
                    mover = 1

                elif mover == '2':
                    mover = 2

                elif mover == '3':
                    mover = 3

                else:
                    leer('\nResponda bien con 1, 2 o 3.' +
                         '\nPor favor.\n\n')

            if mover == 1:
                movido = movimiento_p(posición1)

            elif mover == 2:
                movido = movimiento_p(posición2)

            elif mover == 3:
                movido = movimiento_p(posición3)

            if (movido == posición1 or movido == posición2
               or movido == posición3):
                leer('\nCreo que deberíamos intentar otro movimiento\n\n')
                mover = ''

            elif movido == posición4:
                leer('\nNo, debemos acercarnos sigilosamente a él\n')
                mover == ''

            else:
                if mover == 1:
                    posición1 = movido
                    fin_perros = 1

                elif mover == 2:
                    posición2 = movido
                    fin_perros = 1

                elif mover == 3:
                    posición3 = movido
                    fin_perros = 1

        # Movimiento de la liebre
        libre = 0

        while libre != 1:
            if pertenece(posición4, octágonos) == True:
                movido = [posición4[0] + random.randint(-1, 1),
                          posición4[1] + random.randint(-1, 1)]

            dirección = random.randint(0, 1)
            if (pertenece(posición4, cuadrados) == True and
               dirección == 0):
                movido = [posición4[0],
                          posición4[1] + random.randint(-1, 1)]

            elif (pertenece(posición4, cuadrados) == True and
                  dirección == 1):
                movido = [posición4[0] + random.randint(-1, 1),
                          posición4[1]]

            if pertenece(movido, posiciones_válidas) != True:
                libre = 0

            elif posibilidad(posición1, posición2,
                             posición3, movido) == False:
                capturada = 1
                posición4 = movido
                libre = 1

            elif (movido == posición1 or movido == posición2 or
                  movido == posición3 or movido == posición4):
                libre = 0

            else:
                posición4 = movido
                libre = 1

        posiciones = posición1 + posición2 + posición3 + posición4


# veintiuno ----------------------------------


def escoger_carta():
    palos = ["picas", "corazones", "diamantes", "tréboles"]
    números = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]

    elección_palos = palos[random.randint(0, 3)]
    elección_números = números[random.randint(0, 10)]

    return elección_números, elección_palos


def asignar_primeras(lista, lista_p):
    """
    Se usa para asignar las cartas iniciales al jugador y a los \
    rivales
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


def leer_2(texto):
    """
    Esto hace que un texto vaya apareciendo poco a poco en pantalla
    E: Un texto
    S: Un texto
    R: Texto tipo str
    """

    texto_nuevo = texto+"\n"
    for letras in texto_nuevo:
        print(letras, end="", flush=True)
        time.sleep(0.025)


def nombres():
    """
    Escoge el nombre del contrincante
    E: nada
    S: nombre y apellido en string
    R: nada
    """
    nombre = ["José", "María", "Carlos", "Ana", "Luis", "Sofía", "Juan", "Isabel", "Pedro", "Lucía",
              "Gabriel", "Carmen", "Fernando", "Laura", "Miguel", "Teresa", "Antonio", "Patricia", "Ricardo",
              "Elena", "Francisco", "Adriana", "Manuel", "Victoria", "David", "Marta", "Raúl", "Gloria",
              "Alberto", "Clara"]

    apellido = ["Chaves", "Pérez", "Jiménez", "González", "Rodríguez", "Vargas", "Monge", "Ramírez", "Alvarado", "Gómez",
                "Morales", "Rojas", "Araya", "Quirós", "Castro", "Sánchez", "Muñoz", "Bermúdez", "Salazar", "Moreno",
                "Ureña", "Cordero", "Soto", "Vargas", "Alfaro", "Vásquez", "Siles", "Herrera", "Cruz",
                "Benavides"]
    número_aleatorio = random.randint(0, len(nombre)-1)
    número_aleatorio_2 = random.randint(0, len(apellido)-1)
    n_final = nombre[número_aleatorio]
    a_final = apellido[número_aleatorio_2]
    return n_final, a_final


def convertir_as(lista):
    """
    Los as son 11 por defecto.
    Si la lista se pasa de 21, busca los as y los convierte en 1 hasta \
    que tenga menos de 21
    E: Una lista
    S: Una lista
    R: Lista tipo list
    """
    if type(lista) != list:
        print('Error: La lista no es lista en convertir_as(lista)')

    for valor in range(0, len(lista) - 1):
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

    """
    Yo lo haría así:
    for valor in lista:
        if type(valor) == str:
            contador += 10

        else:
            contador += lista[valor]
    """
    return contador


def turno_jugador(lista_j, lista_p_j, número):
    """
    Le pide al jugador si quiere agarrar otra carta o no
    E: un input
    S: True o False
    R: la respuesta del jugador debe ser una opción válida
    """
    while True:
        respuesta = input("¿Quiere agarrar otra carta?\n" +
                          "1. Sí\n2. No\n\n")

        if respuesta == "1":
            número += 1
            asignar_primeras(lista_j, lista_p_j)
            if lista_j[número] == 11 or lista_j[número] == 1:
                leer_2(
                    f"La nueva carta del jugador es un as de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta, número
            else:
                leer_2(
                    f"La nueva carta del jugador es un {lista_j[número]} de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta, número
        elif respuesta == "2":
            return lista_j, lista_p_j, respuesta, número
        else:
            leer_2("Esa no es una opción")


def cpu1(lista_f, lista_p_f, nombre):
    """
    Ejecuta el turno de la cpu 1
    - Agarra carta si tiene 18 o menos
    - 50/50 si tiene 19 o 20
    - No agarra si tiene 21 o más
    """
    valor = contar(lista_f)

    if valor <= 18:
        asignar_primeras(lista_f, lista_p_f)
        leer_2(f"{nombre} agarró una carta.")
        return lista_f, lista_p_f, 1

    elif valor == 19 or valor == 20:
        aleatorio = random.randint(1, 2)

        if aleatorio == 1:
            asignar_primeras(lista_f, lista_p_f)
            leer_2(f"{nombre} agarró una carta.")
            return lista_f, lista_p_f, 1

        else:
            leer_2(f"{nombre} no agarró otra carta.")
            return lista_f, lista_p_f, 2

    else:
        leer_2(f"{nombre} no agarró otra carta.")
        return lista_f, lista_p_f, 2


def cpu2(lista_f, lista_p_f,nombre):
    """
    Ejecuta el turno de la cpu 2
    - Agarra carta si tiene 15 o menos
    - No agarra si tiene 16 o más
    """
    valor = contar(lista_f)

    if valor <= 15:
        asignar_primeras(lista_f, lista_p_f)
        leer_2(f"{nombre} agarró una carta.")
        return lista_f, lista_p_f, 1

    else:
        leer_2(f"{nombre} no agarró otra carta.")
        return lista_f, lista_p_f, 2


def cpu3(lista_f, lista_p_f, nombre):
    """
    Ejecuta el turno de la cpu 3
    - Agarra carta si tiene 15 o menos
    - 50/50 si tiene entre 16 y 19
    - No agarra si tiene 20 o 21
    """
    valor = contar(lista_f)

    if valor <= 15:
        asignar_primeras(lista_f, lista_p_f)
        leer_2(f"{nombre} agarró una carta.")
        return lista_f, lista_p_f, 1

    elif valor >= 16 and valor <= 19:
        aleatorio = random.randint(1, 2)

        if aleatorio == 1:
            asignar_primeras(lista_f, lista_p_f)
            leer_2(f"{nombre} agarró una carta.")
            return lista_f, lista_p_f, 1

        else:
            leer_2(f"{nombre} no agarró otra carta.")
            return lista_f, lista_p_f, 2

    else:
        leer_2(f"{nombre} no agarró otra carta.")
        return lista_f, lista_p_f, 2


def cpu4(lista_f, lista_p_f, nombre):
    """
    Ejecuta el turno de la cpu 4
    No agarra cartas, se queda con las iniciales
    """
    leer_2(f"{nombre} no agarró otra carta.")
    return lista_f, lista_p_f, 2


def resultados(lista_j, lista_p_j, lista_f,
               lista_p_f, puntos_j, puntos_f):
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
        puntos_j_n, victoria_j = resultados_aux(lista_j, lista_p_j,
                                                puntos_j)

    if contar(lista_f) == 21:
        puntos_f_n, victoria_f = resultados_aux(lista_f, lista_p_f,
                                                puntos_f)

    if contar(lista_j) < 21:
        if len(lista_j) == 5:
            for carta in range(5):
                if type(lista_j[carta]) != str:
                    verificar_figuras += 1

        if verificar_figuras == 5:
            puntos_j_n = 2
            victoria_j = 2
        else:
            puntos_j_n = 0
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
            puntos_f_n = 0
            victoria_f = 1

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

    for carta in range(0, len(lista) - 1):
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


def imprimir_finales(lista_j, lista_p_j, lista_f, lista_p_f, nombre):
    """
    Imprime la lista de cartas finales
    E: las listas de cartas
    S: las cartas finales
    R: no deberían haber
    """
    leer_2("\nLas cartas del jugador son:\n")

    for carta in range(0, len(lista_j)):
        if lista_j[carta] == 1 or lista_j[carta] == 11:
            leer_2(f"As de {lista_p_j[carta]}")
        else:
            leer_2(f"{lista_j[carta]} de {lista_p_j[carta]}")

    leer_2(f"\nLas cartas de {nombre} son:\n")

    for carta in range(0, len(lista_f)):
        if lista_f[carta] == 1 or lista_f[carta] == 11:
            leer_2(f"As de {lista_p_f[carta]}")
        else:
            leer_2(f"{lista_f[carta]} de {lista_p_f[carta]}")


def mensaje_victoria(victoria_j, victoria_f, puntos_j, puntos_f, nombre):
    """
    Imprime el mensaje de victoria y muestra los puntos
    E: victoria de cada uno y los puntos
    S: mensaje de victoria y puntos
    R: no
    """

    if victoria_j == 0:
        leer_2("El jugador se pasó de 21, no gana puntos.")
    elif victoria_j == 1:
        leer_2("El jugador tuvo menos de 21, no gana puntos.")
    elif victoria_j == 2:
        leer_2("El jugador ganó con 5 o más cartas sin figuras. Gana 2 puntos.")
    elif victoria_j == 3:
        leer_2("El jugador ganó con Black Jack. Gana 1 punto.")
    elif victoria_j == 4:
        leer_2("El jugador ganó con un 5 de rombos como primera carta. Gana 3 puntos.")
    elif victoria_j == 5:
        leer_2("El jugador ganó con Doble As. Gana 4 puntos.")
    elif victoria_j == 6:
        leer_2("El jugador ganó con triple 7. Gana 5 puntos.")
    elif victoria_j == 8:
        leer_2("El jugador ganó con 21 sin ningún bonus. Gana 1 punto.")
    else:
        leer_2("Error01")

    print()

    if victoria_f == 0:
        leer_2(f"{nombre} se pasó de 21, no gana puntos.")

    elif victoria_f == 1:
        leer_2(f"{nombre} tuvo menos de 21, no gana puntos.")

    elif victoria_f == 2:
        leer_2(f"{nombre} ganó con 5 o más cartas sin figuras. " +
               "Gana 2 puntos.\n")

    elif victoria_f == 3:
        leer_2(f"{nombre} ganó con Black Jack. Gana 1 punto.")

    elif victoria_f == 4:
        leer_2(f"{nombre} ganó con un 5 de rombos como primera " +
               "carta. Gana 3 puntos.")

    elif victoria_f == 5:
        leer_2(f"{nombre} ganó con Doble As. Gana 4 puntos.")
    elif victoria_f == 6:
        leer_2(f"{nombre} ganó con triple 7. Gana 5 puntos.")
    elif victoria_f == 8:
        leer_2(f"{nombre} ganó con 21 sin ningún bonus. Gana 1 punto.")
    else:
        leer_2("Error02")

    leer_2(f"\nPuntos del jugador   |   Puntos de {nombre}")
    print()
    leer_2(f"         {puntos_j}                    {puntos_f} ")
    print("\n\n")

    return puntos_f, puntos_j


def fin_del_juego(puntos_j, puntos_f, nombre):
    """
    Imprime el mensaje al terminar el juego
    E: los puntos de los dos jugadores
    S: el mensaje de fin del juegp
    R: no hay
    """
    if puntos_f < puntos_j:
        leer_2(
            f"El jugador ganó con {puntos_j} puntos.\n{nombre} perdió con {puntos_f} puntos.")
    elif puntos_f == puntos_j:
        leer_2(
            f"Ambos jugadores tuvieron {puntos_j} puntos. Quedaron en un empate.")
    else:
        leer_2(
            f"{nombre} ganó con {puntos_f} puntos.\nEl jugador perdió con {puntos_j} puntos.")


def veintiuno(lista_f=[], lista_p_f=[], lista_j=[], lista_p_j=[]):
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
        nombre,apellido = nombres()
        leer_2(f"Su oponente será {nombre} {apellido}.\nSe repartieron las " +
               "primeras cartas boca abajo.\n")
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
            leer_2(
                f"La segunda carta de {nombre} es un as de {lista_p_f[1]}")
        else:
            leer_2(
                f"La segunda carta de {nombre} es un {lista_f[1]} de {lista_p_f[1]}")
        print()
        if lista_j[1] == 11 or lista_j[1] == 1:
            leer_2(
                f"La segunda carta del jugador es un as de {lista_p_j[1]}")
        else:
            leer_2(
                f"La segunda carta del jugador es un {lista_j[1]} de {lista_p_j[1]}")

        print()
        perfiles = [cpu1, cpu2, cpu3, cpu4]
        índice = random.randint(0, 3)
        perfil = perfiles[índice]

        while True:

            lista_j, lista_p_j, respuesta, número_n = turno_jugador(
                lista_j, lista_p_j, número)
            lista_f, lista_p_f, respuesta_f = perfil(lista_f, lista_p_f,nombre)

            if respuesta == "1":
                número = número_n
            if respuesta == "2" and respuesta_f == 2:
                break

        lista_j = convertir_as(lista_j)
        lista_f = convertir_as(lista_f)

        imprimir_finales(lista_j, lista_p_j, lista_f, lista_p_f)

        print()

        leer_2(f"Las cartas del jugador suman {contar(lista_j)}")

        print()

        leer_2(f"Las cartas de {nombre} suman {contar(lista_f)}")

        puntos_j, puntos_f, victoria_j, victoria_f = resultados(
            lista_j, lista_p_j, lista_f, lista_p_f, puntos_j, puntos_f)

        puntos_f, puntos_j = mensaje_victoria(
            victoria_j, victoria_f, puntos_j, puntos_f, nombre)

        loop = True
        while loop:
            volver_a_jugar = input("¿Quiere jugar de nuevo?\n1. Sí\n2. No\n")
            if volver_a_jugar == "1":
                loop = False
                break
            elif volver_a_jugar == "2":
                loop = False
                fin_del_juego(puntos_j, puntos_f, nombre)
                jugar = False
            else:
                leer_2("Esa no es una opción.")


def transición(número):
    """
    Esto hace la transición del primer juego al segundo
    E: Un número
    S: El 21
    R: Número 1 o 2
    """
    if número == 1:
        veintiuno()

    elif número == 2:
        time.sleep(1)
        leer("\n\nEspera...\n")
        time.sleep(1)
        leer("Oye...\n")
        time.sleep(1)
        leer("OYE...\n")
        time.sleep(1)
        leer("\n[Despiertas confundido]\n[Sientes que tuviste una" +
               " pesadilla]\n")

        input('\nPRESIONA ENTER PARA CONTINUAR\n')

        leer("\nAmigo, ¿todo bien?\n" +
               "Capturamos a un fascista en Alajuela y caiste muerto" +
               " por el cansansio\nEstábamos a punto de jugar unas " +
               "partidas de 21.\n")

        loop = True
        while loop:
            jugar21 = input("\n¿Te animas a jugar?\n1. Sí\n2. No\n")

            if jugar21 == '1':
                leer("\n\nGenial, por hoy tú serás la casa\n" +
                       "Aquí vamos\n")
                veintiuno()
                loop = False

            elif jugar21 == '2':
                leer('\nBueno, sigue durmiendo.\nAquí estaremos.')
                time.sleep(1)
                leer('\n\n[Vuelves a dormir]\n')
                time.sleep(1)
                leer('[Sientes que te perdiste de mucha diversión]\n')
                loop = False

            else:
                leer('\n\nOk pero, ¿vas a jugar o no?\n')


anarquistas_contra_fascistas()
