import pygame
from pygame.locals import *
from Vector2 import Vector2
from Teams import Teams
from StateGame import State, StateGame

class EventHandler:
    z = False
    q = False
    s = False
    d = False
    space = False

    leftMouse = False
    rightMouse = False

    characterCanMove = False

    teams = None
    stateGame = None
    mousePosition = None

    def __init__(self, team, stategame):
        x, y = pygame.mouse.get_pos()
        self.mousePosition = Vector2(x,y)
        self.teams = team
        self.stateGame = stategame

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
            elif event.type == pygame.QUIT:
                self.QuitGame()
            
    def ProcessEvents(self):
        self.ProcessKey()
        self.ProcessMouse()
        self.ResetInputs()

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
                traj = "yes"
            # Trajectory create
        elif self.stateGame.state == State.InClickForShoot and self.rightMouse:
            if not(self.stateGame.AskToReturnInGame()):
                izi = 1
                # Trajectory destroy

        elif self.stateGame.state == State.InClickForShoot and not(self.leftMouse):
            # Shoot
            self.stateGame.state = State.WaitBullet


    def ResetInputs(self):
        self.z = False
        self.q = False
        self.s = False
        self.d = False
        self.space = False

        self.leftMouse = False
        self.rightMouse = False

    def QuitGame(self):
        pygame.quit() 
        exit(0)