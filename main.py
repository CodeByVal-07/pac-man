import pygame
import json
import os
from mapa import crear_laberinto, crear_items, matriz_mapa
from pac_man import Jugador
from fantasmas import Fantasma

pygame.init()

TILE = 32
ARCHIVO_PUNTAJES = "puntajes.json"


def cargar_puntajes():
    if os.path.exists(ARCHIVO_PUNTAJES):
        try:
            with open(ARCHIVO_PUNTAJES, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def guardar_puntajes(datos):
    with open(ARCHIVO_PUNTAJES, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def registrar_intento(nombre):
    datos = cargar_puntajes()
    datos[nombre] = datos.get(nombre, 0) + 1
    guardar_puntajes(datos)
    return datos[nombre]


def tile_pos(col, fila, tam_sprite):
    """Centra un sprite dentro de la celda (col, fila)."""
    margen = (TILE - tam_sprite) // 2
    return col * TILE + margen, fila * TILE + margen


# Tamaño de la ventana según el mapa
filas = len(matriz_mapa)
cols = len(matriz_mapa[0])
ANCHO, ALTO = cols * TILE, filas * TILE

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 48)
fuente_chica = pygame.font.SysFont(None, 28)


def pedir_nombre():
    """Pantalla inicial donde se escribe el nombre del jugador."""
    nombre = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre.strip():
                    return nombre.strip()
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 15 and evento.unicode.isprintable():
                    nombre += evento.unicode
        pantalla.fill((0, 0, 0))
        t1 = fuente.render("Escribe tu nombre:", True, (255, 255, 0))
        t2 = fuente.render(nombre + "|", True, (255, 255, 255))
        t3 = fuente_chica.render("ENTER para comenzar", True, (200, 200, 200))
        pantalla.blit(t1, t1.get_rect(center=(ANCHO // 2, ALTO // 2 - 60)))
        pantalla.blit(t2, t2.get_rect(center=(ANCHO // 2, ALTO // 2)))
        pantalla.blit(t3, t3.get_rect(center=(ANCHO // 2, ALTO // 2 + 60)))
        pygame.display.flip()
        reloj.tick(60)


def nueva_partida():
    pacman = Jugador(*tile_pos(9, 14, 26))
    blinky = Fantasma(*tile_pos(8, 10, 24), (255, 0, 0))
    pinky = Fantasma(*tile_pos(10, 10, 24), (255, 182, 193))
    paredes = crear_laberinto()
    puntos, powerups = crear_items()
    fantasmas = pygame.sprite.Group(blinky, pinky)
    todos = pygame.sprite.Group()
    todos.add(paredes, puntos, powerups, pacman, blinky, pinky)
    return pacman, paredes, puntos, powerups, fantasmas, todos

nombre_jugador = pedir_nombre()
intentos = registrar_intento(nombre_jugador)
pacman, paredes, puntos, powerups, fantasmas, todos = nueva_partida()
game_over = False

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN and not game_over:
            if evento.key == pygame.K_LEFT:
                pacman.mover_izquierda()
            elif evento.key == pygame.K_RIGHT:
                pacman.mover_derecha()
            elif evento.key == pygame.K_UP:
                pacman.mover_arriba()
            elif evento.key == pygame.K_DOWN:
                pacman.mover_abajo()
        elif evento.type == pygame.KEYUP and not game_over:
            pacman.detener()
        elif evento.type == pygame.KEYDOWN and game_over and evento.key == pygame.K_r:
            intentos = registrar_intento(nombre_jugador)
            pacman, paredes, puntos, powerups, fantasmas, todos = nueva_partida()
            game_over = False

    if not game_over:
        pacman.update(paredes)
        for f in fantasmas:
            f.update(paredes)

        # Pac-Man come puntos / powerups
        pygame.sprite.spritecollide(pacman, puntos, True)
        pygame.sprite.spritecollide(pacman, powerups, True)

        # Los fantasmas matan a Pac-Man al tocarlo
        if pygame.sprite.spritecollideany(pacman, fantasmas):
            game_over = True

    pantalla.fill((0, 0, 0))
    todos.draw(pantalla)
    hud = fuente_chica.render(
        f"Jugador: {nombre_jugador}   Intentos: {intentos}", True, (255, 255, 255)
    )
    pantalla.blit(hud, (10, 5))
    if game_over:
        texto = fuente.render("GAME OVER - pulsa R", True, (255, 0, 0))
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto, rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
