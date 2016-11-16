import gnupg
from pprint import pprint
def listkeys():
    gpg = gnupg.GPG(gnupghome='/home/i2p/.gnupg')
    public_keys = gpg.list_keys()
    private_keys = gpg.list_keys(True)
    print 'public keys:'
    pprint(public_keys)
    print 'private keys:'
    pprint(private_keys)
    print 'resumen:'
    #falta hacer un buscador
listkeys()
def encrytar(a, b):
    gpg = gnupg.GPG(gnupghome='/home/i2p/.gnupg')
    unencrypted_string = a
    encrypted_data = gpg.encrypt(unencrypted_string, b)
    encrypted_string = str(encrypted_data)
    print 'ok: ', encrypted_data.ok
    print 'status: ', encrypted_data.status
    print 'stderr: ', encrypted_data.stderr
    print 'unencrypted_string: ', unencrypted_string
    print 'encrypted_string: ', encrypted_string
    return encrypted_string
a = encrytar('hola como estas', '1869B494884B2FAA')
print('pensar')
print(a)
def descrytar(a, b):
    gpg = gnupg.GPG(gnupghome='/home/i2p/.gnupg')
    unencrypted_string = a
    encrypted_data = gpg.encrypt(unencrypted_string, b)
    encrypted_string = str(encrypted_data)
    print(a, 'hola')
    a = raw_input('Pon tu contrasenya: ')
    decrypted_data = gpg.decrypt(encrypted_string, passphrase=a)
    print 'ok: ', decrypted_data.ok
    print 'status: ', decrypted_data.status
    print 'stderr: ', decrypted_data.stderr
    print 'decrypted string: ', decrypted_data.data
descrytar(a, '1869B494884B2FAA')