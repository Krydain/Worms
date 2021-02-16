from Vector2 import Vector2

class Character:
    image = None
    position = None
    move = Vector2(0,0)
    radius = None
    rotation = None
    physic = None
    isGravity = False
    life = None

    def __init__(self):
        self.position = Vector2(0,0)
        self.life = 100

    def SetMove(self,x,y):
        self.move.x = x
        self.move.y = y

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