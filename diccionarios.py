menu = {
    '1' :   'Agregar proceso',
    '2' :   'Ejecutar proceso',
    '3' :   'Mostrar procesos',
    '4' :   'Salir'
}

menu2 = {
    '1' : 'Ejecutar un proceso por su PID',
    '2' : 'No hacer nada'
}

menu3 = {
    '1' : 'Mostrar solo RAM',
    '2' : 'Mostrar solo Mapa de bits',
    '3' : 'Mostrar solo Lista ligada',
    '4' : 'Mostrar todo'
}

colores = {
    '1'   : '\x1b[48;5;52m',
    '2'   : '\x1b[48;5;61m',
    '3'   : '\x1b[48;5;94m',
    '4'   : '\x1b[48;5;17m',
    '5'   : '\x1b[48;5;89m',
    'verde' : '\x1b[48;5;28m',
    'rojo'  : '\x1b[48;5;124m',
    'default'   : '\x1b[0m'
}

mensajeValidacion = {
    '1' : 'Tamaño valido, espacio en RAM disponible',
    '0' : 'Tamaño no valido, ingrese un tamaño mayor a 0',
    '-1' : 'Tamaño no valido, supera tamaño total de la RAM: ',
    '-2' : 'Memoria RAM llena',
    '-3' : 'No hay espacio suficiente en la RAM',
}