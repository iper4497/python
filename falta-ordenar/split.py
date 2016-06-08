#codigo fuente de split.
import string
import os
import sys

ruta = sys.argv[1] # Archivo a dividir
nombre_archivo = os.path.basename(ruta) # Obtener nombre real del archivo
tamano_trozo = sys.argv[2] # Tamaño de los trozos (Bytes xDDDD)
destino = sys.argv[3] # Destino de los Trozos
destino2 = destino
tamano_trozo = int(tamano_trozo) # Pasamos argumento de String a Integer
tamano = os.path.getsize(ruta) # Tamaño del Archivo (Bytes)
print "Tamaño: " + repr(tamano) + " Bytes\n\nParticionando Archivo, por favor espere..." # Imprimir Tamaño del Archivo (Bytes)
datos = '' # Datos del buffer
posicion = 0 # Para posicionarse en los datos a leer
i = 0 # Para Hacer .0, .1, .2, .3, .4, etc...
f = open (ruta, 'rb') # Abrimos archivo
while posicion <= tamano: # Creamos bucle que diga que si posicion menor o igual que tamaño hago lo que esta a continuación
    destino = destino + nombre_archivo + "." + repr(i) # Crear nombre del archivo prueba.jpg.0, prueba.jpg.1, prueba.jpg.*
    print "Creado: " + destino
    j = open (destino, 'wb') # Creamos el archivo prueba.jpg.*
    if i == 0: # Condicional para leer el bloque inicial
        datos = f.read(tamano_trozo) # Datos toma lo leido del buffer
        j.write(datos) # Escribimos en el archivo.
        j.close() # Cerramos archivo
        posicion = tamano_trozo # Metemos la posición siguiente en la integer
        i = i + 1 # Sumamos 1 a la variable integer
    else:
        f.seek (posicion) # Función que va al byte con el valor de posición
        datos = f.read(tamano_trozo) # Poner datos (X bytes de info.) en la variable desde esa posición
        j.write(datos) # Escribimos en archivo
        posicion = posicion + tamano_trozo # Vamos una posicion más avanzada
        j.close() # Cerramos archivo
        i = i + 1 # Sumamos 1 a la variable integer
    destino = destino2
f.close() # Cerramos archivo principal

x = open (destino2 + nombre_archivo + ".bat", 'w') # A partir de aquí creamos el .bat para pegar archivos
x.write('copy /b "'+ nombre_archivo + '.0" "' + nombre_archivo + '"\n')
z = 1
while z<i:
    x.write('copy /b "'+ nombre_archivo +'"+"'+ nombre_archivo +'.'+ repr(z)+ '"\n')
    z = z + 1
x.close()

# x = open ('pegador_linux', 'w') # Creamos el equivalente .bat para Linux es decir para Bash
# x.write('#!/bin/bash\n')