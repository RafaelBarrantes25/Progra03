import random
import time

def escoger_carta():
    palos = ["picas","corazones","diamantes","tréboles"]
    números = [1,2,3,4,5,6,7,8,9,10,11]

    elección_palos = palos[random.randint(0,3)]
    elección_números = números[random.randint(0,10)]

    return elección_números,elección_palos


def fascistas_cartas(lista):
    
    valor = 0
    valor_obtenido, palo_obtenido = escoger_carta()


    for número in range(len(lista)):
        valor += lista[número]
    
    if valor == 21:
        print("Tiene 21")
    else:
        if valor < 21:
            if valor_obtenido == 1:
                lista += [11]
                print(lista)
            else:
                lista += [valor_obtenido]
                print(lista)
        else:

            for número in range(len(lista)):
                if lista[número] == 11:
                    lista[número] = 1
                    print(lista)
              
    


    print(lista)
    return lista
            
    
    

    

def juego(lista_fascistas):
    
    if lista_fascistas == []:
        lista = []
    else:
        lista = lista_fascistas
    lista_fascistas = fascistas_cartas(lista)

    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
    fascistas_cartas(lista_fascistas)
juego([])