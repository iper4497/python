def calc(P, D, C):
	R = (( P * C  * D ) / 100  ) - P
	print R
P = input('EL preu es : ')
C = input('Cantidad:  ')
D = input('Descompte:  ')
calc(P, C, D)
