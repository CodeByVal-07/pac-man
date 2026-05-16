import pygame
import random

TILE = 32
TAM_FANTASMA = 24


class Fantasma(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((TAM_FANTASMA, TAM_FANTASMA))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.velocidad = 2
        self.direccion = random.choice(["izq", "der", "arr", "abj"])

    def _delta(self, direccion):
        if direccion == "izq":
            return -self.velocidad, 0
        if direccion == "der":
            return self.velocidad, 0
        if direccion == "arr":
            return 0, -self.velocidad
        if direccion == "abj":
            return 0, self.velocidad
        return 0, 0

    def update(self, paredes):
        dx, dy = self._delta(self.direccion)

        # Eje X
        self.rect.x += dx
        choque_x = pygame.sprite.spritecollide(self, paredes, False)
        for pared in choque_x:
            if dx > 0:
                self.rect.right = pared.rect.left
            elif dx < 0:
                self.rect.left = pared.rect.right

        # Eje Y
        self.rect.y += dy
        choque_y = pygame.sprite.spritecollide(self, paredes, False)
        for pared in choque_y:
            if dy > 0:
                self.rect.bottom = pared.rect.top
            elif dy < 0:
                self.rect.top = pared.rect.bottom

        # Si chocó, elige otra dirección al azar
        if choque_x or choque_y:
            self.direccion = random.choice(["izq", "der", "arr", "abj"])