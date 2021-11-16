import turtle

class Paddle:
    # implements a Pong game paddle

    def __init__(self, pos):
        # store pos as a dictionary
        ''' initializes a paddle with a position '''

        self.pos = pos

        self.turt = make_turtle("square", "white", 5, 1, self.x_position, self.y_position)


    def up(self):
        y = self.turt.ycor()
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        y = self.turt.ycor() #Get the current y coordinate
        y -= 20             #add 20px could also be y=y+20
        self.turt.sety(y)    #move the paddle to the new y position
        self.y_position = y


    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()

