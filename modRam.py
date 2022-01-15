import random


def buscarEspacio(lista, tamProceso):
    for nodo in lista:
        if(nodo[0]=='H'):
            tamNodo = (nodo[1][1] - nodo[1][0]) + 1
            if(tamProceso <= tamNodo): 
                posInicial = nodo[1][0]
                return posInicial

def buscarProceso(ram, pid):
    for elemento in ram:
        if(elemento == pid): return True
    return False

def addProceso(ram, pid, tamProceso, posInicial):
    pid += 1
    for i in range(tamProceso):
        ram[posInicial] = pid
        posInicial += 1
    return ram, pid


def subProceso(ram, PID):
    for i, elemento in enumerate(ram):
        if(elemento == PID): ram[i] = 0
    return ram

def convertir(tamProceso):
    ascii = list(tamProceso.encode('ascii'))
    if(ascii[0] >= 48 and ascii[0] <= 59):
        return int(tamProceso)
    else:
        return tamProceso