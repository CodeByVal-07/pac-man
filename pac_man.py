import pygame
import random


AMARILLO=(255, 255, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
      
        self.image = pygame.Surface([45, 45])
        self.image.fill(AMARILLO) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.cambio_x = 0
        self.cambio_y = 0

    def mover_izquierda(self):
        self.cambio_x = -3
        self.cambio_y = 0

    def mover_derecha(self):
        self.cambio_x = 3
        self.cambio_y = 0

    def mover_arriba(self):
        self.cambio_y = -3
        self.cambio_x = 0

    def mover_abajo(self):
        self.cambio_y = 3
        self.cambio_x = 0

    def detener(self):
        self.cambio_x = 0
        self.cambio_y = 0   

    def update(self, paredes):
    
        self.rect.x += self.cambio_x
    
    
        lista_colisiones = pygame.sprite.spritecollide(self, paredes, False)
        for paredes in lista_colisiones:
            
            if self.cambio_x > 0: 
                self.rect.right = paredes.rect.left
            elif self.cambio_x < 0: 
                self.rect.left = paredes.rect.right

        self.rect.y += self.cambio_y
        
        
        lista_colisiones = pygame.sprite.spritecollide(self, paredes, False)
        for paredes in lista_colisiones:
            if self.cambio_y > 0: 
                self.rect.bottom = paredes.rect.top
            elif self.cambio_y < 0: 
                self.rect.top = paredes.rect.bottom


   
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()


pacman = Jugador(400, 300) 
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(pacman)


jugando = True
while jugando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

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



    pantalla.fill((0, 0, 0)) 
    todos_los_sprites.draw(pantalla) 
    
    pygame.display.flip() 
    reloj.tick(60)

pygame.quit()