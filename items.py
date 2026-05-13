import pygame

BLANCO = (255, 255, 255)

class Punto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
       
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
      
        self.rect.center = (x + 16, y + 16)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface([12, 12])
        self.image.fill(BLANCO)
       
        self.rect = self.image.get_rect()
        self.rect.center = (x + 16, y + 16)