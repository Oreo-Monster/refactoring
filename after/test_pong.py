import turtle
from ball import Ball
from window import GameWindow
from pong import Pong
import os
import matplotlib
matplotlib.use('TkAgg')
def test_ball():
    pong = Pong()
    ball = pong.ball
    assert ball.getPos() == {'x': 0, 'y': 0}
    ball.move()
    assert ball.getPos() == {'x': 0.0925, 'y': 0.0925}
    ball.move()
    assert ball.getPos() == {'x': 0.185, 'y': 0.185}
    ball.reset()
    assert ball.getPos() == {'x': 0, 'y': 0}
    assert ball.vel['x'] == -0.0925
    ball.ybounds = {'min':-290, 'max':-80}
    ball.checkCollision()
    assert ball.getPos() == {'x': 0, 'y': -80}
    assert ball.vel == {'x': -0.0925, 'y': -0.0925}
    ball.ybounds = {'min':80, 'max':290}
    ball.checkCollision()
    assert ball.getPos() == {'x': 0, 'y': 80}
    assert ball.vel == {'x': -0.0925, 'y': 0.0925}

def test_window():
    pong = Pong()
    window = pong.window
    assert window.window.canvwidth == 400
    assert window.window.canvheight == 300
    assert window.turt.get_shapepoly() == ((10.0, -10.0), (10.0, 10.0), (-10.0, 10.0), (-10.0, -10.0))
    assert window.turt.pos() == (0.00, 260.00)
    window.goto({'x':200, 'y':200})
    assert window.turt.pos() == (200.00, 200.00)

def test_paddle():
    pong = Pong()
    paddle = pong.paddle_1
    assert paddle.getPos() == {'x': -350, 'y': 0}
    paddle.up()
    assert paddle.getPos() == {'x': -350, 'y': 20}
    paddle.down()
    assert paddle.getPos() == {'x': -350, 'y': 0}
    
def test_paddle_ball_collision():
    pong = Pong()
    paddle = pong.paddle_1
    ball = pong.ball
    ball.setPos({'x':-345, 'y':0})
    assert ball.vel == {'x': -0.0925, 'y': 0.0925}
    ball.checkPaddleCollision([paddle])
    assert ball.getPos() == {'x': -345, 'y': 0}
    assert ball.vel == {'x': 0.0925*1.5, 'y': 0.0925}
    ball.setPos({'x':-350, 'y':50})
    ball.checkPaddleCollision([paddle])
    assert ball.getPos() == {'x': -350, 'y': 50}
    assert ball.vel == {'x': 0.0925*1.5, 'y': 0.0925}
    ball.setPos({'x':-250, 'y':0})
    ball.checkPaddleCollision([paddle])
    assert ball.getPos() == {'x': -250, 'y': 0}
    assert ball.vel == {'x': 0.0925*1.5, 'y': 0.0925}
    ball.setPos({'x':350, 'y':0})
    ball.checkPaddleCollision([paddle])
    assert ball.getPos() == {'x': 350, 'y': 0}
    assert ball.vel == {'x': 0.0925*1.5, 'y': 0.0925}

def test_score():
    pong = Pong()
    score = pong.score
    ball = pong.ball
    ball.setPos({'x':-360, 'y':0})
    pong.checkForScore()
    assert score.score == {'p1': 0, 'p2': 1}
    assert ball.getPos() == {'x': 0, 'y': 0}
    ball.setPos({'x':360, 'y':0})
    pong.checkForScore()
    assert score.score == {'p1': 1, 'p2': 1}
    assert ball.getPos() == {'x': 0, 'y': 0}
