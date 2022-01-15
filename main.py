from memAbs import (crearMapaBits, crearListaLigada, imprimirLista, llenarMapa)
from printMem import (printRam, printMapa, printListaColor)
from modRam import (buscarEspacio, addProceso, buscarProceso, subProceso)
from validaciones import(validacion)
from diccionarios import (menu, menu2, menu3, mensajeValidacion)

run = True
tamRam = 32
pid = 256

ram = [0] * tamRam
mapaBits = crearMapaBits(tamRam)
mapaBits = llenarMapa(ram, mapaBits)
listaLigada = crearListaLigada(ram)

print('\nTamaño de la RAM: '+ str(tamRam)+'B')
print(ram,'\n')
print(mapaBits,'\n')
print(listaLigada,'\n')

while(run):
    print('----------------------------------------')
    print ('\t\tMenu:')
    for key in menu: print ("\t", key, ":", menu[key])
    opcion = input('\t\t[ ]\033[2D')

    if(opcion   == '1'): 
        tamProceso = int(input('\t Ingrese tamaño del proceso: [   ]\033[4D'))
        respuesta = validacion(tamRam, tamProceso, listaLigada)
        print('\t',mensajeValidacion[str(respuesta)], end='')
        if(respuesta == 1):
            posInicial = buscarEspacio(listaLigada, tamProceso)
            ram, pid = addProceso(ram, pid, tamProceso, posInicial)
            mapaBits = llenarMapa(ram, mapaBits)
            listaLigada = crearListaLigada(ram)
            print('\n\t Se agrego el proceso: ', pid)
        elif(respuesta == -1):print(tamRam, 'B')
        elif(respuesta == -2 or respuesta == -3):
            print('\n\t¿Que desea realizar?')
            for key in menu2: print ("\t", key, ":", menu2[key])
            opcion = input('\t\t[ ]\033[2D')
            if(opcion == '1'):
                pidBuscar = int(input('\tIngrese PID a ejecutar: [   ]\033[4D'))
                if(buscarProceso(ram, pidBuscar)): 
                    ram = subProceso(ram, pidBuscar)
                    mapaBits = llenarMapa(ram, mapaBits)
                    listaLigada = crearListaLigada(ram)
                    print('\tProceso ejecutado: ', pidBuscar)
                else: print('\tProceso no encontrado')

    elif(opcion == '2'): 
        pidBuscar = int(input('\tIngrese PID a ejecutar: [   ]\033[4D'))
        if(buscarProceso(ram, pidBuscar)): 
            ram = subProceso(ram, pidBuscar)
            mapaBits = llenarMapa(ram, mapaBits)
            listaLigada = crearListaLigada(ram)
            print('\tProceso ejecutado: ', pidBuscar)
        else: print('\tProceso no encontrado')

    elif(opcion == '3'): 
            for key in menu3: print ("\t", key, ":", menu3[key])
            opcion = input('\t\t[ ]\033[2D')
            if(opcion == '1'): printRam(ram)
            if(opcion == '2'): printMapa(mapaBits)
            if(opcion == '3'): printListaColor(listaLigada)
            if(opcion == '4'):
                printRam(ram)
                printMapa(mapaBits)
                printListaColor(listaLigada)
    elif(opcion == '4'): run = False