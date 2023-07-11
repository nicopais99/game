import pygame
import random
from objeto_juego import *


class Item(Objeto):
    def __init__(self, imagen, x_inicial, y_inicial, tamaño, animaciones):
        super().__init__(imagen, x_inicial, y_inicial, tamaño)
        self.tamaño = tamaño
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.y_inicial = y_inicial        
        self.x_inicial = x_inicial
        self.imagen = imagen
        self.imagen = pygame.image.load(self.imagen)
        self.imagen = pygame.transform.scale(self.imagen, (self.tamaño))
        self.animaciones = animaciones
        self.rectangulo = self.animaciones["main"][0].get_rect()
        self.rectangulo.x = x_inicial
        self.rectangulo.y = y_inicial
        self.lados_items = obtener_rectangulos(self.rectangulo)
        self.desplazamiento_y = 0
        self.gravedad = -1
        self.limite_velocidad = 1

      
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))



    def animar(self, screen, que_animacion, velocidad_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        screen.blit(animacion[int(self.contador_pasos)], self.lados["main"])
        self.contador_pasos += velocidad_animacion
 

    
    def update(self, pantalla, lista_items):
        for item in lista_items:
            self.animar(pantalla, "main", 0.2)










class Item_vida(Item):
    def __init__(self, imagen, x_inicial, y_inicial, tamaño, animaciones):
        super().__init__(imagen, x_inicial, y_inicial, tamaño, animaciones)
        self.lados = obtener_rectangulos(self.rectangulo)
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamaño)
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial

    def update(self, pantalla, x_inicial, y_inicial):
        pantalla.blit(self.imagen,(x_inicial, y_inicial))

