import pygame
import math

ALTO = 800
ANCHO = 800

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)


r = 380
R = 60
l = .9

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
termina = False
while not termina:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            termina = True

    ventana.fill(BLANCO)
    k = r / R
    for angulo in range(1, 360 * 20):
        a = math.radians(angulo)
        x = int(R * (((1 - k) * math.cos(a)) + ((l * k) * math.cos(((1 - k) / k) * a))))
        y = int(R * (((1 - k) * math.sin(a)) - ((l * k) * math.sin(((1 - k) / k) * a))))
        pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)
    pygame.display.flip()
    reloj.tick(1)

pygame.quit()

