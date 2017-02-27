import libcerebrov3
#a = libcerebrov3.keys('/home/i2p/.gnupg')
#a.encrytar('adios', '13897290384@inbox.im')
lista_llaves=['linux@linux', 'linux2@linux']
a = libcerebrov3.fichero('/home/i2p/python2remonte/basesdedatos/')
a.var_archivo('tex')
b = a.mues()
d = ''
for c in b:
	d = c + d
a = libcerebrov3.keys('/home/i2p/.gnupg')
for c in lista_llaves:
	d = a.encrytar(d, c)
