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
def anadir_temperatura(temperaturas1):
    '''
    Esta funcion se utiliza para anadir una temperatura a la lista de temperaturas.
    '''
    elemento6=float(input("Introduce un valor nuevo de temperaturas:"))
    temperaturas1.append(elemento6)
    return temperaturas1
def flotante(temperaturafinal):
    '''
    Esta funcion se utiliza para cambiar las temperaturas a flotantes.
    '''
    temperaturafinal[0]=float(temperaturafinal[0])
    temperaturafinal[1]=float(temperaturafinal[1])
    temperaturafinal[2]=float(temperaturafinal[2])
    return temperaturafinal
def lista_temp2(temperaturafinalfloat):
    '''
    Esta funcion crea una lista de temperaturas para anadirla despues a las temperaturas.
    '''
    tmp=[]
    pregunta=input("Quiere crear una lista nueva de temperaturas para anadirla a la anterior?") #Introduzca si o no
    while pregunta=="Si" or pregunta=="si":
        elemento=float(input("Introduzca otro elemento:"))
        tmp.append(elemento)
        pregunta=input("Quieres meter mas elementos?")
    return tmp    
def temperaturas_finales(temperaturafinalfloat):
    '''
    Esta funcion anade la lista tmp a las temperaturas.
    '''
    temperaturafinalfloat.append(tmp)
    return temperaturafinalfloat
def contar_elementos(lastemperaturas):
    '''
    Esta funcion cuenta los elementos en temperaturas.
    '''
    l=len(tmp)+len(temperaturafinalfloat)
    bueno=l-1
    return bueno
def cadena_texto(lastemperaturas):
    '''
    Esta funcion pasa las temperaturas a cadena de texto.
    '''
    
if __name__=="__main__":
    lista=[]
    print(crear_lista(lista))
    id_paciente,fase,temperaturas1=dividir_lista(lista)
    temperaturafinal=anadir_temperatura(temperaturas1)
    temperaturafinalfloat=flotante(temperaturafinal)
    tmp=lista_temp2(temperaturafinalfloat)
    lastemperaturas=temperaturas_finales(temperaturafinalfloat)
    elementos_temperaturas=contar_elementos(temperaturafinalfloat)
    