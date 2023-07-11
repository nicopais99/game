import pygame
from personaje import *
from animaciones import *
from objeto_juego import *
from plataforma import *
from items import Item
import random
from random import randint
import time





class Personaje_Enemigo(Objeto):
    def __init__(self, imagen, animaciones,x_inicial, y_inicial, tamaño):
        super().__init__(imagen, x_inicial, y_inicial, tamaño)
        self.tamaño = tamaño
        self.imagen = imagen
        self.imagen = pygame.image.load(self.imagen)
        self.imagen = pygame.transform.scale(self.imagen, (self.tamaño))
        self.y_inicial = x_inicial
        self.x_inicial = y_inicial
        self.gravedad = 2
        self.velocidad = 3
        self.limite_velocidad_caida = 15
        self.personaje_top = False
        self.daño = 1
        self.en_plataforma = False
        self.desplazamiento_y = 0
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.direccion = ["izquierda", "derecha"]
        self.animaciones = animaciones
        self.direccion_aleatoria = random.randint(0, len(self.direccion)- 1)
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["corriendo_derecha_enemigo"][0].get_rect()
        self.rectangulo.x = x_inicial
        self.rectangulo.y = y_inicial
        self.lados_enemigo = obtener_rectangulos(self.rectangulo)

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, lista_plataformas, lista_enemigos):
        for direccion in self.direccion:
            if self.direccion_aleatoria == 1:
                self.mover(self.velocidad)
                self.animar(pantalla, self.animaciones, "corriendo_derecha_enemigo")
            else:
                self.mover(self.velocidad * -1)
                self.animar(pantalla, self.animaciones, "corriendo_izquierda_enemigo")

        self.caer_libre()
        self.realizar_comportamiento(pantalla, lista_plataformas)
        
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto))
        
    def caer_libre(self):
        for lados in self.lados_enemigo:
            self.lados[lados].y += self.desplazamiento_y
                
        if (self.desplazamiento_y + self.gravedad) < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad

    def realizar_comportamiento(self, pantalla, lista_plataformas):
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma["top"]):
                self.desplazamiento_y = 0
                self.lados["main"].bottom = plataforma["main"].top + 5
                self.en_plataforma = True
                if self.en_plataforma == True and self.lados["main"].right > plataforma["main"].right - 2:
                    self.direccion_aleatoria = 0
                elif self.en_plataforma == True and self.lados["main"].left < plataforma["main"].left + 2:
                    self.direccion_aleatoria = 1

                

        for lados in self.lados:
            if self.lados["main"].right > 1000 -10:
                self.direccion_aleatoria = 0
            elif self.lados["main"].left < 10:
                self.direccion_aleatoria = 1

    
                

    




lista_enemigos = []
for i in range(6):
    x_inicial = random.randrange(50, 740, 40) 
    y_inicial = random.randrange(-100, -50, 40)
    enemigo = Personaje_Enemigo("proyecto_pygame/Secuencia_enemigo/1.png", diccionario_animaciones_enemigo, x_inicial, y_inicial, (35, 40))
    lista_enemigos.append(enemigo)


class Proyectil(Item):
    def __init__(self, posx, posy, imagen, tamaño, animaciones, direccion):
        super().__init__(imagen, x_inicial, y_inicial, tamaño, animaciones)
        self.tamaño = tamaño
        self.rectangulo = self.imagen.get_rect()
        self.velocidad = 10
        self.direccion = direccion
        self.rectangulo.right = posx
        self.rectangulo.top = posy
        self.lista_animaciones = animaciones
        self.lados = obtener_rectangulos(self.rectangulo)
        self.reescalar_animaciones()


    def trayectoria(self):
        if self.direccion == "Derecha":
            self.rectangulo.left = self.rectangulo.left + self.velocidad
        else:
            self.rectangulo.left = self.rectangulo.left - self.velocidad

    def update (self, pantalla):
        self.trayectoria()
        self.animar(pantalla, "main", 0.5)

    


class Trampolin(Item):
    def __init__(self, imagen, x_inicial, y_inicial, tamaño, animaciones):
        super().__init__(imagen, x_inicial, y_inicial, tamaño, animaciones)


        
    def update(self, pantalla, lista_items):
        for item in lista_items:
            self.animar(pantalla, "main", 0.5)


class Trampa(Trampolin):
    def __init__(self, imagen, x_inicial, y_inicial, tamaño, animaciones):
        super().__init__(imagen, x_inicial, y_inicial, tamaño, animaciones)
        self.animaciones = animaciones


class Boss(Personaje_Enemigo):
    def __init__(self, imagen, animaciones, x_inicial, y_inicial, tamaño):
        super().__init__(imagen, animaciones, x_inicial, y_inicial, tamaño)
        self.vidas = 10
        self.lista_disparos = []
        self.rectangulo.top = y_inicial 
        self.rectangulo.left = x_inicial
        self.vivo = True


    def atacar(self):
        if (randint(0,100) < 2):
            self.disparar()

    def update(self, pantalla):
        self.animar(pantalla, diccionario_boss, "corriendo_derecha_enemigo")
        self.atacar()
        if len(self.lista_disparos) > 0:
            for disparo in self.lista_disparos:
                disparo.update(pantalla)


    def disparar(self):
        x,y = self.rectangulo.center
        proyectil_enemigo = Proyectil(x, y, "proyecto_pygame/proyectil/0.png", (20,30), diccionario_bullet_personaje, "Izquierda")
        self.lista_disparos.append(proyectil_enemigo)

    









