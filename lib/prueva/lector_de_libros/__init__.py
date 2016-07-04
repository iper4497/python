# -*- coding: utf-8 -*-
#Esto sera una prueva de la liberia para escuhar i mandarlos al medio configurado en un archvio
def configuracion():
    #para leer los archvivos de configuracion i retornar el valor como string
    #Index: a[1] archvio a soltar los audios
    a = 'config'    
    a = open(a, 'r')
    c = 0
    a.readline()
    for b in a.readline():
        c.append(b)
    return c 
a = configuracion()
print(a)
