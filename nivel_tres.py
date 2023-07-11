from nivel import Nivel
import pygame
from plataforma import *
from animaciones import *
from modo import *
from personaje import *
from objeto_juego import *
from personaje_enemigo import *
from items import *

class NivelTres(Nivel):
    def __init__(self, pantalla, personaje_principal, enemigo, lista_trampas, lista_trampolines, items, lista_item_vida,
                  lista_plataformas, imagen_fondo, lados_plataformas, lista_boss):
        
                
        W = pantalla.get_width()
        H = pantalla.get_height()
        screen_size = (W, H)

        fondo_escalado = pygame.image.load("proyecto_pygame/imagenes_fondos/background-transformed.jpeg")
        fondo_escalado = pygame.transform.scale(fondo_escalado, screen_size)


        #PISO
        piso = pygame.Rect(10,10, LARGO, 10)  
        piso.top = mi_personaje.lados["main"].bottom
        piso_lados = obtener_rectangulos(piso)


        plataforma = Plataforma("proyecto_pygame/plataforma/plataform.png", (450, 290), 150, 20)

        plataforma2 = Plataforma("proyecto_pygame/plataforma/plataform.png", (700, 170), 150, 20)

        plataforma3 = Plataforma("proyecto_pygame/plataforma/plataform.png",(200, 170), 150,20)


        lista_plataformas = [plataforma, plataforma2, plataforma3]

        lados_plataformas = [piso_lados, plataforma.lados, plataforma2.lados, plataforma3.lados]

        trampolin1 = Trampolin("proyecto_pygame/trampolin/0.png", 200, 430, (60,45), diccionario_trampolin)

        lista_trampolines = [trampolin1]


        trampa1 = Trampa("proyecto_pygame/trampa/0.png", 710, 155, (60,50), diccionario_trampa)
        trampa2 = Trampa("proyecto_pygame/trampa/0.png", 210, 155, (60,50), diccionario_trampa)
        trampa3 = Trampa("proyecto_pygame/trampa/0.png", 700, 380, (60,50), diccionario_trampa)

        lista_trampas = [trampa1, trampa2, trampa3]


        item_vida1 = Item_vida("proyecto_pygame/Secuencia_personaje/vidas/icono_bugs.png", 700, 500, (50,60), diccionario_item_vida)

        lista_item_vida = [item_vida1]

        boss = Boss("Proyecto_pygame/Boss/0.png", diccionario_boss, 800, 325, (70,100))


        lista_boss = [boss]


        

        super().__init__(pantalla, personaje_principal, enemigo, lista_trampas, lista_trampolines, items, lista_item_vida, lista_plataformas, imagen_fondo, lados_plataformas, lista_boss)