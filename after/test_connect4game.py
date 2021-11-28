from connect4game import Connect4Game
from connect4window import Connect4Window

def test_turn():
    #make sure player turns toggle correctly
    connect4 = Connect4Game()
    assert connect4.turn == 1
    connect4.switchTurn()
    assert connect4.turn == 2
    connect4.switchTurn()
    assert connect4.turn == 1

def test_grid():
    #try setting/verifying color values on grid
    connect4 = Connect4Game()
    assert connect4.grid.getTileValue({'row':0, 'col':0}) == 0
    connect4.grid.setTileValue({'row':0, 'col':0}, 1)
    assert connect4.grid.getTileValue({'row':0, 'col':0}) == 1
    connect4.grid.setTileValue({'row':2, 'col':0}, 2)
    assert connect4.grid.getTileValue({'row':2, 'col':0}) == 2

def test_coordinates():
    #try converting coords to inds
    connect4 = Connect4Game()
    offset = connect4.grid.offset
    tile_size = connect4.grid.tile_size
    shape = connect4.grid.grid.shape
    assert connect4.grid.getRow(3).shape[0] == shape[1]
    assert connect4.grid.getCol(1).shape[0] == shape[0]
    ind = {'row':0, 'col':0}
    coords = connect4.grid.getCoordinates(ind)
    inds = connect4.grid.getIndices(coords)
    assert inds['row'] == ind['row']

def test_wins():
    #check for vertical win
    connect4 = Connect4Game()
    for i in range(0,4):
        connect4.grid.setTileValue({'row':0, 'col':i}, 1)
    assert connect4.check_win()
    #check for horizontal win
    connect4 = Connect4Game()
    for j in range(0,4):
        connect4.grid.setTileValue({'row':j, 'col':0}, 1)
    assert connect4.check_win()
    #check for diagonal win
    connect4 = Connect4Game()
    for k in range(0,4):
        connect4.grid.setTileValue({'row':k, 'col':k}, 1)
    assert connect4.check_win()
    #check backwards diagonal win
    connect4 = Connect4Game()
    for l in range(0,4):
        connect4.grid.setTileValue({'row':l, 'col':3-l}, 1)
    assert connect4.check_win()

def test_inline_wins():
    #non win, 4 in a row
    connect4 = Connect4Game()
    color = 1
    for i in range(0,4):
        if i%2==0:
            color = 2
        connect4.grid.setTileValue({'row':0, 'col':i}, color)
    assert not connect4.check_inline_win(connect4.grid.getRow(0))
    #check with list of 4 in a row
    row1 = [1,1,1,1,0,0,0]
    assert connect4.check_inline_win(row1)
    row2 = [0,0,1,2,2,2,2,1,0]
    connect4.switchTurn()
    assert connect4.check_inline_win(row2)

