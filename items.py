import pygame

TILE = 32
BLANCO = (255, 255, 255)


class Punto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect(center=(x + TILE // 2, y + TILE // 2))


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect(center=(x + TILE // 2, y + TILE // 2))
