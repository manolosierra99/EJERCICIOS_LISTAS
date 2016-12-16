'''
Created on 30 nov. 2016

@author: Manuel
'''
def crear_lista(lista):
    '''
    Funcion para crear una lista con 5 variables a partir de una lista vacia que utilizaremos posteriormente.
    Por favor, introduzca solo 5 variables porque sino lo demas no funciona.
    '''
    objeto=input("Introduzca un elemento a la cadena:")
    lista.append(objeto)
    pregunta=input("Quieres meter mas elementos?") #Introduzca si o no
    while pregunta=="Si" or pregunta=="si":
        elemento=input("Introduzca otro elemento:")
        lista.append(elemento)
        print(lista)
        pregunta=input("Quieres meter mas elementos?")
    return lista
def dividir_lista(lista):
    ''' 
    A continuacion vamos a dividir la lista en pacientes, fase en la que se encuentra y temperaturas.
    '''
    id_paciente=lista[0]
    fase=lista[1]
    temperaturas=lista[2:]
    return id_paciente,fase,temperaturas
def anadir_temperatura(temperaturas):
    '''
    Esta funcion se utiliza para anadir una temperatura a la lista de temperaturas.
    '''
    elemento6=float(input("Introduce un valor nuevo de temperaturas:"))
    temperaturas.append(elemento6)
    return temperaturas
def flotante(temperaturas):
    '''
    Esta funcion se utiliza para cambiar las temperaturas a flotante.
    '''
    
if __name__=="__main__":
    lista=[]
    print(crear_lista(lista))
    id_paciente,fase,temperaturas=dividir_lista(lista)
    temperaturafinal=anadir_temperatura(lista)
        