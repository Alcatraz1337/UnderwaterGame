from cgi import test
from email.errors import ObsoleteHeaderDefect
from turtle import speed
import pygame
import agent
import random
import sys

# Test screen
pygame.init()
testScreen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Obstacles:
    def __init__(self, rect:tuple, speed:list) -> None:
        self.rect = pygame.Rect(rect) # Coordinate can also be found by rect
        self.color = 102, 51, 51
        self.speed = speed

    def Move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])

    def RandomSpeed(self):
        self.speed[0] = random.randint(2, 8)
        self.speed[1] = random.randint(2, 8)

    def CheckCollisionWithScreen(self, screen:pygame.Surface):
        if(self.rect.left < 0 or self.rect.right > screen.get_rect().right):
            self.speed[0] = -self.speed[0]
        if(self.rect.top < 0 or self.rect.bottom > screen.get_rect().bottom):
            self.speed[1] = -self.speed[1]

    def CheckCollisionWithAgents(self, Agents:list):
        index = self.rect.collidelist(Agents)
        if index >=0 :
            temp_obs = Obstacles(self.rect, self.speed)
            while temp_obs.rect.colliderect(Agents[index].rect):
                if temp_obs.speed[1] * self.speed[1] > 0:
                    temp_obs.speed[0] = self.speed[0]
                    temp_obs.speed[1] = -self.speed[1]
                else:
                    temp_obs.speed[0] = -self.speed[0]
                    temp_obs.speed[1] = self.speed[1]
                temp_obs.rect = temp_obs.rect.move(temp_obs.speed)
            if temp_obs.speed[0] * self.speed[0] > 0:
                self.speed[1] = -self.speed[1]
            else:
                self.speed[0] = -self.speed[0]

    def DrawObstacle(self, screen:pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
            

# Test Agent and test screen display
a = agent.Agent([200, 25], 5, testScreen)
o = Obstacles((50, 50, 120, 90), [3, 2])
A = []
A.append(a)

while 1:
    timeDelta = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    o.Move()
    o.CheckCollisionWithAgents(A)
    o.CheckCollisionWithScreen(testScreen)
    #Update screen
    testScreen.fill((0,0,0))
    agent.DrawAgent(a, testScreen)
    aRect = a.GetRect()
    o.DrawObstacle(testScreen)
    pygame.display.update()