import pygame
from pygame.locals import *
from StateGame import StateGame, State

class UI:

    def __init__(self, screen, teams, stateGame):
        self.screen = screen
        self.teams = teams
        self.stateGame = stateGame
        self.bulletType1 = pygame.image.load("../Images/GrenadeGame.png").convert_alpha()

        self.bulletType2 = pygame.image.load("../Images/RoquetteGame.png").convert_alpha()


    def Draw(self, isType1):
        if self.teams.teamTurn %2:
            pygame.draw.circle(self.screen, (0,0,255), (15,15), 10)
        else:
            pygame.draw.circle(self.screen, (255,0,0), (15,15), 10)

        if self.stateGame.state == State.WaitPlayerToSpace:
            pygame.draw.circle(self.screen, (0,0,0), (15,15), 7)

        if isType1:
            self.screen.blit(self.bulletType1, (35,9)) 
        else: 
            self.screen.blit(self.bulletType2, (35,10)) 