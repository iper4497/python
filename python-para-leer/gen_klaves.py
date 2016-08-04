a = ['a','b','c','d','e','f',
     'g','h','i','j','k','l',
     'm','n','o','p','q','r',
     's','t','u','v','w','x',
     'y','z']
n = "Son los caracteres"
#calculo = 27 ^ n
c = 0
R = range(719)
for s in range(2):
	for d in a:
		c = c + 1
		for b in a:
			c = c + 1 
			#Ya esta aun mas facil
			R[c] = d,b
			print(R)
			print("Conguiendo a R")
	a = R
	print("conguiendo a ", a)
	print("fin")
	R = range(719)
