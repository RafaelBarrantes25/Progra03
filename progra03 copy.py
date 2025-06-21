import random
import time

def escoger_carta():
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,"J","Q","K",11]
    
    elección_palos = palos[random.randint(0,3)]
    elección_números = números[random.randint(0,10)]

    return elección_números,elección_palos


def asignar_primeras(lista,lista_p):
    
    valor = 0
    valor_obtenido, palo_obtenido = escoger_carta()

 
    if valor < 21:
        if valor_obtenido == 1:
            lista += [11]
            lista_p += [palo_obtenido]
        else:
            lista += [valor_obtenido]
            lista_p += [palo_obtenido]
    else:

        for número in range(len(lista)):
            if lista[número] == 11:
                lista[número] = 1
                    
    return lista,lista_p

def contar(lista):
    contador = 0
    for valor in range(len(lista)):
        if type(lista[valor]) == str:
            contador += 10
        else:
            contador += lista[valor]
    return contador

def juego(lista_f=[],lista_p_f=[],lista_j=[],lista_p_j=[]):
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
    
    if lista_j[1] == 11 or lista_j[1] == 1:
        print(
            f"La segunda carta del jugador es un as de {lista_p_j[1]}")
    else:   
        print(
            f"La segunda carta del jugador es un {lista_j[1]} de {lista_p_j[1]}")
    print(lista_j)
    print(lista_p_j)
    print(contar(lista_j))



juego()