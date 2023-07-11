import pygame
from animaciones3 import *

class Objeto:
    def __init__(self, path_image, x_inicial, y_inicial, tamaño):
        self.imagen = pygame.image.load(path_image)
        self.tamaño = tamaño
        self.imagen = pygame.transform.scale(self.imagen, (self.tamaño))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x_inicial
        self.rectangulo.y = y_inicial
        self.lados = obtener_rectangulos(self.rectangulo)
        self.contador_pasos = 0 

    def animar(self, screen, animaciones, que_animacion):
        self.animaciones = animaciones
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        screen.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1