'''
Created on 30 nov. 2016

@author: Manuel
'''
def crear_lista(lista):
    objeto=input("Introduzca un elemento a la cadena:")
    lista.append(objeto)
    pregunta=input("Quieres meter mas elementos?")
    while pregunta=="Si" or pregunta=="si":
        elemento=input("Introduzca otro elemento:")
        lista.append(elemento)
        print(lista)
        pregunta=input("Quieres meter mas elementos?")
    return lista
if __name__=="__main__":
    lista=[]
    print(crear_lista(lista))