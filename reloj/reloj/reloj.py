# -*- coding: utf-8 -*-

import sys, time
import os
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *
def alarma():
    os.system('vlc /mnt/Despertador.mp4 &')
class reloj(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("reloj.ui",self)
        self.mostrarHora()
    def mostrarHora(self):
        self.ui.label.setText(time.strftime("%H:%M:%S"))
        QtCore.QTimer.singleShot(1000, self.mostrarHora)
        a = time.strftime("%H:%M:%S")
        b = '5:45:00'
        if a == b:
            alarma()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = reloj() #Es la variable de la hora a sonar
    myapp.show()
    sys.exit(app.exec_())
