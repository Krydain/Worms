from Timer import Timer

class TimerBullet:
    timer = None
    delay = 0.0
    timePassed = 0.0

    def __init__(self, bullet, delay, world):
        self.timer = Timer()
        self.bullet = bullet
        self.delayy = delay
        self.timePassed = 0.0
        self.timer.deltaTime()
        self.world = world
        
    def Update(self):
        self.timePassed = self.timePassed + self.timer.deltaTime()
        if self.timePassed > self.delay:
            self.Explode()

    def Explode(self):
        self.world.BulletExplode()