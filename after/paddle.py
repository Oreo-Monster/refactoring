import turtle

class Paddle:
    # implements a Pong game paddle

    def __init__(self, turtle, pos, vel=20):
        # store pos as a dictionary
        ''' initializes a paddle with a position '''
        self.pos = pos
        self.turt = turtle
        self.vel = vel

    def move(self, direction):
        ''' moves the paddle in the direction specified '''
        if direction == 'up':
            self.pos['y'] += self.vel
        elif direction == 'down':
            self.pos['y'] -= self.vel
        self.turt.sety(self.pos['y'])

    def up(self):
        self.move('up')

    def down(self):
        self.move('down')

    def getPos(self):
        return self.pos

