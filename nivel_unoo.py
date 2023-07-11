from nivel import Nivel
import pygame
from plataforma import *
from animaciones import *
from modo import *
from personaje import *
from objeto_juego import *
from personaje_enemigo import *
from items import *

class NivelUno(Nivel):
    def __init__(self, pantalla, personaje_principal, enemigo, trampas, trampolines, items,
                  lista_plataformas, imagen_fondo, lados_plataformas):
        
                
        W = pantalla.get_width()
        H = pantalla.get_height()
        screen_size = (W, H)

        fondo_escalado = pygame.image.load("proyecto_pygame/imagenes_fondos/fondo_juego_transformed.jpeg")
        fondo_escalado = pygame.transform.scale(fondo_escalado, screen_size)




        #PISO
        piso = pygame.Rect(10,10, LARGO, 10)  
        piso.top = self.jugador.lados["main"].bottom


        plataforma = Plataforma("proyecto_pygame/plataforma/plataform.png", (450, 270), 150, 20)

        plataforma2 = Plataforma("proyecto_pygame/plataforma/plataform.png", (700, 150), 150, 20)

        plataforma3 = Plataforma("proyecto_pygame/plataforma/plataform.png",(200, 150), 150,20)


        lista_plataformas = [plataforma, plataforma2, plataforma3]

        piso_lados = obtener_rectangulos(piso)

        lados_plataformas = [piso_lados, plataforma.lados, plataforma2.lados, plataforma3.lados]

        trampolin1 = Trampolin("proyecto_pygame/trampolin/0.png", 200, 390, (60,45), diccionario_trampolin)

        trampolines = [trampolin1]


        trampa1 = Trampa("proyecto_pygame/trampa/0.png", 710, 135, (60,50), diccionario_trampa)
        trampa2 = Trampa("proyecto_pygame/trampa/0.png", 210, 135, (60,50), diccionario_trampa)
        trampa3 = Trampa("proyecto_pygame/trampa/0.png", 700, 380, (60,50), diccionario_trampa)

        trampas = [trampa1, trampa2, trampa3]
        


        

        super().__init__(pantalla, personaje_principal, enemigo, trampas, trampolines, items, lista_plataformas, imagen_fondo, lados_plataformas)