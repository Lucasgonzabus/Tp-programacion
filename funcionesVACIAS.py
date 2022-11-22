from principal import *
from configuracion import *
import random
import math


def nuevaPalabra(lista):
    # hago una variable y dentro uso random.choice(), tomando la lista como parametro asi me da una palabra al azar de la lista
    newpalabra=random.choice(lista)

    return newpalabra


# Esta funcion es para hacer mas breve la funcion de lectura lo que hace es sacar los '/n' de las palabras de una lista y las agrega a otra lista
def sacarEspacios(lista):
    nlista=[]
    # recorro las palabras de la lista
    for palabra in lista:

        npalabra=''
        #recorro las letras de la palabra y si son diferentes a '\n' entonces las agrega a npalabra
        for letra in palabra:

            if letra!='\n':

                npalabra=npalabra+letra
        #cuando termine de agregar las letras a la palabra va a agregarla a la lista nueva (nlista)
        nlista.append(npalabra)
    #devuelve nlista
    return nlista



def lectura(archivo, salida, largo):
    # leo todo el archivo por completo y cargo sus palabras en la lista (text1)
    text1= archivo.readlines()
    # usando la funcion que hice antes le saco los '/n' a las palabras de la lista
    text1= sacarEspacios(text1)
    # recorro las palabras de la lista, utilizando un condicional reviso si tienen el mismo largo que la variable largo y si es asi, las agrego a salida
    for palabra in text1:

        if len(palabra)==largo:

            salida.append(palabra)


def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):

        # con otro condicional averiguo si ambas palabras son iguals y si es asi que agregue a correctas todas las letras y de un True en el return
    if palabraCorrecta == palabra:

        for letras in palabra:

            correctas.append(letras)

        return True
        # si no es asi, hago que revise cada letra de la palabra y la agregue donde debe
    else:
        for i in range(len(palabra)):
                # en este condicional va a agregar las letras correctas en la lista correctas
            if palabra[i]==palabraCorrecta[i]:
                correctas.append(palabra[i])

                #en este condicional va a agregar las letras incorrectas en el lugar pero que estan en la palabra en la lista casi
            elif palabra[i] in palabraCorrecta:
                casi.append(palabra[i])

                #en este directamente agrega las letras que no estan en la palabra en incorrectas
            else:
                incorrectas.append(palabra[i])

    #por ultimo devuelve un return False si la palabra no era correcta
    return False

def controlPalabra(palabraC,palabraU,palabrasU,largo,diccionario):
    if palabraU  not in palabrasU:
        if palabraU in diccionario:
            if len(palabraC)==len(palabraU):
                return True
    return False

