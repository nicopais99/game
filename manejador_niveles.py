import pygame
from nivel_unoo import *
from nivel_doos import *
from nivel_tres import *


class ManejadorNiveles:
    def __init__(self, pantalla):
        self.slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}


    

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self.slave)
        