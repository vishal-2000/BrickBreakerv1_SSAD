import config

class Brick:
    def __init__(self, strength, x, y):
        self.x = x
        self.y = y
        self.shape = config.BRICK_SHAPE
        self.width = config.BRICK_WIDTH
        self.strength = strength
        self.color = ""
        self.broken = "NO" # implies the brick is not broken yet

    def colorChange(self): # used to decrease color on collision
        if self.color == "RED": 
            self.color = "BLUE"
        elif self.color == "BLUE":
            self.color = "GREEN"
        elif self.color == "GREEN":
            self.color = "NONE" # implies the brick is broken

    def handleCollision(self):
        if self.color == "WHITE" or self.color == "NONE":
            return
        if self.color == "GREEN":
            self.color = "NONE"
        elif self.color == "BLUE":
            self.color = "GREEN"
        elif self.color == "RED":
            self.color = "BLUE"
        self.strength -= 1


class RedBrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, 3, x, y) # strength = 3 # no of collisions required to break the brick
        self.color = "RED"

class BlueBrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, 2, x, y) # strength = 3 # no of collisions required to break the brick
        self.color = "BLUE"

class GreenBrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, 1, x, y) # strength = 3 # no of collisions required to break the brick
        self.color = "GREEN"

class WhiteBrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, -1, x, y) # strength = 3 # no of collisions required to break the brick
        self.color = "WHITE"