

class Pipe:

    def __init__(self, x, y, gap):
        self.gap = gap # Default gap

        # Coordinates for gap
        self.gapX = x
        self.gapY = y

        self.width = 30
        self.height = self.gap

    def update(self):

        self.gapX -= 10

    def getPos(self):
        # Returns the gap position
        return self.gapX, self.gapY, self.gap

    def setX(self, x):
        self.gapX = x

    def setY(self, y):
        self.gapY = y


