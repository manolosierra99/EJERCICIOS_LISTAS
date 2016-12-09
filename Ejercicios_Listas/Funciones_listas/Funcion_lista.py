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
    pregunta=input("Quieres meter mas elementos?") #Introduzca si o no#
    while pregunta=="Si" or pregunta=="si":
        elemento=input("Introduzca otro elemento:")
        lista.append(elemento)
        print(lista)
        pregunta=input("Quieres meter mas elementos?")
    return lista
''' 
A continuacion vamos a dividir la lista en pacientes, fase en la que se encuentra y temperaturas.
'''
def dividir_lista(lista):
    id_paciente=lista[0]
    return id_paciente
    print(id_paciente)
    fase=lista[1]
    return fase
    print(fase)
    temperaturas=lista[2:5]
    return temperaturas
    print(temperaturas)
if __name__=="__main__":
    lista=[]
    print(crear_lista(lista))
    print(dividir_lista(lista))