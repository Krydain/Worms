import pygame
from pygame.locals import *
from Vector2 import Vector2
import random
from Character import Character


class Teams:
    blueTeam = []
    redTeam = []

    teamTurn = 1

    world = None
    actualCharacter = Character(0)

    def __init__(self,wrld):
        self.world = wrld
        self.Createteams()
            

    def Createteams(self):
        if len(self.blueTeam) == 0 and len(self.redTeam) == 0:
            for i in range(0,6):
                isEnnemy = False if i%2 == 0 else True
                self.LoadCharacter(i,isEnnemy)
        else:
            print("Teams already created")

                
    def LoadCharacter(self, _id, isEnnemy):
        character = Character(_id)
        character.image = pygame.image.load("../Images/WormsEnnemyModelGame.png").convert_alpha() if isEnnemy else pygame.image.load("../Images/WormsModelGame.png").convert_alpha()
        character.image = pygame.transform.scale(character.image, (25, 38))
        
        self.world.objects.append(character)

        if isEnnemy:
            self.redTeam.append(character)
            character.position = Vector2(random.randint(449, 875),231)
        else:
            self.blueTeam.append(character)
            character.position = Vector2(random.randint(25, 449),231)


    def BeginGame(self):
        if len(self.blueTeam) == 3 and len(self.redTeam) == 3:
            self.Next()

    def Next(self):
        self.teamTurn = self.teamTurn + 1
        self.actualCharacter = None
        if self.teamTurn % 2: #blue team
            self.actualCharacter = self.blueTeam[random.randint(0, len(self.blueTeam) - 1)]
        else: # red team
            self.actualCharacter = self.redTeam[random.randint(0, len(self.redTeam) - 1)]


    def CharacterDied(self, charac):
        if charac in self.blueTeam:
            self.blueTeam.remove(charac)
            self.world.objects.remove(charac)
        elif charac in self.redTeam:
            self.redTeam.remove(charac)
            self.world.objects.remove(charac)
            
    def DoesBulletKill(self,x):
        for charac in self.blueTeam:
            if self.IsInRange(x,charac.position.x):
                self.CharacterDied(charac)

        for charac in self.redTeam:
            if self.IsInRange(x,charac.position.x):
                self.CharacterDied(charac)

        self.WatchTeamWin()

    def WatchTeamWin(self):
        if len(self.blueTeam) == 0 and len(self.blueTeam) == 0:
            print("Exequo")
        elif len(self.blueTeam) == 0:
            print("Red win")
        elif len(self.redTeam) == 0:
            print("Blue win")
        else:
            self.world.Next()

    def IsInRange(self, x1, x2):
        if x1 > x2:
            x = x1 - x2
        else:
            x = x2 - x1

        return x < 15
