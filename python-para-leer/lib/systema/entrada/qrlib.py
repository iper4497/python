# -*- coding: utf-8 -*-
#Este es un archvio para qr. 
import commands
def cam():
    a = commands.getoutput('zbarcam')
    return a