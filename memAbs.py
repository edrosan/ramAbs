from diccionarios import colores

def crearMapaBits(tamRam):
    mapaBits = []
    n = (tamRam // 8)
    for i in range(n): mapaBits.append([0] * 8)
    return mapaBits

def llenarMapa(ram, mapaBits):
    for i, proceso in enumerate(ram):
        if (proceso != 0): 
            fila = i // 8
            columna = i % 8
            mapaBits[fila][columna] = 1
        elif(proceso == 0): 
            fila = i // 8
            columna = i % 8
            mapaBits[fila][columna] = 0
    return mapaBits

def agregarLista(lista, espacio, inicio, final):
    return lista.append([espacio, [inicio, final]])

def crearListaLigada(ram):
    contProcesos = 0
    contHuecos = 0
    lista = []

    for indice in range(len(ram)): 
        if(ram[indice] == 0):#* encontro hueco
            if(contProcesos != 0): 
                posFinal = (contProcesos - 1) + posInicial
                lista.append(['P', [posInicial, posFinal]])
                contProcesos = 0
            if(contHuecos == 0): posInicial = indice
            contHuecos += 1
        elif(ram[indice] != 0):#* encuentra proceso
            if(contHuecos!=0): 
                posFinal = (contHuecos - 1) + posInicial
                lista.append(['H', [posInicial, posFinal]])
                contHuecos = 0
            if(contProcesos == 0): posInicial = indice
            contProcesos += 1

    #* Agrega al ultimo proceso en la RAM
    if(contHuecos!=0):
        posFinal = (contHuecos-1)+posInicial
        lista.append(['H', [posInicial, posFinal]])
    elif(contProcesos!=0):
        posFinal = (contProcesos-1)+posInicial
        lista.append(['P', [posInicial, posFinal]])
    return lista

def imprimirLista(listaLigada):
    for i in listaLigada:
        print('[',i[0],'|',i[1][0],'/',i[1][1],']->', end=' ')
    print()
