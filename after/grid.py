import turtle, numpy as np

def __init__(self, shape={'row':5, 'col':7}, offset={'x':-150, 'y':200}, tile_size=50):
    self.grid = np.zeros(shape['row'], shape['col'])
    self.offset = offset
    self.tile_size = tile_size

def get(self, coordinates):
    return self.grid[coordinates['row'], coordinates['col']]

def getTileSize(self):
    return self.tile_size

def getOffsets(self):
    return self.offset

def getShape(self):
    return self.grid.shape