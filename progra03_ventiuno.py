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
    for carta in range(2):
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



def turno_jugador(lista_j,lista_p_j):
    """
    Le pide al jugador si quiere agarrar otra carta o no
    E: un input
    S: True o False
    R: la respuesta del jugador debe ser una opción válida
    """
    verificar = True
    while True:
        respuesta = input("¿Quiere agarrar otra carta?\n1. Sí\n2. No\n\n")
        
        if respuesta == "1":
            pass
        elif respuesta == "2":
            pass
        else:
            print("Esa no es una opción") 
        





def juego(lista_f=[],lista_p_f=[],lista_j=[],lista_p_j=[]):
    """
    Ejecuta el juego
    E: las listas de cartas de las distintas funciones
    S: el juego
    R: no deberían haber restricciones
    """
    if lista_j == []:
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
        
    #Estos prints son de prueba, hay que quitarlos después
    #-----------------------------------------------------------
    print(lista_j)
    print(lista_p_j)
    print(contar(lista_j))
    # -----------------------------------------------------------
    turno_jugador(lista_j,lista_p_j)
    
 



juego()