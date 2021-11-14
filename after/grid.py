import turtle, numpy as np

class Grid:
    def __init__(self, shape={'row':5, 'col':7}, offset={'x':-150, 'y':0}, tile_size=50):
        self.grid = np.zeros((shape['row'], shape['col']))
        self.offset = offset
        self.tile_size = tile_size

    def getTileValue(self, coordinates):
        return self.grid[coordinates['row'], coordinates['col']]
    
    def setTileValue(self, coordinates, value):
        self.grid[coordinates['row'], coordinates['col']] = value

    def getTileSize(self):
        return self.tile_size

    def getOffsets(self):
        return self.offset

    def getShape(self):
        return {'row':self.grid.shape[0], 'col':self.grid.shape[1]}

    def getCol(self, col):
        return self.grid[:, col]
    
    def getRow(self, row):
        return self.grid[row, :]

    def getCoordinates(self, indices):
        coordinates = {}
        coordinates['x'] = self.offset['x'] + (indices['col']) * self.tile_size
        coordinates['y'] = self.offset['y'] + (indices['row']) * self.tile_size
        return coordinates
    
    def getDiagonal(self):
        #return every diagonal in the array
        diagonals = []
        for i in range(-(self.grid.shape[0]-1),self.grid.shape[1]):
            diagonals.append(self.grid.diagonal(offset=i))
            diagonals.append(np.fliplr(self.grid).diagonal(offset=i))
        return diagonals
    
    def getIndices(self, pos):
        indices = {}
        indices['col'] = int(abs((pos['x'] - self.offset['x'] - (self.tile_size/2)) // (self.tile_size) + 1))
        indices['row'] = int(abs((pos['y'] - self.offset['y'] - (self.tile_size/2)) // (self.tile_size) + 1))
        return indices