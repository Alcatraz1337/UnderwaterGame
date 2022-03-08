from multiprocessing import set_forkserver_preload
import pygame

white = 255,255,255

class Agent:
    def __init__(self,coordinate:list, radius:int, surface) -> None:
        self.axis_x = coordinate[0]
        self.axis_y = coordinate[1]
        self.position = coordinate
        self.rect = pygame.draw.circle(surface, white, coordinate, radius)

    def GetCoordinate(self):
        return [self.axis_x, self.axis_y]
    
    def GetRect(self):
        return self.rect
