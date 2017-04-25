# -*- coding: utf-8 -*-
#Esto sera una prueva de la liberia para escuhar i mandarlos al medio configurado en un archvio
def configuracion():
    #para leer los archvivos de configuracion i retornar el valor como string
    #Index: a[1] archvio a soltar los audios
    a = open('config.py', 'r')
    c = 0
    a.read()
    for b in a.read():
        c.append(b)
    print(c)
a = configuracion()
print(a)