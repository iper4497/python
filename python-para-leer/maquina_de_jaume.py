def main():
	alpha = ['a','b','c','d','e','f',
     'g','h','i','j','k','l',
     'm','n','o','p','q','r',
     's','t','u','v','w','x',
     'y','z']
	code = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '4D1', '4D2', '4D3', '4D4', '4D5', '4D6', '4D6', '50', '51','52', '53', '54', '55', '56', '57', '58', '59', '5D1']
	c = raw_input('Palabra a codificar: ')
	e = 0;
	for a in alpha:
    		e = e + 1
	print('Abacedari numero de lletres', e)
	for b in c:
    		for a in range(26):
        		if b == alpha[a]:
            			print(code[a])
	b = '*'
	for a in range(100):
    		b = b + '*'
	for a in range(2):
		print(b)
a = True
b = 'n'
c = 0
d = 0
while a:
	main()
	c = c + 1
	for d in range(c):
		print('*')
	b = raw_input('apagar s/n  ')
	if b == 's':
		a = False
