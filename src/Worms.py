
import os, sys
import pygame
from pygame.locals import *
from datetime import datetime
import time
import math
import random
from Vector2 import Vector2
from Timer import Timer
from MathG import MathG

gravity = -9.81
isResAir = False

class World:

    graphicTimer = None
    objects = []
    physicObjects = []
    backgroundImage = None

    resolutionRef = Vector2(1920,1080) 
    actualResolution = None
    ratioResolution = None

    screen = None

    def __init__(self,x,y,):
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.actualResolution = Vector2(x,y)
        self.ratioResolution = Vector2(self.resolutionRef.x/self.actualResolution.x,self.resolutionRef.y/self.actualResolution.y)
        self.graphicTimer = Timer()
        self.physicTimer = Timer()

    def Start(self):
        self.screen.blit(self.backgroundImage.image,(0,0))
        self.graphicTimer.deltaTime()
        self.physicTimer.deltaTime()

    def UpdateGraphics(self):
        deltaGraphic = self.graphicTimer.deltaTime()
        self.screen.blit(self.backgroundImage.image, (0,0))  
        for obj in self.objects:
            

            if isinstance(obj, Bullet) and obj.isInMotion:
                obj.UpdatePosition(deltaGraphic)
            else:
                obj.Move(deltaGraphic)
                

            self.screen.blit(obj.image, (obj.position.x,obj.position.y))      #draw new player

        if isWind: 
            DrawWind()
        pygame.display.update()


    def Add(self, obj):
        if(obj.physic != None):
            self.physicObjects.append(obj)
        self.objects.append(obj)

    def Remove(self, obj):
        if(obj.physic != None):
            self.physicObjects.remove(obj)
        self.objects.remove(obj)


class Object:
    image = None
    position = None
    move = Vector2(0,0)
    radius = None
    rotation = None
    physic = None
    isGravity = False

    def __init__(self):
        self.position = Vector2(0,0)

    def SetMove(self,x,y):
        self.move.x = x
        self.move.y = y

    def Move(self,delta):
        self.position.x = self.position.x + self.move.x * delta
        self.position.y = self.position.y + self.move.y * delta
        self.move.x = 0
        self.move.y = 0

        MathG.ApplyGravity(self,delta)

    def GetMiddlePosition(self):
        XPos = self.image.get_width()
        YPos = self.image.get_height()
        XPos = XPos / 2
        YPos = YPos / 2

        XPos = XPos + self.position.x
        YPos = YPos + self.position.y

        return (XPos, YPos)

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

class Bullet:
    Vo = None
    alpha = None
    timeSinceBegin = None
    posInit = Vector2(0,0)
    image = None
    isInMotion = False
    position = None
    isRightDirection = None

    def __init__(self, posinit, vo, alphaa, direction):
        self.Vo = vo / 5
        self.alpha = alphaa
        self.timeSinceBegin = 0
        self.posInit = Vector2(posinit.x , posinit.y)
        self.isInMotion = True
        self.position = Vector2(posinit.x , posinit.y)
        self.isRightDirection = 1 if direction else -1

    def UpdatePosition(self, delta):
        self.timeSinceBegin = self.timeSinceBegin + delta
        self.position.x = self.Vo * math.cos(self.alpha) * self.isRightDirection * self.timeSinceBegin + self.posInit.x
        self.position.y = -(1/2) * gravity * math.pow(-self.timeSinceBegin,2) + self.Vo * math.sin(self.alpha) * -self.timeSinceBegin + self.posInit.y
            


        if self.position.y > 300:
            del self

class EventHandler:
    z = False
    q = False
    s = False
    d = False

    mousePosition = None

    def __init__(self):
        x, y = pygame.mouse.get_pos()
        self.mousePosition = Vector2(x,y)

def QuitGame():
    pygame.quit() 
    exit(0)

def KeyEvent(key,action):
    if key == pygame.K_z:
        eventHandler.z = action
    elif key == pygame.K_q:
        eventHandler.q = action
    elif key == pygame.K_s:
        eventHandler.s = action
    elif key == pygame.K_d:
        eventHandler.d = action

def MouseMotion():
    izi = 1

def MouseUp(btn):
    global isResAir
    if btn == 1: # left click
        xMouse, yMouse = pygame.mouse.get_pos()
        print(xMouse)
        print(yMouse)
        xPlayer, yPlayer = player.GetMiddlePosition()
        vMouseToPlayer = MathG.CreateVector2From2Points(Vector2(xMouse, yMouse),Vector2(xPlayer, yPlayer))
        vGroundToPlayer = MathG.CreateVector2From2Points(Vector2(xMouse, 250),Vector2(xPlayer, yPlayer))
        angle = MathG.GetAngleTwoVectors(vMouseToPlayer,vGroundToPlayer)
        angle = angle * -1 if yMouse >= 250 else angle
        #angle = angle * (180/math.pi)
        norm = math.sqrt(math.pow(vMouseToPlayer.x,2) + math.pow(vMouseToPlayer.y,2))
        direction = True if xMouse > xPlayer else False
        LoadBullet(Vector2(xPlayer, yPlayer), norm, angle, direction, True)
        isResAir = not(isResAir)
        #print("Norm " + str(norm))
        #print("Angle " + str(angle))
        #print("Left click up")
    elif btn == 3: # right click
        print("Right click up")


def MouseDown(btn):
    if btn == 1: # left click
        print("Left click down")
    elif btn == 3: # right click
        print("Right click down")

def GetEvents():
# 8 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            KeyEvent(event.key,True)
        elif event.type == pygame.KEYUP:
            KeyEvent(event.key,False)
        elif event.type == pygame.MOUSEMOTION:
            MouseMotion()
        elif event.type == pygame.MOUSEBUTTONUP:
            MouseUp(event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            MouseDown(event.button)
        elif event.type == pygame.QUIT:
            QuitGame()
        
def ProcessEvents():
    if eventHandler.q ^ eventHandler.d: # XOR
        direction = -1 if eventHandler.q else 1
        player.SetMove(12 * direction,0)
    if eventHandler.z:
        player.GetMiddlePosition()
    
def DrawWind():
    pygame.draw.line(world.screen, (255,255,255), (886,55), (wind.x + 886, wind.y + 55),3)            


def LoadPlayer(isEnnemy):
    player = Object()
    player.image = pygame.image.load("../Images/WormsEnnemyModelGame.png").convert_alpha() if isEnnemy else pygame.image.load("../Images/WormsModelGame.png").convert_alpha()
    player.image = pygame.transform.scale(player.image, (25, 38))
    world.objects.append(player)
    return player

def LoadBackground():
    background = Object()
    background.image = pygame.image.load("../Images/BackGroundGame.png")
    background.image = pygame.transform.scale(background.image, (960, 540))
    world.backgroundImage = background

def LoadBullet(posinit, vo, alphaa, direction, isGrenada):
    bullet = Bullet(posinit, vo, alphaa, direction)
    bullet.image = pygame.image.load("../Images/GrenadeGame.png") if isGrenada else pygame.image.load("../Images/RoquetteGame.png")
    bullet.image = pygame.transform.scale(bullet.image, (6, 7))
    world.objects.append(bullet)

def DrawTrajectory(self):
    pygame.draw

world = World(960,540)

eventHandler = EventHandler()

# 3 - Load images
player = LoadPlayer(False)
player.position = Vector2(380,231)
ennemy = LoadPlayer(True)
ennemy.position = Vector2(580,231)
LoadBackground()
bullet = None

actualPlayer = None
isMinus1 = 1 if random.random() <= .5 else -1
isMinus2 = 1 if random.random() < .5 else -1
wind = Vector2(random.random() * 30 * isMinus1, random.random() * 30 * isMinus2)
isWind = False
world.Start()

# 4 - keep looping through
while 1:

    GetEvents()
    ProcessEvents()
    world.UpdateGraphics()
    #print(player.position.x)
    pygame.time.delay(16) 

        


    