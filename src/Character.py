from Vector2 import Vector2

class Character:
    image = None
    
    radius = None
    rotation = None
    physic = None
    isGravity = False
    characterId = None
    

    def __init__(self, idd):
        self.position = Vector2(0,0)
        self.life = 100
        self.characterId = idd
        self.move = Vector2(0,0)


    def __eq__(self, other):
        assert isinstance(other, Character)
        return self.characterId == other.characterId

    def SetMove(self,x,y):
        self.move.x = self.move.x + x
        self.move.y = self.move.y + y

    def Move(self,delta):
        self.position.x = self.position.x + self.move.x * delta
        self.position.y = self.position.y + self.move.y * delta
        self.move.x = 0
        self.move.y = 0

        Vector2.ApplyGravity(self,delta)

    def GetMiddlePosition(self):
        XPos = self.image.get_width()
        YPos = self.image.get_height()
        XPos = XPos / 2
        YPos = YPos / 2

        XPos = XPos + self.position.x
        YPos = YPos + self.position.y

        return (XPos, YPos)