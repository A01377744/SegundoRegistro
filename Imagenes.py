import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


def dibujarFondo(ventana, imgFondo):
    ventana.blit(imgFondo, (0, 0))


def dibujarCuadricula(ventana, imgPusheen):
    for renglon in range(8):        #Para cada renglón genera 11 columnas
        for columna in range(11):
            if renglon > 1 and columna >= 7 and columna <= 8:
                pass
            else:
                ventana.blit(imgPusheen, (columna*50, renglon*50))


def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #Imagenes
    imgFondo = pygame.image.load("9f370d61c65fbe3d0552faa4b783f387.jpg")
    imgPusheen = pygame.image.load("N90giK9n_400x400.jpg")

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarFondo(ventana, imgFondo)
        dibujarCuadricula(ventana, imgPusheen)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()

dibujar()
