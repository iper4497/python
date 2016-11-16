import gnupg
from pprint import pprint
import pygtk
import gtk
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
a = keys('/home/i2p/.gnupg')
a.encrytar('hola como estas', '1869B494884B2FAA')
a.listkeys()
class graf(object):
    def __init__(self):
        self.key = keys('/home/i2p/.gnupg')
        self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.ventana.connect("destroy", self.quit)
        self.boton = gtk.Button('encryptar')
        #self.boton.connect("clicked", self.key.encryptar('hola como estas', '1869B494884B2FAA'))
        self.boton.show()
    def main(self):
        gtk.main()
if __name__ == "__main__":
    s = graf()
    s.main()