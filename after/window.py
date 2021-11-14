import turtle

class GameWindow():
    
    def __init__(self, on_click, grid,name="Connect 4", color="light sky blue", shape={'width':800, 'height':600}):
        self.name = name
        self.color = color
        self.shape = shape
        self.window = turtle.Screen()
        self.window.title(name)
        self.window.bgcolor(color)
        self.window.setup(shape['width'], shape['height'])
        self.window.tracer(0)
        self.window.onclick(on_click)
        self.turt = None
        self.grid = grid

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
        turt.shapesize(stretch['width'], stretch['length']) 
        turt.penup()
        turt.goto(pos['x'], pos['y']) # Start position
        self.turt = turt

    def goto(self, pos):
        ''' moves the turtle to x, y '''
        self.turt.up()
        self.turt.goto(pos['x'], pos['y'])
        self.turt.down()

    def draw_grid(self):
        ''' draws a grid at x, y with a specific tile_size '''
        
        offsets = self.grid.getOffsets()
        tileSize = self.grid.getTileSize()
        shape = self.grid.getShape()
        colors = {1: 'red', 2: 'yellow', 0: 'white'}
        self.goto(offsets)

        for row in range(shape['row']):
            for col in range(shape['col']):
                gridValue = self.grid.get({'row': row, 'col': col})
                self.turtle.goto(offsets['x']+ col * tileSize, offsets['y']+row * tileSize)
                self.turt.dot(tileSize-5, colors[gridValue])
                

        

        