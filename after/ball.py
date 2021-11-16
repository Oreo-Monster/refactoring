
import turtle

class Ball:
    # implements a Pong game ball

    def __init__(self, turtle, vel={'x':.0925, 'y':.0925},pos={'x':0, 'y':0}, ybounds={'min':-290, 'max':290}):
        ''' intializes a ball with default direction and position '''
        self.turt = turtle
        self.vel = vel
        self.pos = pos
        self.ybounds = ybounds

    def move(self):
        ''' moves the ball in x and y directions '''
        self.updatePos()
        self.checkCollision()

    def checkCollision(self):
        if self.pos['y'] > self.ybounds['max']:
            self.pos['y'] = self.ybounds['max']
            self.vel['y'] *= -1
        if self.pos['y'] < self.ybounds['min']:
            self.pos['y'] = self.ybounds['min']
            self.vel['y'] *= -1

    def updatePos(self):
        ''' moves ball to new x, y positions '''
        self.pos={'x':self.pos['x']+self.vel['x'], 'y':self.pos['y']+self.vel['y']}
        self.turt.goto(self.pos['x'], self.pos['y'])


    def setPos(self, pos):
        ''' sets ball position '''
        self.pos = pos
        self.turt.goto(self.pos['x'], self.pos['y'])

    def getPos(self):
        return self.pos