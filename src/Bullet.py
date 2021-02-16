from Vector2 import Vector2
import math

class Bullet:
    Vo = None
    alpha = None
    timeSinceBegin = None
    posInit = Vector2(0,0)
    image = None
    isInMotion = False
    position = None
    isRightDirection = None

    def __init__(self, vo, alphaa, posinit, direction):
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
        self.position.y = -(1/2) * -9.81 * math.pow(-self.timeSinceBegin,2) + self.Vo * math.sin(self.alpha) * -self.timeSinceBegin + self.posInit.y
            
        if self.position.y > 300:
            print("Under boom")