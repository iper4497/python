import os
def esp(a):
    a = 'sleep ' + a
    os.system(a)
def calc(h, m):
    M = m * 60
    H = h * 3600
    print(H, M)
    S = H + M
    return(S)
h = input('cuantas horas a esperar   ')
m = input('Cuantos minuntos  ')
a = calc(h, m)
print(a)
esp(a)