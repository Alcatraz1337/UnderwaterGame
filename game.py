import sys
import pygame
import Agent as ag
import Obstacles as ob
import GameManager as gm
import numpy as np
import random


pygame.init()

# Game properties
size = width, height = 400, 400
speed = [1, 1]

# Color definition
black = 0,0,0
white = 255,255,255

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

# Test Agent and test screen display
a0 = ag.Agent([200, 25], 5, screen)
a1 = ag.Agent([34, 146], 5, screen)
a2 = ag.Agent([98, 341], 5, screen)
a3 = ag.Agent([302, 341], 5, screen)
a4 = ag.Agent([366, 146], 5, screen)
o0 = ob.Obstacles((50, 50, 50, 33), [random.randint(2,8), random.randint(2,8)])
o1 = ob.Obstacles((230, 200, 45, 33), [random.randint(3,8), random.randint(3,8)])
A = []
O = []
A.append(a0)
A.append(a1)
A.append(a2)
A.append(a3)
A.append(a4)
O.append(o0)
O.append(o1)

linkTable = np.zeros([len(A), len(A)])
linkTable[1][3] = 1
linkTable[3][4] = -1

while 1:
    timeDelta = clock.tick(33)
    i:ob.Obstacles
    j:ag.Agent
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    for i in O:
        i.Move()
        i.CheckCollisionWithAgents(A)
        i.CheckCollisionWithScreen(screen)

    screen.fill(black)
    for j in A:
        j.DrawAgent(screen)
    
    for i in O:
        i.DrawObstacle(screen)
    gm.DrawConnection(linkTable, A, screen)
    
    pygame.display.update()
    

    # o1.Move()
    # o1.CheckCollisionWithAgents(A)
    # o1.CheckCollisionWithScreen(screen)
    # #Update screen
    # screen.fill((0,0,0))
    # A[0].DrawAgent(screen)
    # aRect = a.GetRect()
    # o.DrawObstacle(screen)
    # pygame.display.update()