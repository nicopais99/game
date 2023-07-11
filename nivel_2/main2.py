import pygame , sys
from animaciones2 import *
from modo2 import *
from personaje2 import *
from objeto_juego2 import *
from personaje_enemigo2 import *
from plataforma2 import *
from items2 import *




FPS = 20
LARGO = 1000
ANCHO = 500
screen_size = (LARGO, ANCHO)
PANTALLA = pygame.display.set_mode((screen_size)) #pixeles

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







def actualizar_pantalla(pantalla, un_personaje:Personaje, un_enemigo, fondo, lados_plataforma,
                        lista_plataformas, lista_items, lista_trampolines, lista_trampas):
    pantalla.blit(fondo, (0,0))

    for plataforma in lista_plataformas:
        plataforma.update(pantalla)
    
    for item in lista_items:
        item.update(pantalla,lista_items)
    
    for trampolin in lista_trampolines:
        trampolin.update(pantalla, lista_trampolines)

    for trampa in lista_trampas:
        trampa.update(pantalla, lista_trampas)





    if len(mi_personaje.lista_disparos) > 0:
        for disparo in mi_personaje.lista_disparos:
            disparo.update(pantalla)

    un_personaje.update(pantalla, lados_plataforma, un_enemigo, lista_items, lista_trampolines, lista_trampas)




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

    actualizar_pantalla(PANTALLA, mi_personaje, lista_enemigos, fondo_escalado, lados_plataformas, lista_plataformas, lista_items, lista_trampolines, lista_trampas)
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

        # for disparo in mi_personaje.lista_disparos:
        #     for lado in mi_personaje.lista_disparos:
        #         pygame.draw.rect(PANTALLA, "Yellow", disparo.lados[lado], 3)


        
    pygame.display.update()


