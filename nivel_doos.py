from nivel import Nivel
import pygame
from plataforma import *
from animaciones import *
from modo import *
from personaje import *
from objeto_juego import *
from personaje_enemigo import *
from items import *

class NivelDos(Nivel):
    def __init__(self, pantalla):
        
                
        W = pantalla.get_width()
        H = pantalla.get_height()
        screen_size = (W, H)

        fondo_escalado = pygame.image.load("proyecto_pygame/imagenes_fondos/fondo_bosque_transformed.jpeg")
        fondo_escalado = pygame.transform.scale(fondo_escalado, screen_size)


        #PISO
        piso = pygame.Rect(10,10, LARGO, 10)  
        piso.top = mi_personaje.lados["main"].bottom
        piso_lados = obtener_rectangulos(piso)



        plataforma = Plataforma("proyecto_pygame/plataforma/plataform.png", (30, 100), 150,20)
        plataforma2 = Plataforma("proyecto_pygame/plataforma/plataform.png", (100, 180), 150,20)
        plataforma3 = Plataforma("proyecto_pygame/plataforma/plataform.png",(150, 260), 150,20)

        plataforma5 = Plataforma("proyecto_pygame/plataforma/plataform.png",(800, 100), 150,20)
        plataforma6 = Plataforma("proyecto_pygame/plataforma/plataform.png",(750, 180), 150,20)
        plataforma7 = Plataforma("proyecto_pygame/plataforma/plataform.png",(700, 260), 150,20)


        lista_plataformas = [plataforma, plataforma2, plataforma3, plataforma5, plataforma6, plataforma7]

        lados_plataformas = [piso_lados, plataforma.lados, plataforma2.lados, plataforma3.lados, plataforma5.lados, plataforma6.lados, plataforma7.lados]



        trampolin1 = Trampolin("proyecto_pygame/trampolin/0.png", 500, 390, (60,45), diccionario_trampolin)

        lista_trampolines = [trampolin1]


        trampa1 = Trampa("proyecto_pygame/trampa/0.png", 60, 85, (50,50), diccionario_trampa)
        trampa2 = Trampa("proyecto_pygame/trampa/0.png", 220, 165, (50,50), diccionario_trampa)
        trampa3 = Trampa("proyecto_pygame/trampa/0.png", 700, 380, (50,50), diccionario_trampa)

        lista_trampas = [trampa1, trampa2, trampa3]


        boss = Boss("proyecto_pygame/Boss/0.png", diccionario_boss, 400, 325, (60,60))
        lista_boss = [boss]

        
        lista_items = []
        for i in range(4):
            x_inicial = random.randrange(50, 600, 30) 
            y_inicial = random.randrange(50, 300, 30)
            item = Item("proyecto_pygame/items/0.png", x_inicial, y_inicial, (25, 30), diccionario_animaciones_carrot)
            lista_items.append(item)



        super().__init__(pantalla, mi_personaje, enemigo, lista_trampas, lista_trampolines, lista_items, lista_plataformas, fondo_escalado, lados_plataformas, lista_trampolines, lista_trampas, item_vida, lista_boss)