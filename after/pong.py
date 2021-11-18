from paddle import Paddle
from ball import Ball
from window import GameWindow
from scoreboard import Scoreboard

class Pong:

    def __init__(self):
        self.window = GameWindow("Pong - A CS151 Reproduction!", "black", {'width':800, 'height':600})
        self.setUpPaddles()
        self.setUpBall()
        self.setUpScoreboard()
        keyBinds = {
            "w": self.paddle_1.up,
            "s": self.paddle_1.down,
            "Up": self.paddle_2.up,
            "Down": self.paddle_2.down
        }
        self.window.setupKeys(keyBinds)
        self.window.update()
        self.window.listen()
        


    def setUpPaddles(self):
        paddle1Pos = {"x": -350, "y": 0}
        paddleTurt = self.window.make_turtle(shape = 'square', stretch={'width':1, 'height':5}, color='white', pos=paddle1Pos)
        self.paddle_1 = Paddle(paddleTurt, paddle1Pos)
        paddle2Pos = {"x": 350, "y": 0}
        paddleTurt = self.window.make_turtle(shape = 'square', stretch={'width':1, 'height':5}, color='white', pos=paddle2Pos)
        self.paddle_2 = Paddle(paddleTurt, paddle2Pos)

    def setUpBall(self):
        ballTurt = self.window.make_turtle(shape='square', stretch={'width':1, 'height':1}, color='white', pos={'x':0, 'y':0})
        self.ball = Ball(ballTurt)

    def setUpScoreboard(self):
        scoreTurt = self.window.make_turtle(shape='square', stretch={'width':1, 'height':1}, color='white', pos={'x':0, 'y':260})
        self.score = Scoreboard(scoreTurt)
        self.score.draw()

    def gameLoop(self):
        
        while True:
            self.window.listen()
            self.window.update()
            self.ball.move()
            self.checkForScore()
            self.ball.checkPaddleCollision([self.paddle_1, self.paddle_2])
    
    
    def checkForScore(self):
        x = self.ball.getPos()['x']
        if  x > 350:
            self.score.increment('p1')
            self.ball.reset()
        elif x < -350:
            self.score.increment('p2')
            self.ball.reset()
            