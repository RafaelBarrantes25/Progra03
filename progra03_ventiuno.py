import random
import time

def escoger_carta():
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,"J","Q","K"]
    
    elección_palos = palos[random.randint(0,3)]
    elección_números = números[random.randint(0,10)]

    return elección_números,elección_palos





def asignar_primeras(lista,lista_p):
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
                    
    return lista,lista_p


def convertir_as(lista):
    """
    Los as son 11 por defecto
    si la lista se pasa de 21, busca los as y los convierte en 1 hasta que tenga menos de 21
    """

    for valor in range(len(lista)-1):
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
    for valor in range(len(lista)):
        if type(lista[valor]) == str:
            contador += 10
        else:
            contador += lista[valor]
    return contador





def turno_jugador(lista_j,lista_p_j,número):
    """
    Le pide al jugador si quiere agarrar otra carta o no
    E: un input
    S: True o False
    R: la respuesta del jugador debe ser una opción válida
    """
    while True:
        respuesta = input("¿Quiere agarrar otra carta?\n1. Sí\n2. No\n\n")
        
        if respuesta == "1":
            asignar_primeras(lista_j,lista_p_j)
            if lista_j[número] == 11 or lista_j[número] == 1:
                print(
                f"La nueva carta del jugador es un as de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta
            else:
                print(
                f"La nueva carta del jugador es un {lista_j[número]} de {lista_p_j[número]}")
                return lista_j, lista_p_j, respuesta
        elif respuesta == "2":
            return lista_j, lista_p_j, respuesta
        else:
            print("Esa no es una opción") 
            

    

def cpu1(lista_f,lista_p_f):
    """
    Ejecuta el turno de la cpu 1
    - Agarra carta si tiene 18 o menos
    - 50/50 si tiene 19 o 20
    - No agarra si tiene 21 o más
    """
    valor = contar(lista_f)

    if valor <= 18:
        asignar_primeras(lista_f,lista_p_f)
        print("Los fascistas agarraron una carta.")
        return lista_f, lista_p_f, 1
    elif valor == 19 or valor == 20:
        aleatorio = random.randint(1,2)
        if aleatorio == 1:
            asignar_primeras(lista_f, lista_p_f)
            print("Los fascistas agarraron una carta.")
            return lista_f,lista_p_f, 1
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


def juego(lista_f=[],lista_p_f=[],lista_j=[],lista_p_j=[]):
    """
    Ejecuta el juego
    E: las listas de cartas de las distintas funciones
    S: el juego
    R: no deberían haber restricciones
    """

    número = 2 #Se usa para imprimir la última carta de la lista

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
    índice = random.randint(0,3)
    perfil = perfiles[índice]
    
    while True:
        
        lista_j,lista_p_j,respuesta = turno_jugador(lista_j,lista_p_j,número)
        lista_f,lista_p_f,respuesta_f = perfil(lista_f,lista_p_f)
        
        if respuesta == "1":
            número += 1
        
        if respuesta == "2" and respuesta_f == 2:
            break
    
    lista_j = convertir_as(lista_j)
    lista_f = convertir_as(lista_f)
    print(lista_j,lista_f,contar(lista_j),contar(lista_f))

    
 



juego()