import math
import pygame
from Bullet import Bullet
from Vector2 import Vector2
from pygame.locals import *


class Trajectory:

    def __init__(self, world):
        self.v0 = None
        self.alpha = None
        self.posIni = None
        self.maxHeight = None
        self.maxWidth = None
        self.isRightDirection = None
        self.world = world
        self.GetPropertiesTrajectory()

    def SetTrajectory(self, V0, alphaa, posInit, direction):
        self.v0 = V0 / 5
        self.alpha = alphaa
        self.posIni = posInit
        self.isRightDirection = direction

        isAbove = self.alpha > 0 and self.alpha < math.pi

        self.maxHeight = (self.v0**2) * (math.sin(alphaa) **
                                         2) / (2*-9.81) * -1 if isAbove else 0
        self.maxWidth = self.v0**2 * \
            math.sin(self.alpha) * math.cos(self.alpha) / - \
            9.81 if isAbove else 0

        if not(self.isRightDirection):
            self.maxWidth = self.maxWidth * -1

    def DrawTrajectory(self):
        if self.alpha > 0 and self.alpha < math.pi:

            for t in range(0, int(abs(self.maxWidth))):
                direction = 1 if self.isRightDirection else -1
                x = int(self.v0 * math.cos(self.alpha)
                        * direction * t + self.posIni.x)
                y = int(-(1/2) * -9.81 * math.pow(-t, 2) + self.v0 *
                        math.sin(self.alpha) * -t + self.posIni.y)
                self.world.screen.set_at((x, y), (255, 255, 255))

            for i in range(-3, 4):
                self.world.screen.set_at(
                    (int(self.posIni.x - self.maxWidth) + i, int(self.posIni.y - self.maxHeight)), (255, 0, 0))

    def GetPropertiesTrajectory(self):
        xMouse, yMouse = pygame.mouse.get_pos()
        xPlayer, yPlayer = self.world.teams.actualCharacter.GetMiddlePosition()
        vMouseToPlayer = Vector2.CreateVector2From2Points(
            Vector2(xMouse, yMouse), Vector2(xPlayer, yPlayer))
        vGroundToPlayer = Vector2.CreateVector2From2Points(
            Vector2(xMouse, 250), Vector2(xPlayer, yPlayer))
        angle = Vector2.GetAngleTwoVectors(vMouseToPlayer, vGroundToPlayer)
        angle = angle * -1 if yMouse >= 250 else angle

        norm = Vector2.GetNormPoints(vMouseToPlayer.x, vMouseToPlayer.y)
        direction = True if xMouse > xPlayer else False

        self.SetTrajectory(norm, angle, Vector2(xPlayer, yPlayer), direction)
