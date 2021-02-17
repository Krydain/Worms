from enum import Enum
from Timer import Timer

class State(Enum):
    Nothing = 0
    Start = 1
    WaitPlayerToSpace = 2
    WaitPlayer = 3
    InGame = 4
    InClickForShoot = 5
    WaitBullet = 6
    HasWin = 7

class StateGame:

    def __init__(self, team):
        self.state = State.WaitPlayerToSpace
        self.timer = Timer()
        self.teams = team
        self.timeTurn = 0

    def StartTurn(self):
        self.timeTurn = 0.0
        self.timer.deltaTime()

    def CanIMove(self):
        if self.state == State.InGame:
            self.timeTurn = self.timeTurn + self.timer.deltaTime()

            if self.timeTurn > 3:
                self.state = State.WaitPlayerToSpace
                self.teams.Next()
                return False
            else:
                return True 
        elif self.state == State.WaitPlayer:
            self.StartTurn()
            self.state = State.InGame
            return True

    def CanIAim(self):
        if self.state == State.InGame:
            self.timeTurn = self.timeTurn + self.timer.deltaTime()

            if self.timeTurn > 3:
                self.state = State.WaitPlayerToSpace
                self.teams.Next()
                return False
            else:
                self.state = State.InClickForShoot
                return True 
        elif self.state == State.WaitPlayer:
            self.StartTurn()
            self.state = State.InClickForShoot
            return True

    def AskToReturnInGame(self):
        self.timeTurn = self.timeTurn + self.timer.deltaTime()
        if self.timeTurn > 3:
            self.state = State.WaitPlayerToSpace
            self.teams.Next()
            return False
        else:
            self.state = State.InGame
            return True 

        
        


