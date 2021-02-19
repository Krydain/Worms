from datetime import datetime

class Timer:

    def __init__(self):
        self.lastTime = datetime.now()

    def restart(self):
        self.lastTime = datetime.now()

    def deltaTime(self):
        currentTime = datetime.now()
        delta = currentTime - self.lastTime
        self.lastTime = currentTime
        return delta.total_seconds()