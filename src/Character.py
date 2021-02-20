from Vector2 import Vector2

class Character:
    
    def __init__(self, _id):
        self.position = Vector2(0,0)
        self.life = 100
        self.characterId = _id
        self.move = Vector2(0,0)
        self.velocity = Vector2(0,0)
        self.image = None
        self.imageFocus = None
        self.focus = False
        self.radius = None
        self.rotation = None
        self.physic = None
        self.isGravity = False

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.characterId == other.characterId
        else:
            return False

    def SetMove(self,x,y):
        self.move.x = self.move.x + x
        self.move.y = self.move.y + y

    def Move(self, delta, teams):
        self.position.x = self.position.x + self.move.x * delta
        self.position.y = self.position.y + self.move.y * delta
        self.move.x = 0
        self.move.y = 0

        Vector2.ApplyGravity(self,delta)

        if self.position.y > 540:
            teams.CharacterDied(self)
            teams.WatchTeamWin()

    def GetMiddlePosition(self):
        XPos = self.image.get_width()
        YPos = self.image.get_height()
        XPos = XPos / 2
        YPos = YPos / 2

        XPos = XPos + self.position.x
        YPos = YPos + self.position.y

        return (XPos, YPos)