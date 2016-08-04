# -*- coding: utf-8 -*-
import os
import command
class lector(object):
    def __init__(self, a):
        self.a = '/tmp/pdf'
        self.pal = command.system('pdftotext' + a + self.a)
    def archivo(self, a):
        os.system('espeak' + self.a + '-w ' + a)
    def escuchar(self):
        for a in self.pal:
            os.system('espeak' + a)
lector