"""
 Ejemplo de Fractales usando recursividad

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


def dibujo_recursivo(x, y, largo, alto, cuenta):
    # Dibujamos el rectangulo
    # pygame.draw.rect(pantalla,NEGRO,[x,y,largo,alto],1)
    pygame.draw.line(pantalla,
                     NEGRO,
                     [x + largo*.25,alto//2+y],
                     [x + largo*.75,alto//2+y],
                     3)
    pygame.draw.line(pantalla,
                     NEGRO,
                     [x+largo*.25,(alto*.5)//2+y],
                     [x+largo*.25,(alto*1.5)//2+y],
                     3)
    pygame.draw.line(pantalla,
                     NEGRO,
                     [x + largo*.75,(alto*.5)//2+y],
                     [x + largo*.75,(alto*1.5)//2+y],
                     3)

    if cuenta > 0:
        cuenta -= 1
        # Arriba izquierda
        dibujo_recursivo(x, y, largo // 1, alto // 2, cuenta)
        # Arriba derecha
        dibujo_recursivo(x + largo // 1, y, largo // 2, alto // 2, cuenta)
        # Abajo izquierda
        dibujo_recursivo(x, y + largo // 2, largo // 2, alto // 2, cuenta)
        # Abajo derecha
        dibujo_recursivo(x + largo // 2, y + largo // 2, largo // 2, alto // 2, cuenta)


pygame.init()

# Establecemos el alto y largo de la pantalla
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("Mi Juego")

#Iteramos hasta que el usuario haga click sobre el boton de cerrar
hecho = False

# Usado para gestionar cuan rapido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa  -----------
while not hecho:
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle


    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(BLANCO)

    # TODO EL CoDIGO DE DIBUJO DEBERiA IR DEBAJO DE ESTE COMENTARIO
    nivel_fractal = 3
    dibujo_recursivo(10, 0, 700, 700, nivel_fractal)
    # TTODO EL CoDIGO DE DIBUJO DEBERiA IR DEBAJO DE ESTE COMENTARIO

    # # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limitamos a 20 fotogramas por segundo
    reloj.tick(5)

# Portate bien con el IDLE. Si nos olvidamos de esta linea, el programa se 'colgara'
# en la salida.
pygame.quit()