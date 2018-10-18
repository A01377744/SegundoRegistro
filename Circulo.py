import math
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def transformarARadianes(angulo):
    radianes = (angulo / 180) * math.pi
    return radianes


def generarFigura(vertices):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        z = 360 // vertices
        radio = 200
        for angulo in range(0, 360, z):
            for newAngle in range(z, 360, z):
                radianes = transformarARadianes(angulo)
                newRadianes = transformarARadianes(newAngle)
                y = math.sin(radianes) * radio
                x = math.cos(radianes) * radio
                xnew = math.cos(newRadianes) * radio
                ynew = math.sin(newRadianes) * radio
                pygame.draw.line(ventana, NEGRO, (400+x, 400+y), (400+xnew, 400+ynew), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


def main():
    vertices = 2
    while vertices != -1:
        vertices = int(input("Numero de puntos"))
        generarFigura(vertices)


main()