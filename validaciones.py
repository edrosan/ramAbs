def validacion(tamRam, tamProceso, listaLigada):
    if(tamProceso <= 0 ): return 0
    elif(tamProceso > tamRam): return -1
    elif(ramLlena(listaLigada)): return -2
    elif(comprobarEspacio(listaLigada, tamProceso)): return 1
    elif(not comprobarEspacio(listaLigada, tamProceso)): return -3

def ramLlena(lista):
    if (len(lista) == 1) and lista[0][0]=='P': return True
    else: return False

def comprobarEspacio(lista, tamProceso):
    for nodo in lista:
        if(nodo[0]=='H'):
            tamNodo = (nodo[1][1] - nodo[1][0]) + 1
            if(tamProceso <= tamNodo): return True
    return False
