import pygame
from pygame.locals import *
from Vector2 import Vector2
import random
from Character import Character


class Teams:
    blueTeam = []
    redTeam = []

    teamTurn = 1

    actualCharacter = Character()

    def __init__(self,wrld):
            self.Createteams(wrld)

    def Createteams(self,wrld):
        if len(self.blueTeam) == 0 and len(self.redTeam) == 0:
            for i in range(0,6):
                isEnnemy = False if i%2 == 0 else True
                self.LoadCharacter(isEnnemy, wrld)
        else:
            print("Teams already created")

                
    def LoadCharacter(self, isEnnemy, wrld):
        character = Character()
        character.image = pygame.image.load("../Images/WormsEnnemyModelGame.png").convert_alpha() if isEnnemy else pygame.image.load("../Images/WormsModelGame.png").convert_alpha()
        character.image = pygame.transform.scale(character.image, (25, 38))
        
        wrld.objects.append(character)

        if isEnnemy:
            self.redTeam.append(character)
            character.position = Vector2(random.randint(449, 875),231)
        else:
            self.blueTeam.append(character)
            character.position = Vector2(random.randint(25, 449),231)


    def BeginGame(self):
        if self.blueTeam == 3 and self.redTeam == 3:
            self.actualCharacter = self.blueTeam[0]

    def Next(self):
        self.teamTurn = self.teamTurn + 1

        if self.teamTurn % 2: #blue team
            print("BlueTeam len : " + str(len(self.blueTeam)))
            self.actualCharacter = self.blueTeam[random.randint(0, len(self.blueTeam))]

        else: # red team
            print("RedTeam len : " + str(len(self.redTeam)))
            self.actualCharacter = self.redTeam[random.randint(0, len(self.redTeam))]


    def CharacterDied(self, charac):
        if charac in self.blueTeam:
            self.blueTeam.remove(charac)
        elif charac in self.redTeam:
            self.redTeam.remove(charac)


    def WatchTeamWin(self):
        if len(self.blueTeam) == 0 and len(self.blueTeam) == 0:
            print("Exequo")
        elif len(self.blueTeam) == 0:
            print("Red win")
        elif len(self.redTeam) == 0:
            print("Blue win")