from grid import Grid
from window import GameWindow

class Game:
    def __init__(self):
        self.grid = Grid()
        self.window = GameWindow(self.play, self.grid)
        self.window.draw_grid(self.grid)
        self.turn = 1
        self.window.make_turtle()
    
    def check_inline_win(self, fragment):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''
        count = 0
        for i in range(len(fragment)):
            if fragment[i] == self.turn:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    

    def check_win(self):
        ''' checks the winner in the grid
        returns true if player won
        returns false if player lost
        '''

        # check rows
        shape = self.grid.getShape()

        for row in range(shape['row']):
            if self.check_inline_win(self.grid.getRow(row)):
                return True
        

        # check columns
        for col in range(shape['col']):
            if self.check_inline_win(self.grid.getCol(col)):
                return True

        # check diagonal
        diagonals = self.grid.getDiagonals()
        for diag in diagonals:
            if diag.shape[0] >=4:
                if self.check_inline_win(diag):
                    return True

    def switchTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
  
    def play(self, x_pos, y_pos):
        ''' '''
        inds = self.grid.getIndices({'x': x_pos, 'y': y_pos})
        self.window.grid.setTileValue(inds, self.turn)
        self.window.draw_grid()

        if self.check_win(): #Only need to check 
            print(f"player {self.turn} won")

        self.switchTurn()

