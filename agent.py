from imghdr import tests
from imp import source_from_cache
from msilib.schema import Class
import sys
from turtle import screensize
import pygame

# Test screen
# pygame.init()
# testScreen = pygame.display.set_mode((400, 400))
# clock = pygame.time.Clock()

class Agent:
    def __init__(self,coordinate:list, radius:int, surface:pygame.Surface) -> None:
        self.color = 255,255,255
        self.axis_x = coordinate[0]
        self.axis_y = coordinate[1]
        self.radius = 5
        self.position = coordinate
        self.rect = pygame.Rect(coordinate[0] - radius, coordinate[1] - radius, radius * 2, radius * 2)
        self.isConnected = False
        self.hasConnections = 0

    def GetCoordinate(self):
        return [self.axis_x, self.axis_y]
    
    def GetRect(self):
        return self.rect
                      
def DrawAgent(agent:Agent, screen:pygame.Surface):
    pygame.draw.circle(screen, agent.color, agent.GetCoordinate(), agent.radius)

# # Test Agent and test screen display
# a = Agent([200, 25], 5, testScreen)

# while 1:
#     timeDelta = clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     #Update screen
#     testScreen.fill((0,0,0))
#     DrawAgent(a, testScreen)
#     aRect = a.GetRect()
#     print(testScreen.get_rect().y)
#     pygame.display.update()