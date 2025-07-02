##Imports

import random
import time


##Anarquistas contra fascistas: La lucha continua

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

    #Fila 0
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

    #Fila 1
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


    #Fila 2
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

    #Fila 3
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


    #Fila 4
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

    print("\nVista del dron:\n")
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
         "que traten de\ncapturarlo pacíficamente mientras tú los guías"
         + " con ayuda de un dron\nfuturista. Pero te advierto que " +
         "como buenos anarquistas\nno van a retroceder, literalmente.\n"
         )
         
    input("\n¿Estás listo?\n1. ¡Vamos!\n2. Si\n")
    
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
        return lista
        leer("Tu amigo no puede moverse desde ahí\n")
                               
        
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
             "[Falta agregar]\n")
    
    elif bando == 'fascista':
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
    
    

##Funciones auxiliares

def leer(texto):
    """
    Esto hace que un texto vaya apareciendo poco a poco en pantalla
    E: Un texto
    S: Un texto
    R: Texto tipo str
    """
    for letras in texto:
        print(letras,end="",flush=True)
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


##Pruebas


##Juego

def anarquistas_contra_fascistas():
    """
    Esto corre el juego de anarquistas contra fascistas
    E: Ninguna
    S: La ejecución del juego
    R: Ninguna
    """
    #lore()

    posiciones_válidas = [[0, 1], [0, 2], [0, 3],
                          [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                          [2, 1], [2, 2], [2, 3]]
                          
    octágonos = [[0, 1], [0, 3], [1, 0], [1, 2], [1, 4], [2, 1], [2, 3]]
                          
    cuadrados = [[0, 2], [1, 1], [1, 3], [2, 2]]
                            

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

        if(posición4[1] <= posición1[1] and posición4[1] <= posición2[1]
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

            
        """
        elif :
            fin = final('anarquista')
        """ 

        #Movimiento perros
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
            
            if(movido == posición1 or movido == posición2
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
                
        #Movimiento de la liebre
        libre = 0
            
        while libre != 1:
            if pertenece(posición4, octágonos) == True:
                movido = [posición4[0] + random.randint(-1, 1),
                          posición4[1] + random.randint(-1, 1)]
                
                          
            dirección = random.randint(0, 1)
            if(pertenece(posición4, cuadrados) == True and
               dirección == 0):
                movido = [posición4[0],
                          posición4[1] + random.randint(-1, 1)]
                          
            elif(pertenece(posición4, cuadrados) == True and
                 dirección == 1):
                movido = [posición4[0] + random.randint(-1, 1),
                          posición4[1]]
                
            if pertenece(movido, posiciones_válidas) != True:
                libre = 0
        
            elif(movido == posición1 or movido == posición2 or
                movido == posición3 or movido == posición4):
                libre = 0
                
            else:
                posición4 = movido
                libre = 1
                
        posiciones = posición1 + posición2 + posición3 + posición4


anarquistas_contra_fascistas()
