import math
import pygame
from pygame.locals import *

class Trajectory:
    v0 = None
    alpha = None
    posIni = None
    maxHeight = None
    maxWidth = None
    isRightDirection = None

    def __init__(self,V0, alphaa, posInit, direction):
        self.v0 = V0 / 5
        self.alpha = alphaa
        self.posIni = posInit
        self.isRightDirection = direction
        isAbove = self.alpha > 0 and self.alpha < math.pi

        self.maxHeight = (self.v0**2) * (math.sin(alphaa)**2) / (2*-9.81) *-1 if isAbove else 0
        self.maxWidth = self.v0**2 * math.sin(self.alpha) * math.cos(self.alpha) / -9.81 if isAbove else 0
    


        if not(self.isRightDirection):
            self.maxWidth = self.maxWidth * -1

    def DrawTrajectory(self, screen):
        if self.alpha > 0 and self.alpha < math.pi:


            for t in range(0, int(abs(self.maxWidth))):
                direction = 1 if self.isRightDirection else -1
                x = int(self.v0 * math.cos(self.alpha) * direction * t + self.posIni.x)
                y = int(-(1/2) * -9.81 * math.pow(-t,2) + self.v0 * math.sin(self.alpha) * -t + self.posIni.y)
                screen.set_at((x,y), (255,255,255))


            screen.set_at((int(self.posIni.x - self.maxWidth), int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) + 1, int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) + 2, int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) + 3, int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) - 1, int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) - 2, int(self.posIni.y - self.maxHeight)), (255,0,0))
            screen.set_at((int(self.posIni.x - self.maxWidth) - 3, int(self.posIni.y - self.maxHeight)), (255,0,0))
