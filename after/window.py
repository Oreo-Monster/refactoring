import turtle

class GameWindow():
    
    def __init__(self, name, color, shape):
        self.name = name
        self.color = color
        self.shape = shape
        self.window = turtle.Screen()
        self.window.title(name)
        self.window.bgcolor(color)
        self.window.setup(shape['width'], shape['height'])
        self.window.tracer(0)
        self.turt = None

    def update(self):
        self.window.update()
    
    def listen(self):
        self.window.listen()

    def close(self):
        self.window.close()

    def make_turtle(self, shape='classic', color='white', stretch={'width':1, 'height':1}, pos={'x':0, 'y':0}):
        ''' creates a turtle and sets initial position '''

        turt = turtle.Turtle()
        turt.speed(0)    # Speed of animation, 0 is max
        turt.shape(shape)
        turt.color(color)
        turt.shapesize(stretch['height'], stretch['width']) 
        turt.penup()
        turt.goto(pos['x'], pos['y']) # Start position
        self.turt = turt
        return turt

    def goto(self, pos):
        ''' moves the turtle to x, y '''
        self.turt.up()
        self.turt.goto(pos['x'], pos['y'])
        self.turt.down()

    def setupKeys(self, keyBindings={}):
        # value will be function, key will be keyboard key
        for key, func in keyBindings.items():
            print(f'func = {func}\nkey={key}')
            self.window.onkeypress(func, key)
 

        

        