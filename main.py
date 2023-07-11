import pygame , sys
from animaciones import *
from modo import *
from personaje import *
from objeto_juego import *
from personaje_enemigo import *
from plataforma import *
from items import *




FPS = 20
LARGO = 1000
ANCHO = 500
screen_size = (LARGO, ANCHO)
PANTALLA = pygame.display.set_mode((screen_size)) #pixeles

fondo_escalado = pygame.image.load("proyecto_pygame/imagenes_fondos/fondo_juego_transformed.jpeg")
fondo_escalado = pygame.transform.scale(fondo_escalado, screen_size)






#PISO
piso = pygame.Rect(10,10, LARGO, 10)  
piso.top = mi_personaje.lados["main"].bottom
piso_lados = obtener_rectangulos(piso)


plataforma = Plataforma("proyecto_pygame/plataforma/plataform.png", (450, 270), 150, 20)

plataforma2 = Plataforma("proyecto_pygame/plataforma/plataform.png", (700, 150), 150, 20)

plataforma3 = Plataforma("proyecto_pygame/plataforma/plataform.png",(200, 150), 150,20)


lista_plataformas = [plataforma, plataforma2, plataforma3]

lados_plataformas = [piso_lados, plataforma.lados, plataforma2.lados, plataforma3.lados]

trampolin1 = Trampolin("proyecto_pygame/trampolin/0.png", 200, 390, (60,45), diccionario_trampolin)

lista_trampolines = [trampolin1]


trampa1 = Trampa("proyecto_pygame/trampa/0.png", 710, 135, (60,50), diccionario_trampa)
trampa2 = Trampa("proyecto_pygame/trampa/0.png", 210, 135, (60,50), diccionario_trampa)
trampa3 = Trampa("proyecto_pygame/trampa/0.png", 700, 380, (60,50), diccionario_trampa)

lista_trampas = [trampa1, trampa2, trampa3]


item_vida = Item_vida("proyecto_pygame/Secuencia_personaje/vidas/icono_bugs.png", 300, 325, (30,30), diccionario_item_vida)
item_vida1 = Item_vida("proyecto_pygame/Secuencia_personaje/vidas/icono_bugs.png", 150, 325, (30,30), diccionario_item_vida)

lista_item_vida = [item_vida, item_vida1]

boss = Boss("Proyecto_pygame/Boss/0.png", diccionario_boss, 500, 325, (45,45))


lista_boss = [boss]

def actualizar_pantalla(pantalla, un_personaje:Personaje, un_enemigo, fondo, lados_plataforma,
                        lista_plataformas, lista_items, lista_trampolines, lista_trampas, item_vida, boss):
    pantalla.blit(fondo, (0,0))

    for plataforma in lista_plataformas:
        plataforma.update(pantalla)
    
    for item in lista_items:
        item.update(pantalla,lista_items)
    
    for trampolin in lista_trampolines:
        trampolin.update(pantalla, lista_trampolines)

    for trampa in lista_trampas:
        trampa.update(pantalla, lista_trampas)

    for item in item_vida:
        item.update(pantalla)    

    if len(lista_boss) > 0:
        lista_boss[0].update(pantalla)


    if len(mi_personaje.lista_disparos) > 0:
        for disparo in mi_personaje.lista_disparos:
            disparo.update(pantalla)

    un_personaje.update(pantalla, lados_plataforma, un_enemigo, lista_items, lista_trampolines, lista_trampas, item_vida, boss)



pygame.init()

sonido = pygame.mixer.Sound("proyecto_pygame/Sonidos/intro.mp3")
sonido.set_volume(0)
sonido.play()

 

Clock = pygame.time.Clock()

while True:
    Clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
             if evento.key == pygame.K_TAB:
                  cambiar_modo()
                  
    presiono = pygame.key.get_pressed()
    if presiono[pygame.K_RIGHT] and mi_personaje.lados["main"].right < LARGO -15:
        mi_personaje.que_hace = "Derecha"
    elif presiono[pygame.K_LEFT] and mi_personaje.lados["main"].left > 10:
        mi_personaje.que_hace = "Izquierda"
    elif presiono[pygame.K_UP]:
         mi_personaje.que_hace = "Saltando"
    elif presiono[pygame.K_SPACE]:
        mi_personaje.que_hace = "Disparando"
        x , y = mi_personaje.rectangulo.center
        mi_personaje.disparar(x, y)
    else:
         mi_personaje.que_hace = "Quieto"

    actualizar_pantalla(PANTALLA, mi_personaje, lista_enemigos, fondo_escalado, lados_plataformas, 
                        lista_plataformas, lista_items, lista_trampolines, lista_trampas, lista_item_vida, lista_boss)
    mi_personaje.blit_vidas_puntaje(PANTALLA)
 
    if get_mode():
        pygame.draw.rect(PANTALLA, "Green", piso, 3)
        for plataforma in lista_plataformas:
            for lado in plataforma.lados:
                pygame.draw.rect(PANTALLA, "yellow", plataforma.lados[lado], 3)
            
        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "orange", mi_personaje.lados[lado], 3)

        for enemigo in lista_enemigos:
            for lado in enemigo.lados:
                pygame.draw.rect(PANTALLA, "orange", enemigo.lados[lado], 3)






        
    pygame.display.update()


