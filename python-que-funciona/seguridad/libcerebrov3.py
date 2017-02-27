import gnupg
from pprint import pprint
class fichero(object):
    def __init__(self, a):
        self.r = a
    def crea(self, a):
        self.b = self.r + a
        archi=open(self.b,'w')
        archi.close()
        self.b = a
    def eli(a):
        pass
    def nueva(self, a):
        archi=open(self.b,'a')
        c = -1
        for b in a:
            c = c + 1
            archi.write('\n')
            archi.write(a[c])
            archi.write('\n')
        archi.close()
    def mues(self):
        a = self.b
        archi=open(self.b,'r')
        lineas=archi.readlines()
        for li in lineas:
            print li
        archi.close()
        return lineas
    def var_archivo(self, a):
        self.b = self.r + a
    def check(self, a):
        self.b = self.r + a
        try:
            fichero = open(self.b)
            fichero.close()
            return 0
        except:
            return 1
def input():
    a = raw_input()
    return a
def ouput(a):
    a = a + '\n'
    print(a)
class keys(object):
    def __init__(self, a):
        self.gpg = gnupg.GPG(gnupghome=a)
    def listkeys(self):
        public_keys = self.gpg.list_keys()
        private_keys = self.gpg.list_keys(True)
        print 'public keys:'
        pprint(public_keys)
        print 'private keys:'
        pprint(private_keys[1])
    def encrytar(self, a, b):
        unencrypted_string = a
        encrypted_data = self.gpg.encrypt(unencrypted_string, b)
        encrypted_string = str(encrypted_data)
        print 'ok: ', encrypted_data.ok
        print 'status: ', encrypted_data.status
        print 'stderr: ', encrypted_data.stderr
        print 'unencrypted_string: ', unencrypted_string
        print 'encrypted_string: ', encrypted_string
        return encrypted_string
    def descrytar(self, a, b, c):
        unencrypted_string = a
        encrypted_data = self.gpg.encrypt(unencrypted_string, b)
        encrypted_string = str(encrypted_data)
        decrypted_data = self.gpg.decrypt(encrypted_string, passphrase=c)
        print 'ok: ', decrypted_data.ok
        print 'status: ', decrypted_data.status
        print 'stderr: ', decrypted_data.stderr
        print 'decrypted string: ', decrypted_data.data
        return decrypted_data.data
