import os, sys
import pygame
from pygame.locals import *
from datetime import datetime
import time
import math
import random
from Vector2 import Vector2
from Timer import Timer
from Trajectory import Trajectory
from EventHandler import EventHandler
from Bullet import Bullet
from Wind import Wind
from Teams import Teams
from Image import Image
from StateGame import StateGame, State
from UI import UI
from TimerBullet import TimerBullet

gravity = -9.81

class World:

    graphicTimer = None
    objects = []
    physicObjects = []
    backgroundImage = None
    
    bulletType = False
    timerBullet = None
    resolutionRef = Vector2(1920,1080) 
    actualResolution = None
    ratioResolution = None

    trajectory = None

    screen = None

    def __init__(self,x,y,):
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.actualResolution = Vector2(x,y)
        self.ratioResolution = Vector2(self.resolutionRef.x/self.actualResolution.x,self.resolutionRef.y/self.actualResolution.y)
        self.graphicTimer = Timer()
        self.physicTimer = Timer()
        self.bullet = None
        self.wind = Wind(self.screen)
        self.wind.isWindy = True
        self.wind.New(self.screen)
        self.teams = Teams(self)
        self.stateGame = StateGame(self.teams)
        self.eventHandler = EventHandler(self)
        self.ui = UI(self)

    def Start(self):
        self.screen.blit(self.backgroundImage.image,(0,0))
        self.graphicTimer.deltaTime()
        self.physicTimer.deltaTime()

    def UpdateGraphics(self):

        deltaGraphic = self.graphicTimer.deltaTime()
        self.screen.blit(self.backgroundImage.image, (0,0)) 

        for obj in self.objects:
            obj.Move(deltaGraphic,self.teams)
                
            self.screen.blit(obj.image, (obj.position.x,obj.position.y))      #draw new player
        
        if isinstance(self.bullet, Bullet):
            if self.bullet.isInMotion: 
                isTouch = self.bullet.UpdatePosition(deltaGraphic)
                if isTouch is True:
                    delay = 5 if self.bulletType else 0
                    self.timerBullet = TimerBullet(self.bullet, delay, self)
                elif isTouch is False:
                    self.bullet = None
                    self.stateGame.state = State.WaitPlayerToSpace
                    self.teams.Next()


            if self.bullet != None:
                self.screen.blit(self.bullet.image, (self.bullet.position.x,self.bullet.position.y)) 

        if self.trajectory != None:
            self.trajectory.GetPropertiesTrajectory()
            self.trajectory.DrawTrajectory()

        if self.wind.isWindy: 
            self.wind.DrawWind()

        if self.timerBullet != None:
            self.timerBullet.Update()

        self.ui.Draw(self.bulletType)
            
        
    def LoadBullet(self):
        self.trajectory.GetPropertiesTrajectory()
        self.bullet = Bullet(self.trajectory.v0, self.trajectory.alpha, self.trajectory.posIni, self.trajectory.isRightDirection)
        self.bullet.image = pygame.image.load("../Images/GrenadeGame.png") if self.bulletType else pygame.image.load("../Images/RoquetteBulletGame.png")
        self.bullet.image = pygame.transform.scale(self.bullet.image, (6, 7)) if self.bulletType else pygame.transform.scale(self.bullet.image, (6, 7))
        self.trajectory = None


    def SwitchBulletType(self):
        self.bulletType = not(self.bulletType)

    def BulletExplode(self):
        self.timerBullet = None
        xPosition = self.bullet.position.x
        self.teams.DoesBulletKill(xPosition)
        self.bullet = None

    def Next(self):
        self.teams.Next()
        self.stateGame.state = State.WaitPlayerToSpace

    def Add(self, obj):
        if(obj.physic != None):
            self.physicObjects.append(obj)
        self.objects.append(obj)

    def Remove(self, obj):
        if(obj.physic != None):
            self.physicObjects.remove(obj)
        self.objects.remove(obj)

    
        





class Physic:
    acceleration = 0.0
    speed = 0.0
    collider = None
    inMotion = False

    def __init__(self):
        self.collider = Vector2(0,0) # TO CHANGE
    
    def UpdatePhysics(self):
        return None

    def UpdateStateMotion(self):
        if self.speed == 0.0 and self.acceleration == 0.0:
            self.inMotion = False


def LoadBackground():
    background = Image(pygame.image.load("../Images/BackGroundGame.png"))
    background.image = pygame.transform.scale(background.image, (960, 540))
    world.backgroundImage = background


world = World(960,540)

LoadBackground()


world.Start()
world.teams.BeginGame()

# 4 - keep looping through
while 1:

    world.eventHandler.GetEvents()
    world.eventHandler.ProcessEvents()
    world.UpdateGraphics()
    pygame.display.update()
    pygame.time.delay(12) 