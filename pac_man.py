import pygame

AMARILLO = (255, 255, 0)
TILE = 32
TAM_PACMAN = 26  # un poco más chico que el tile para caber en pasillos


class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([TAM_PACMAN, TAM_PACMAN])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.cambio_x = 0
        self.cambio_y = 0
        self.velocidad = 2

    def mover_izquierda(self):
        self.cambio_x = -self.velocidad
        self.cambio_y = 0

    def mover_derecha(self):
        self.cambio_x = self.velocidad
        self.cambio_y = 0

    def mover_arriba(self):
        self.cambio_y = -self.velocidad
        self.cambio_x = 0

    def mover_abajo(self):
        self.cambio_y = self.velocidad
        self.cambio_x = 0

    def detener(self):
        self.cambio_x = 0
        self.cambio_y = 0

    def update(self, paredes):
        # Eje X
        self.rect.x += self.cambio_x
        for pared in pygame.sprite.spritecollide(self, paredes, False):
            if self.cambio_x > 0:
                self.rect.right = pared.rect.left
            elif self.cambio_x < 0:
                self.rect.left = pared.rect.right

        # Eje Y
        self.rect.y += self.cambio_y
        for pared in pygame.sprite.spritecollide(self, paredes, False):
            if self.cambio_y > 0:
                self.rect.bottom = pared.rect.top
            elif self.cambio_y < 0:
                self.rect.top = pared.rect.bottom
