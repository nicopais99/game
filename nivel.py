import pygame
from modo import *


class Nivel:
    def __init__(self, pantalla, personaje_principal, enemigo, trampas, trampolines, items, lista_plataformas, imagen_fondo,lados_plataformas, lista_trampolines, lista_trampas, item_vida, boss = None):
        
        self.slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.enemigo = enemigo
        self.trampas = trampas
        self.trampolines = trampolines
        self.items = items
        self.lados_plataformas = lados_plataformas
        self.lista_trampolines = lista_trampolines
        self.lista_trampas = lista_trampas
        self.boss = boss
        self.item_vida = item_vida
        

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        self.leer_inputs()
        self.actualizar_pantalla()
        self.jugador.blit_vidas_puntaje(self.slave)


    def leer_inputs(self):
        presiono = pygame.key.get_pressed()
        if presiono[pygame.K_RIGHT] and self.jugador.lados["main"].right < self.slave.get_widht() -15:
            self.jugador.que_hace = "Derecha"
        elif presiono[pygame.K_LEFT] and self.jugador.lados["main"].left > 10:
            self.jugador.que_hace = "Izquierda"
        elif presiono[pygame.K_UP]:
            self.jugador.que_hace = "Saltando"
        elif presiono[pygame.K_SPACE]:
            self.jugador.que_hace = "Disparando"
            x , y = self.jugador.rectangulo.center
            self.jugador.disparar(x, y)
        else:
            self.jugador.que_hace = "Quieto"

    def dibujar_rectangulos(self):
        if get_mode():
            pygame.draw.rect(self.slave, "Green", self.plataformas, 3)
        for plataforma in self.plataformas:
            for lado in plataforma.lados:
                pygame.draw.rect(self.slave, "yellow", self.plataformas.lados[lado], 3)
            
        for lado in self.jugador.lados:
            pygame.draw.rect(self.slave, "orange", self.jugador.lados[lado], 3)


    def actualizar_pantalla(self):
        self.slave.blit(self.img_fondo, (0,0))

        for plataforma in self.plataformas:
            plataforma.update(self.slave)
        
        for item in self.items:
            item.update(self.slave,self.items)
        
        for trampolin in self.trampolines:
            trampolin.update(self.slave, self.trampolines)

        for trampa in self.trampas:
            trampa.update(self.slave, self.trampas)

        for item in self.items:
            item.update(self.slave, self.items)    


        if len(self.jugador.lista_disparos) > 0:
            for disparo in self.jugador.lista_disparos:
                disparo.update(self.slave)

        self.jugador.update(self.slave, self.lados_plataformas, self.enemigo, self.items, self.trampolines, self.trampas,self.item_vida, self.boss)


        # self, pantalla, lados_plataforma, enemigo, lista_items, lista_trampolines, lista_trampas, item_vida, boss):