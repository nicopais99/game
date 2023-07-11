import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagen(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)


def obtener_rectangulos(principal):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right- 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)
    return diccionario
    


personaje_quieto = [
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Quieto/0_quieto.png")
]

personaje_corriendo = [
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Corriendo/0_caminando.png"),
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Corriendo/1_caminando.png"),
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Corriendo/2_caminando.png"),
    ]

personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo, True, False)

personaje_saltando = [
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Saltando/1_saltando.png"),
]

personaje_saltando_izquierda = girar_imagenes(personaje_saltando, True, False)

personaje_disparando = [ 
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Disparando/disparando_1.png"),
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Disparando/disparando_2.png"),
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Disparando/disparando_3.png"),]


personaje_muriendo = [    
    pygame.image.load("proyecto_pygame/Secuencia_personaje/Muriendo/0.png")
]

icono_bugs = pygame.image.load("proyecto_pygame/Secuencia_personaje/vidas/icono_bugs.png")
icono_bugs = pygame.transform.scale(icono_bugs, (40,50))

item = pygame.image.load("proyecto_pygame/items/item1_mejorado.png")
item = pygame.transform.scale(item, (30,40))

item_carrot =[ 
    pygame.image.load("proyecto_pygame/items/0.png"),
    pygame.image.load("proyecto_pygame/items/1.png"),
    pygame.image.load("proyecto_pygame/items/2.png"),
    pygame.image.load("proyecto_pygame/items/3.png"),
    pygame.image.load("proyecto_pygame/items/4.png"),
    pygame.image.load("proyecto_pygame/items/5.png"),
    pygame.image.load("proyecto_pygame/items/6.png"),
    pygame.image.load("proyecto_pygame/items/7.png"),
    pygame.image.load("proyecto_pygame/items/8.png"),
    pygame.image.load("proyecto_pygame/items/9.png"),
    ]

reescalar_imagen(item_carrot, (20,30))


item_vida = [pygame.image.load("proyecto_pygame/Secuencia_personaje/vidas/icono_bugs.png")]

diccionario_item_vida = {}
diccionario_item_vida["main"] = item_vida




diccionario_animaciones_carrot = {}
diccionario_animaciones_carrot["main"] = item_carrot

bullet_personaje =[ 
    pygame.image.load("proyecto_pygame/proyectil/0.png"),
    pygame.image.load("proyecto_pygame/proyectil/1.png"),
    pygame.image.load("proyecto_pygame/proyectil/2.png"),
    pygame.image.load("proyecto_pygame/proyectil/3.png"),
    pygame.image.load("proyecto_pygame/proyectil/4.png"),
]



diccionario_bullet_personaje = {}
diccionario_bullet_personaje["main"] = bullet_personaje



trampolin = [
    pygame.image.load("proyecto_pygame/trampolin/0.png"),
    pygame.image.load("proyecto_pygame/trampolin/1.png"),
    pygame.image.load("proyecto_pygame/trampolin/2.png"),
    pygame.image.load("proyecto_pygame/trampolin/3.png"),
    pygame.image.load("proyecto_pygame/trampolin/4.png")]


diccionario_trampolin = {}
diccionario_trampolin["main"] = trampolin


trampa = [ pygame.image.load("proyecto_pygame/trampa/0.png")
]

diccionario_trampa = {}
diccionario_trampa["main"] = trampa

reescalar_imagen(trampa, (20,20))


#BOSS

boss = [pygame.image.load("proyecto_pygame/Boss/0.png"),
        pygame.image.load("proyecto_pygame/Boss/0.png"),
        pygame.image.load("proyecto_pygame/Boss/0.png"),
        pygame.image.load("proyecto_pygame/Boss/0.png"),
        pygame.image.load("proyecto_pygame/Boss/0.png"),
        pygame.image.load("proyecto_pygame/Boss/0.png")
        ]

diccionario_boss = {}
diccionario_boss["main"] = boss

boss_corriendo_izquierda = girar_imagenes(boss, True, False)

reescalar_imagen(boss, (50,65))


rectangulo_item = item.get_rect()
lados_item = obtener_rectangulos(rectangulo_item)
#ENEMIGO

lista_enemigo_izquierda = [
    pygame.image.load("proyecto_pygame/Secuencia_enemigo/0.png"),
    pygame.image.load("proyecto_pygame/Secuencia_enemigo/1.png"),
    pygame.image.load("proyecto_pygame/Secuencia_enemigo/2.png"),
    pygame.image.load("proyecto_pygame/Secuencia_enemigo/3.png"),
    pygame.image.load("proyecto_pygame/Secuencia_enemigo/4.png")
]

enemigo_corriendo_derecha = girar_imagenes(lista_enemigo_izquierda, True, False)



diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["corriendo_izquierda_enemigo"] = lista_enemigo_izquierda
diccionario_animaciones_enemigo["corriendo_derecha_enemigo"] = enemigo_corriendo_derecha



#PERSONAJE:
diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["corriendo_derecha"] = personaje_corriendo
diccionario_animaciones["corriendo_izquierda"] = personaje_corriendo_izquierda
diccionario_animaciones["saltando"] = personaje_saltando
diccionario_animaciones["personaje_saltando_izquierda"] = personaje_saltando_izquierda
diccionario_animaciones["personaje_disparando"] = personaje_disparando
diccionario_animaciones["personaje_muriendo"] = personaje_muriendo



