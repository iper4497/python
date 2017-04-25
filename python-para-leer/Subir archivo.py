import os
import commands
import gnupg
from pprint import pprint
class keys(object):
#a = keys('/home/anon/.gnupg')
#a.encrytar('hola como estas', '1869B494884B2FAA')
#a.listkeys()
    def __init__(self, a):
        self.gpg = gnupg.GPG(gnupghome=a)
    def listkeys(self):
        public_keys = self.gpg.list_keys()
        private_keys = self.gpg.list_keys(True)
        print 'public keys:'
        pprint(public_keys)
        print 'private keys:'
        pprint(private_keys)
    def encrytar(self, a, b):
        unencrypted_string = a
        encrypted_data = self.gpg.encrypt(unencrypted_string, b)
        encrypted_string = str(encrypted_data)
        #print 'ok: ', encrypted_data.ok
        #print 'status: ', encrypted_data.status
        #print 'stderr: ', encrypted_data.stderr
        #print 'unencrypted_string: ', unencrypted_string
        #print 'encrypted_string: ', encrypted_string
        return encrypted_string
    def descrytar(self, b, c):
        encrypted_data = b
        encrypted_string = str(encrypted_data)
        decrypted_data = self.gpg.decrypt(encrypted_string, passphrase=c)
        print 'ok: ', decrypted_data.ok
        print 'status: ', decrypted_data.status
        print 'stderr: ', decrypted_data.stderr
        print 'decrypted string: ', decrypted_data.data
        return decrypted_data.data
def cam():
    while c == 'T':
        a = raw_input('Tienes la clave en algun archivo o la quieres sacar por camara a/c')
        if a == 'a':
            #sacar la clave del archivo
            c = 'F'#Terminar el bucle
            return d
        elif a == 'c':
            d = commands.getoutput('zbarcam')
            return d
        else:
            pass
class rcrypt(object):
    def __init__(self, a, c):
        self.c = c
        self.a = a
        self.b = keys('/home/anon/.gnupg')
    def simple(self, w):
        b = self.b.encrytar(self.a, self.c)
        for c in range(w):
            print(c)
            b = self.b.encrytar(b, self.c)
        print(c)
        return b
    def simpledesc(self, b, c):
        for c in range(20):
            print(c)
            b = self.b.descrytar(b, self.c, c)
        print(c)
        return b
    def doble(self, d, c):
        b = self.b.encrytar(self.a, self.c)
        for c in range(d):
            print(c, b)
            r = self.b.encrytar(b, self.c)
            b = self.b.encrytar(r, c)
def arch(a):
    a = open(a, 'r')
    b = a.read()
    return b
class comp(object):
    def __init__(self, a, b):
        self.a = a#archivo
        self.b = b#contrasenya
    def cifrar(self):
        a = '7z a -p'+ self.b + ' ' + self.a + '.7z ' + self.a
        print(a)
        os.system(a)
    def descifrar():
        a = '7z e ' + self.a + '.7z'
        os.system(a)
key = 'DAA25B50E39E5A2E'
ke = '3D500F1EC48DA47A'
print('7z a -p'+ 'hola' + ' '  + 'hola' + '.7z' + 'hola')
a = comp('/media/anon/el_pozo_negro/a_encryptar/clave', 'a')
a.cifrar()
infile = open('/media/anon/el_pozo_negro/a_encryptar/clave.7z', 'r')
v = 1
a = keys('/home/anon/.gnupg')
b = a.encrytar(infile.read(), key)
a.listkeys()
print b
print('askjdfhlaskd')
os.system('subirt ' + b)
c = raw_input('Introduce la contrasena: ')
a = keys('/home/anon/.gnupg')
a = a.descrytar(b, c)
#a = open()# Se convierte el archivo en una variable
#Se encrita en pgp segun la clave de pgp.
#a = cam()#Se vuelve a encritar en zip con la contrasena imperlarga dada por zbarcam
#Donde se copia al archivador.
#La configuracion se hara en un archivo donde se guardara todo para ello se usara la classe arch
#Mas una descompocion de la cadena donde se pondra todo
#Resumiendo habra dos archivos una para hacer log i las claves i otro para la configuracion del usuario
#Se ha de hacer una gui para el buen funcionamiento del mismo.
#Ademas cada vez que se suba un archivo se hara el correspondiente codigo qr.
#Mas poder usar las claves privadas con codigo qr directo txt i demas.
