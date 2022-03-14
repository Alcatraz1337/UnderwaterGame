from operator import imod
import pygame
import Agent as ag
import Obstacles as ob
import numpy as np

# Color Definination
available = 128,128,128 
connected = 60,142,100
blocked = 236,19,22

def DrawConnection(table:np.array, agents:list, screen:pygame.Surface):
    for i in range(0, len(table) - 1):
        for j in range(i + 1, len(table)):
            if table[i][j] == 0:
                pygame.draw.line(screen, available, agents[i].GetCoordinate(), agents[j].GetCoordinate(), 1)
            if table[i][j] == 1:
                pygame.draw.line(screen, connected, agents[i].GetCoordinate(), agents[j].GetCoordinate(), 1)
            if table[i][j] == -1:
                pygame.draw.line(screen, blocked, agents[i].GetCoordinate(), agents[j].GetCoordinate(), 1)
                

