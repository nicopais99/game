import pygame , sys
from animaciones import *
from modo import *
from nivel_doos import NivelDos



Clock = pygame.time.Clock()


nivel_actual = NivelDos(PANTALLA)



while True:
    Clock.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos :
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
    nivel_actual.update(eventos)
 

        
    pygame.display.update()


