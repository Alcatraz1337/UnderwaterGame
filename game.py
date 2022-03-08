import sys
import pygame
import agent

pygame.init()

# Game properties
size = width, height = 400, 400
speed = [1, 1]

# Color definition
black = 0,0,0
white = 255,255,255
available = 128,128,128 
connected = 60,142,100
blocked = 236,19,22

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

# Set agents properties
ball1, ball2, ball3, ball4, ball5 = [200, 25], [34,146], [88,312], [312,312], [366,146]
radius = 5
ball1rect = pygame.draw.circle(screen, white, ball1, radius)
ball2rect = pygame.draw.circle(screen, white, ball2, radius)
ball3rect = pygame.draw.circle(screen, white, ball3, radius)
ball4rect = pygame.draw.circle(screen, white, ball4, radius)
ball5rect = pygame.draw.circle(screen, white, ball5, radius)

# Set obstacles properties

def DrawAgents():
    pygame.draw.circle(screen, white, ball1, radius)
    pygame.draw.circle(screen, white, ball2, radius)
    pygame.draw.circle(screen, white, ball3, radius)
    pygame.draw.circle(screen, white, ball4, radius)
    pygame.draw.circle(screen, white, ball5, radius)

while 1:
    timeDelta = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Update screen
    screen.fill(black)
    DrawAgents()
    pygame.display.update()