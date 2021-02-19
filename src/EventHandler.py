import pygame
from pygame.locals import *
from Vector2 import Vector2
from Teams import Teams
from StateGame import State, StateGame
from Trajectory import Trajectory

class EventHandler:
    
    def __init__(self, world):
        x, y = pygame.mouse.get_pos()
        self.mousePosition = Vector2(x,y)
        self.teams = world.teams
        self.stateGame = world.stateGame
        self.world = world

        self.z = False
        self.q = False
        self.s = False
        self.d = False
        self.space = False

        self.leftMouse = False
        self.rightMouse = False
        self.middleMouse = False

    characterCanMove = False

    def KeyEvent(self, key, action):
        if key == pygame.K_z:
            self.z = action
        elif key == pygame.K_q:
            self.q = action
        elif key == pygame.K_s:
            self.s = action
        elif key == pygame.K_d:
            self.d = action
        elif key == pygame.K_SPACE:
            self.space = action

    def MouseMotion(self):
        izi = 1

    def MouseUp(self, btn):
        if btn == 1: # left click
            self.leftMouse = False
        elif btn == 3: # right click
            self.rightMouse = False
            print("Right click up")

    def MouseDown(self,btn):
        if btn == 1: # left click
            self.leftMouse = True
        elif btn == 3: # right click
            self.rightMouse = True
            print("Right click down")

    def GetEvents(self):
    # 8 - loop through the events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.KeyEvent(event.key,True)
            elif event.type == pygame.KEYUP:
                self.KeyEvent(event.key,False)
            elif event.type == pygame.MOUSEMOTION:
                self.MouseMotion()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.MouseUp(event.button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.MouseDown(event.button)
            elif event.type == pygame.MOUSEWHEEL:
                self.middleMouse = event.y + self.middleMouse
            elif event.type == pygame.QUIT:
                self.QuitGame()
            
    def ProcessEvents(self):
        self.ProcessKey()
        self.ProcessMouse()

    def ProcessKey(self):
        if self.stateGame.state == State.WaitPlayerToSpace:
            if self.space:
                self.stateGame.state = State.WaitPlayer

        elif self.stateGame.CanIMove():
            if self.q ^ self.d: # XOR
                direction = -1 if self.q else 1
                self.teams.actualCharacter.SetMove(12 * direction,0)

    def ProcessMouse(self):
        if (self.stateGame.state == State.InGame or self.stateGame.state == State.WaitPlayer) and self.leftMouse:
            if self.stateGame.CanIAim():
                self.world.trajectory = Trajectory(self.world)
        elif self.stateGame.state == State.InClickForShoot and self.rightMouse:
            if not(self.stateGame.AskToReturnInGame()):
                self.world.trajectory = None
            else:
                self.world.trajectory = None
                self.leftMouse = False
        elif self.stateGame.state == State.InClickForShoot and not(self.leftMouse):
            if(self.stateGame.GetTimeTurn() < 3):
                self.world.LoadBullet()
                self.stateGame.state = State.WaitBullet
            else:
                self.world.trajectory = None
                self.stateGame.state = State.WaitPlayerToSpace
                self.teams.Next()

        if self.stateGame.state != State.WaitBullet and self.middleMouse % 2 != 0:
            self.world.SwitchBulletType()

        self.middleMouse = 0


    def QuitGame(self):
        pygame.quit() 
        exit(0)