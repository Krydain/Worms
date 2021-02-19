import random
import pygame
from pygame.locals import *

class Wind:

    def __init__(self, scren):
        self.screen = scren
        self.x = None
        self.y = None
        self.isWindy = False

    def New(self, screen):
        self.isWindy = True
        isMinus1 = 1 if random.random() <= .5 else -1
        isMinus2 = 1 if random.random() < .5 else -1
        self.x = random.random() * 30 * isMinus1
        self.y = random.random() * 30 * isMinus2

    def DrawWind(self):
        pygame.draw.line(self.screen, (255,255,255), (886,55), (self.x + 886, self.y + 55),3) 