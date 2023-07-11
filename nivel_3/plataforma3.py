import pygame, sys
from animaciones3 import *
from personaje3 import *



FPS = 30
LARGO = 1000
ANCHO = 500
screen_size = (LARGO, ANCHO)
PANTALLA = pygame.display.set_mode((screen_size)) #pixeles


class Plataforma:
    def __init__(self, path_image, posicion_inicial: tuple, ancho, alto):
        self.imagen = path_image
        self.ancho = ancho
        self.alto = alto
        self.path_image = pygame.image.load(self.imagen)
        self.superficie_imagen = pygame.transform.scale(self.path_image, (self.ancho, self.alto))
        self.rectangulo = self.superficie_imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)


    def update(self, pantalla):
        pantalla.blit(self.superficie_imagen, self.rectangulo)









