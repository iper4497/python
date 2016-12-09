#!/usr/bin/python
#
# :: Invasion Tux
# :: Ultima modificacion : miercoles, 10 de diciembre de 2009
# :: Script realizado por makiolo (makiolo@gmail.com) (Licencia Creative Commons con reconocimiento)
# :: Ultima version : https://blogricardo.wordpress.com/2008/12/28/script-para-generar-diccionarios-de-fuerza-bruta/
# :: Dependencias : python 2.5
#

import sys, math, hashlib
from time import time, localtime, strftime
from hashlib import md5, sha1, sha224, sha256, sha384

########################### CONFIGURACION BASICA #########################

LONGITUD = 1
ALFABETO = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789_-."

####################################################################

########################### CONFIGURACION EXTRA ####################

CALCULAR_TIEMPO_RESTANTE = True

LLAMAR_EVENTO = False

GENERAR_FICHERO = True
DESTINO_FICHERO = "diccionario.txt"

BUSCAR_HASH = False
HASH_ALGORITMO = md5 # Opciones: md5, sha1, sha224, sha256, sha384
HASH_BUSCADO = "6091ece73d7b32b63e2f"

####################################################################

########################## CALLBACK ###############################

# ES UN CALLBACK MODIFICABLE SEGUN LA FUNCIONALIDAD A IMPLEMENTAR
def eventoPalabraGenerada(palabra):
  print palabra

####################################################################

########################## FUNCIONES ###############################

def getVariacionesConRepeticion(ALFABETO , LONGITUD):
  sumatorio = 0
  for i in range(LONGITUD):
    producto = 1
    for j in range(i+1):
      producto = producto * len(ALFABETO)
    sumatorio = sumatorio + producto
  return sumatorio

####################################################################

##################### VARS AUXILIARES ##############################

variacionesConRepeticion = getVariacionesConRepeticion(ALFABETO , LONGITUD)
PERIODO_MOSTRAR_ESTADISTICAS = 600000
inicioReloj = time()
cont = 0
progreso = 0

####################################################################

if GENERAR_FICHERO:
  f = open(DESTINO_FICHERO,"w")

LONGITUD_MAXIMA = LONGITUD
LONGITUD = 1
while LONGITUD <= LONGITUD_MAXIMA:
  try:
    contadores = []                                   # ponemos los contadores a 0
    for i in range(LONGITUD):
      contadores.append(0)

    fin = False
    while not fin:

      palabra=[]                                      # Creas una lista vacia (y liberas de paso)
      for i in range(LONGITUD):
        palabra.append(ALFABETO[contadores[i]])       # Vas metiendo al final letra a letra
      palabra_formada = "".join(palabra)

      if GENERAR_FICHERO:
        f.write("%s\n" % palabra_formada)

      if LLAMAR_EVENTO:
        eventoPalabraGenerada(palabra_formada)        # Envias a tu callback tada la lista unida

      if BUSCAR_HASH:
        # algorimos disponibles:
        HASH = HASH_ALGORITMO(palabra_formada).hexdigest()
        if HASH == HASH_BUSCADO:
          print "\n\nDesencriptado el HASH %s !!!!\n" % HASH
          print "Su valor desencriptado es \"%s\"\n\n" % palabra_formada
          raise KeyboardInterrupt

      if CALCULAR_TIEMPO_RESTANTE:
        if (cont % PERIODO_MOSTRAR_ESTADISTICAS == 0) and (cont != 0):
          try:
            progreso = cont*100.0 / variacionesConRepeticion              # porcentaje hasta ahora
            finReloj = time() - inicioReloj                               # finReloj es lo que esta tardando el calculo
            velocidad = cont / finReloj                                   # palabras procesadas por segundo
            estimado = finReloj * variacionesConRepeticion / cont         # es lo que se estima en realizar todo el proceso
            restante = estimado - finReloj                                # es lo que se estima en realizar lo restante
            if restante > 60:
              restante = restante / 60                                    # lo pasamos a minutos
              if restante > 60:
                restante = restante / 60                                 # lo pasamos a horas
                unidad = "horas"
              else:
                unidad = "mins"
            else:
              unidad = "segs"
            sys.stderr.write("%.2f%% - Quedan %.2f %s. La velocidad es de %.2f palabras/seg\n" % (progreso, restante, unidad, velocidad))
          except ZeroDivisionError:
            pass

      cont = cont + 1
      actual = LONGITUD - 1                                             # Pongo actual a la derecha del todo
      contadores[actual] = contadores[actual] + 1                       # Sumo 1 a las unidades

      while(contadores[actual] == len(ALFABETO)) and not fin:           # Propago el carry
        if(actual == 0):
          fin = True                                                    # FIN
        else:
          contadores[actual] = 0                                        # reinicia el actual contador
          actual = actual - 1                                           # avanza a la izquierda
          contadores[actual] = contadores[actual] + 1                   # y le sumo 1

    LONGITUD = LONGITUD + 1                                             # combinaciones para uno menos

  except KeyboardInterrupt:
    sys.stderr.write("Proceso interrumpido\n")
    fin = True                                                          # Fuerzo las condiciones de salida
    LONGITUD = LONGITUD_MAXIMA+1

if cont == variacionesConRepeticion:
  sys.stderr.write("Terminado al 100%\n")
else:
  if CALCULAR_TIEMPO_RESTANTE:
    sys.stderr.write("Terminado al %.2f%%\n" % progreso)
  sys.stderr.write("Realizadas %d combinaciones de %d\n" % (cont, variacionesConRepeticion))

if GENERAR_FICHERO:
  f.close()