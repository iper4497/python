import os
import commands
class comp(object):
    def __init__(self, a, b, c):
        self.a = a#archivo inicial
        self.b = b#contrasenya
        self.c = c#destino
    def cifrar(self):
        a = '7z a -p'+ self.b + ' ' + self.c + '.7z ' + self.a
        print(a)
        os.system(a)
    def descifrar():
        a = '7z e ' + self.a + '.7z'
        os.system(a)
b = commands.getoutput('date')
a = comp('/home/anon', 'qweriouqperiqpwriqeiqpriqperi', '/media/anon/el_pozo_negro/a_encryptar/backup/' + b )
a.cifrar()