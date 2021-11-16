

class Scoreboard:

    def __init__(self, turtle, score={'p1':0, 'p2':0}):
        self.turt = turtle
        self.score = score

    def draw(self):
        self.turt.clear()
        self.turt.write(f"Player A: {self.score['p1']}  Player B: {self.score['p2']}", align="center", font=("Courier", 24, "normal"))
        self.turt.hideturtle()

    def increment(self, player):
        self.score[player] += 1
        self.draw()