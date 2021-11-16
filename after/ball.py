
import turtle

class Ball:
    # implements a Pong game ball

    def __init__(self, turtle, vel={'x':.0925, 'y':.0925},pos={'x':0, 'y':0}, ybounds={'min':-290, 'max':290}):
        ''' intializes a ball with default direction and position '''
        self.turt = turtle
        self.vel = vel
        self.startingVel = vel.copy()
        self.pos = pos
        self.ybounds = ybounds

    def move(self):
        ''' moves the ball in x and y directions '''
        self.updatePos()
        self.checkCollision()

    def reset(self):
        self.pos = {'x':0, 'y':0}
        currentVel = self.vel['x']
        self.vel['x'] = -(currentVel/abs(currentVel)) *  self.startingVel['x']
        
    def checkCollision(self):
        if self.pos['y'] > self.ybounds['max']:
            self.pos['y'] = self.ybounds['max']
            self.vel['y'] *= -1
        if self.pos['y'] < self.ybounds['min']:
            self.pos['y'] = self.ybounds['min']
            self.vel['y'] *= -1
        
    def checkPaddleCollision(self, paddles):
        for paddle in paddles:
            ballPosX = abs(self.getPos()['x'])
            ballPosY = self.getPos()['y']
            paddlePosX = abs(paddle.getPos()['x'])
            paddlePosY = paddle.getPos()['y']
            if ballPosX > paddlePosX-10\
            and ballPosX < paddlePosX\
            and ballPosY < paddlePosY+50\
            and ballPosY > paddlePosY-50\
            and self.pos['x']*paddle.getPos()['x'] > 0:
                self.pos['x'] = self.getPos()['x']
                self.vel['x'] *= -1.5

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