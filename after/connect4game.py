from grid import Grid
from connect4window import Connect4Window

class Connect4Game:
    def __init__(self):
        self.grid = Grid()
        self.window = Connect4Window(self.play, self.grid)
        self.window.make_turtle()
        self.window.draw_grid()
        self.turn = 1
        self.gameOver = False
        
    
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
        diagonals = self.grid.getDiagonal()
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
            self.gameOver = True

        self.switchTurn()


    def gameLoop(self):
        while not self.gameOver:
            self.window.draw_grid()
            self.window.update()
            self.window.listen()