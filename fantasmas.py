import pygame
import random


TILE = 26
TAM_FANTASMA = 20
MARGEN = (TILE - TAM_FANTASMA) // 2

OPUESTA = {
    "izq": "der",
    "der": "izq",
    "arr": "abj",
    "abj": "arr"
}

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
       
        self.image = pygame.Surface((TAM_FANTASMA, TAM_FANTASMA))
        self.image.fill(color)
        
        
        self.rect = self.image.get_rect(topleft=(x, y))
        
        
        self.velocidad = 1
        self.direccion = random.choice(["izq", "der", "arr", "abj"])

    def alineado_al_tile(self):
      
        return (
            self.rect.x % TILE == MARGEN and 
            self.rect.y % TILE == MARGEN
        )

    def direcciones_validas(self, paredes):
        
        opciones = []
        pruebas = {
            "izq": (-self.velocidad, 0),
            "der": (self.velocidad, 0),
            "arr": (0, -self.velocidad),
            "abj": (0, self.velocidad)
        }

        for dir_nombre, (dx, dy) in pruebas.items():
            
            self.rect.move_ip(dx, dy)
            if not pygame.sprite.spritecollideany(self, paredes):
                opciones.append(dir_nombre)
            
            self.rect.move_ip(-dx, -dy)
            
        return opciones

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

        
        dx, dy = 0, 0
        if self.direccion == "izq":
            dx = -self.velocidad
        elif self.direccion == "der":
            dx = self.velocidad
        elif self.direccion == "arr":
            dy = -self.velocidad
        elif self.direccion == "abj":
            dy = self.velocidad

      
        self.rect.x += dx
        self.rect.y += dy

        
        if pygame.sprite.spritecollideany(self, paredes):
            self.rect.x -= dx
            self.rect.y -= dy
            self.direccion = random.choice(["izq", "der", "arr", "abj"])