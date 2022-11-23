from principal import *
from configuracion import *
import random
import math

#en una variable nueva ingreso el random.choice para que me de al azar una palabra de la lista ingresada
def nuevaPalabra(listas):
    newpalabra=random.choice(listas)
    return newpalabra



def lectura(archivo, salida, largo):
    # leo todo el archivo por completo y cargo sus palabras en text1
    text1= archivo.readlines()
    # usando la funcion que hice antes le saco los '/n' a las palabras con el largo estipulado en los parametros y las agrego a salida
    for palabra in text1:

        if len(sacarEspacios(palabra))==largo:

            salida.append(sacarEspacios(palabra))


def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):

    # con el condicional reviso que ambas palabras sean iguales, si es así  va a dar return True
    if palabraCorrecta == palabra:
        return True
    # si no devuelve true hago que recorra cada elemento de la palabra
    else:
        for i in range(len(palabra)):
                # en este condicional va a agregar las letras correctas en el lugar en la lista correctas
            if palabra[i]==palabraCorrecta[i]:
                correctas.append(palabra[i])

                #en este condicional va a agregar las letras incorrectas en el lugar pero que estan en la palabra en la lista casi
            elif palabra[i] in palabraCorrecta:
                casi.append(palabra[i])

                #en este else agrega las letras que no estan en la palabra en la lista incorrectas
            else:
                incorrectas.append(palabra[i])

    #por ultimo devuelve un return False
    return False


# Esta funcion saca los '\n' de las palabras
def sacarEspacios(palabra):
    palabra_sin_espacio=''          #variable vacia para ingresar la palabra sin '\n'
    #recorro los elementos de la palabra y agrego cada elemento que no sea '\n' a la nueva variable
    for letra in palabra:
        if letra!='\n':
            palabra_sin_espacio= palabra_sin_espacio + letra
    # por ultimo devuelve la palabra sin '\n'
    return palabra_sin_espacio


# Esta funcion controla que el usuario no haya escrito una misma palabra otra vez y que la palabra
# dada, este en el lemario y tenga el mismo largo que la palabra correcta. Devuelve True o False
def controlDePalabra(palabra_Correcta,palabra_Usuario,palabras_Usadas,diccionario):

    #en este primer condicional me aseguro que el jugador no vuelva a ecribir la misma palabra que probó en otro inteto
    if palabra_Usuario  not in palabras_Usadas:

        #en este segundo condicional me aseguro que la palabra este en el lemario
        if palabra_Usuario in diccionario:

            # en este ultimo me aseguro que tengan el mismo largo
            if len(palabra_Usuario)==len(palabra_Correcta):
                return True
    return False