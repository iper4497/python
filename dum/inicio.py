# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 640
HEIGHT = 480
BLANCO = (238, 238, 238)

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# ---------------------------------------------------------------------
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DumDarac")
    background_image = load_image('/home/i2p/python2remote/dum/Mop8rfgp.png')
    screen.fill(BLANCO)
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (64, 0)) #Esto se tiene que centrar automaticamente
        pygame.display.flip()
    return 0
class main2():
    def __init__(self):
        main()

if __name__ == '__main__':
    pygame.init()
    main()