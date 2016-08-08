# -*- coding: utf-8 -*-
import os
from distutils.core import setup
import py2exe
a = raw_input('Ruta del prigrama a compilar: ')
setup(console=[a])