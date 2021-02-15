import math
from Vector2 import Vector2

class MathG:
    @staticmethod
    def ApplyGravity(solf, delta):
        if(not(solf.isGravity) and (solf.position.x < 15 or solf.position.x > 883)):
                solf.isGravity = True

        if solf.isGravity:
            solf.position.y += delta * (solf.velocity.y + delta * solf.delta / 2)
            solf.velocity.y += solf.timestep * solf.acceleration.y

    @staticmethod
    def GetAngleTwoVectors(v1, v2):
        angle = math.acos((v1.x * v2.x + v1.y * v2.y) / (math.sqrt(math.pow(v1.x,2) + math.pow(v1.y,2)) * math.sqrt(math.pow(v2.x,2) + math.pow(v2.y,2))))
        return angle

    @staticmethod
    def CreateVector2From2Points(v1,v2):
        return Vector2(abs(v1.x - v2.x),abs(v1.y - v2.y))