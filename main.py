
import pygame
from mapa import crear_laberinto
from pac_man import Jugador
from fantasmas import Fantasma
from items import Punto

pygame.init()


TILE = 26
TAM_FANTASMA = 20
MARGEN = (TILE - TAM_FANTASMA) // 2

def tile_pos(col, fila):
    
    return col * TILE + MARGEN, fila * TILE + MARGEN



ANCHO, ALTO = 600, 630
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")
reloj = pygame.time.Clock()



pacman = Jugador(100, 100)



blinky = Fantasma(*tile_pos(9, 9),  (255, 0, 0))
pinky  = Fantasma(*tile_pos(10, 9), (255, 182, 193))


paredes = crear_laberinto()



todos = pygame.sprite.Group()
todos.add(pacman, blinky, pinky, )
todos.add(paredes)


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pacman.mover_izquierda()
            elif evento.key == pygame.K_RIGHT:
                pacman.mover_derecha()
            elif evento.key == pygame.K_UP:
                pacman.mover_arriba()
            elif evento.key == pygame.K_DOWN:
                pacman.mover_abajo()

        if evento.type == pygame.KEYUP:
            pacman.detener()

    
    pacman.update(paredes)
    blinky.update(paredes)
    pinky.update(paredes)
    

    
    pantalla.fill((0, 0, 0))
    todos.draw(pantalla)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
