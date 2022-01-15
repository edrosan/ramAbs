from diccionarios import colores
import random

def printRam(ram):
    print()
    procesoEnCola = ram[0] 
    n = random.randrange(1,5)   
    for element in ram:
        if(element == 0): print(colores['verde']+' '+str(element), end="") 
        elif (element == procesoEnCola): print(colores[''+str(n)], element, end="")
        else:
            n = random.randrange(1,5)   
            procesoEnCola = element 
            print (colores[''+str(n)], element, end="")
    print(colores['default'])

def printMapa(mapaBits):
    linea = ''
    print()
    for line in mapaBits:
        for element in line:
            if (element == 0): linea += colores['verde']+' 0 '+colores['default']
            elif(element == 1): linea += colores['rojo']+' 1 '+colores['default']
        print(linea)
        linea = '' 
    print()  

def printListaColor(listaLigada):
    print()
    for i in listaLigada:
        if(i[0]=='H'): print('[',colores['verde'],i[0],colores['default'],'|',i[1][0],'/',i[1][1],']->', end=' ')
        else: print('[',colores['rojo'],i[0],colores['default'],'|',i[1][0],'/',i[1][1],']->', end=' ')
    print('\n')
