from Timer import Timer

class TimerBullet:
    timer = None
    bullet = None
    delay = 0.0
    timePassed = 0.0

    def __init__(self):
        self.timer = Timer()

    def Add(self, bullett, delayy):
        self.bullet = bullett
        self.delayy = delayy
        self.timePassed = 0.0
        self.timer.deltaTime()

    def Update(self):
        if self.bullet != None:
            self.timePassed = self.timePassed + self.timer.deltaTime()
            if self.timePassed > self.delay:
                self.Explode()

    def Explode(self):
        # for each player bam bam bam
        izi = 1