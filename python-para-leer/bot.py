#Este es para enviar el bot.
import os
class bot(object):

    def __init__(self, a, b):
        self.a = a #Usario
        self.b = b #password
    def enviar(self, a):
        os.system("curl -u" + self.b + ":"+ self.b +  "http://gnusocial.net/api/statuses/update.xml -d " + "status=" + a )
