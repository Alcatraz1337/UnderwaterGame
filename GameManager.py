from operator import imod
import pygame
import numpy as np
import Agent as ag
import Obstacles as ob

# Color Definination
available = 128,128,128 
connected = 60,142,100
blocked = 236,19,22

def DrawConnection(agents:list, screen:pygame.Surface):
    for i in range(0, len(agents) - 1):
        for j in range(i + 1, len(agents)):
            pygame.draw.line(screen, available, agents[i].GetCoordinate(), agents[j].GetCoordinate(), 1)
