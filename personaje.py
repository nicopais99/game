import pygame
from animaciones import *
from objeto_juego import *
from plataforma import *
from objeto_juego import Objeto
from personaje_enemigo import *
from items import *



pygame.font.init()


fuente = pygame.font.SysFont("segoe print", 25)


class Personaje:
    def __init__(self, tamaño, velocidad, animaciones, posicion_inicial):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.gravedad = 1
        self.potencia_salto = -16
        self.limite_velocidad_caida = self.potencia_salto * -1
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.velocidad = velocidad
        self.animaciones = animaciones
        self.contador_pasos = 0
        self.lista_disparos = []
        self.puntaje = 0
        self.vidas = 3
        self.colision_item = False
        self.muerto = False
        self.colisionado = False
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["corriendo_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)

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

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, lados_plataforma, enemigo, lista_items, lista_trampolines, lista_trampas, item_vida, boss):
        match self.que_hace:
            case "Derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "corriendo_derecha", 1)
                    self.colisionado = False
                self.mover(self.velocidad)
            case "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "corriendo_izquierda", 1)
                    self.colisionado = False
                self.mover(self.velocidad * -1)
            case "Saltando":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto", 1)
            case "Disparando":
                if not self.esta_saltando:
                    self.animar(pantalla, "personaje_disparando", 0.2)
                else:
                    self.animar(pantalla, "personaje_disparando", 0.2)
                    self.esta_saltando = False
       

        self.aplicar_gravedad(pantalla, lados_plataforma)
        for enemigo in lista_enemigos:
            enemigo.update(pantalla, lados_plataforma, lista_enemigos)
        
        if len(boss) > 0:
            self.verificar_colision_bullet_boss(boss[0].lista_disparos)
        self.verificar_colision_enemigo(pantalla, lista_enemigos)
        self.verificar_colision_items(lista_items)
        self.detectar_colision_proyectil(lista_enemigos)
        self.verificar_colision_trampolin(lista_trampolines)
        self.verificar_colision_trampas(lista_trampas)
        self.verificar_colision_boss(boss)
        self.verificar_colision_vida(item_vida)

    def verificar_colision_vida(self, item_vida):
        for item in item_vida.lados:
            if self.lados["main"].colliderect(item.lados["main"]):
                if self.vidas < 3:
                    self.vidas = self.vidas + 1
                    print("ingreso aqui")
                    item_vida.remove(item)
            
        
    def reaparecer_personaje(self, rectangulo_personaje: pygame.Rect):
        for lados in self.lados:
            self.lados[lados].x = posicion_inicial[0]
            self.lados[lados].y = posicion_inicial[1] - 100
        self.rectangulo.x = rectangulo_personaje["main"].x
        self.rectangulo.y = rectangulo_personaje["main"].y


    def desaparecer_personaje(self):
        for lados in self.lados:
            self.lados[lados].y += self.desplazamiento_y
            mi_personaje.lados[lados].y = 1000


    def verificar_colision_boss(self, lista_boss):
            for disparo in self.lista_disparos:
                if len(lista_boss) > 0:
                    if disparo.lados["main"].colliderect(lista_boss[0].lados["main"]):
                        lista_boss[0].vidas = lista_boss[0].vidas - 1
                        self.lista_disparos.remove(disparo)

                    if lista_boss[0].vidas < 1:
                        lista_boss.remove(lista_boss[0])

            
    def verificar_colision_bullet_boss(self, lista_balas):
        for bala in lista_balas:
            if self.lados["main"].colliderect(bala.lados["main"]):
                self.vidas = self.vidas -1
                lista_balas.remove(bala)
                self.reaparecer_personaje(self.lados)

            


    def verificar_colision_trampolin(self, lista_trampolines):
        for trampa in lista_trampolines:
            if self.lados["bottom"].colliderect(trampa.lados["top"]):
                self.desplazamiento_y = -20
                for lados in self.lados:
                    self.lados[lados].y += self.desplazamiento_y


    def verificar_colision_trampas(self, lista_trampas):
        for trampa in lista_trampas:
            if self.lados["bottom"].colliderect(trampa.lados["top"]):
                self.vidas = self.vidas - 1
                lista_trampas.remove(trampa)
                break


    def aplicar_gravedad(self, pantalla, lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "saltando", 1)
             
            for lados in self.lados:
                self.lados[lados].y += self.desplazamiento_y
                
            if (self.desplazamiento_y + self.gravedad) < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for plataforma in lista_plataformas:
                if self.lados["bottom"].colliderect(plataforma["top"]):
                    self.esta_saltando  = False
                    self.desplazamiento_y = 0
                    self.lados["main"].bottom = plataforma["main"].top + 5
                    break
                else:
                    self.esta_saltando = True


    def verificar_colision_enemigo(self, pantalla, lista_enemigos):
        colision = False
        for enemigo in lista_enemigos:
            for lados in self.lados:

                if not self.colisionado and self.lados["right"].colliderect(enemigo.lados["left"]):
                    colision = True
                    self.colisionado = True
                    self.animar(pantalla, "personaje_muriendo", 0.1)
                    self.desaparecer_personaje()        
                    self.reaparecer_personaje(self.lados)    

                elif not self.colisionado and self.lados["left"].colliderect(enemigo.lados["right"]):
                    colision = True
                    self.colisionado = True
                    self.animar(pantalla, "personaje_muriendo", 0.1)
                    self.desaparecer_personaje()    
                    self.reaparecer_personaje(self.lados)           
                elif not self.colisionado and self.lados["left"].colliderect(enemigo.lados["left"]):
                    colision = True
                    self.colisionado = True
                    self.animar(pantalla, "personaje_muriendo", 0.1)
                    self.desaparecer_personaje()     
                    self.reaparecer_personaje(self.lados)   
                elif not self.colisionado and self.lados["right"].colliderect(enemigo.lados["right"]):
                    colision = True
                    self.colisionado = True
                    self.animar(pantalla, "personaje_muriendo", 0.1)
                    self.desaparecer_personaje()     
                    self.reaparecer_personaje(self.lados)    
                elif not self.colisionado and self.lados["top"].colliderect(enemigo.lados["bottom"]):
                    colision = True
                    self.colisionado = True
                    self.animar(pantalla, "personaje_muriendo", 0.1)
                    self.desaparecer_personaje()     
                    self.reaparecer_personaje(self.lados)        

                elif self.lados["bottom"].colliderect(enemigo.lados["top"]):
                    self.desplazamiento_y = -6
                    for lados in self.lados:
                        self.lados[lados].y += self.desplazamiento_y
                        enemigo.lados[lados].y = 1000
                    self.puntaje = self.puntaje + 100

                    if (self.desplazamiento_y + self.gravedad) < 10:
                        self.desplazamiento_y += self.gravedad

        if colision:
            self.vidas -= 1

    def verificar_colision_items(self, lista_items):
        for item in lista_items:
            if self.lados["main"].colliderect(item.lados["main"]):
                for lado in item.lados:
                    lista_items.remove(item)
                    break
                self.puntaje = self.puntaje + 100


    def disparar(self, x, y):
        if mi_personaje.que_hace == "Derecha":
            mi_proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y, "proyecto_pygame/proyectil/0.png", (20,30), diccionario_bullet_personaje, "Derecha")
        elif mi_personaje.que_hace == "Izquierda":
            mi_proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y, "proyecto_pygame/proyectil/0.png", (20,30), diccionario_bullet_personaje, "Izquierda")
        else:
            mi_proyectil = Proyectil(self.rectangulo.x, self.rectangulo.y, "proyecto_pygame/proyectil/0.png", (20,30), diccionario_bullet_personaje, "Derecha")


        self.lista_disparos.append(mi_proyectil)


    def detectar_colision_proyectil(self, lista_enemigos):
        for disparos in self.lista_disparos:
            for enemigo in lista_enemigos:
                if disparos.lados["main"].colliderect(enemigo.lados["main"]):
                    self.puntaje = self.puntaje + 100
                    lista_enemigos.remove(enemigo)
                    for lado in disparos.lados:
                        if disparos in self.lista_disparos:
                            self.lista_disparos.remove(disparos)
                            break
                    

    def blit_vidas_puntaje(self, pantalla):
        pantalla.blit(icono_bugs, (720,0))
        vidas = fuente.render(f"{self.vidas}", True, "Orange")
        pantalla.blit(vidas, (690,5))
        puntaje = fuente.render(f"Points: {self.puntaje}", True, "Orange")
        pantalla.blit(puntaje, (800, 5))





x_inicial = 50
y_inicial = 325
posicion_inicial = (x_inicial, y_inicial)
tamaño = (45,65)
mi_personaje = Personaje(tamaño, 10, diccionario_animaciones, posicion_inicial)







        
