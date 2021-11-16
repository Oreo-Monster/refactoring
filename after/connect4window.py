from window import GameWindow

class Connect4Window(GameWindow):
    def __init__(self, on_click, grid, name="Connect 4", color="light sky blue", shape={'width':800, 'height':600}):
        super().__init__(name, color, shape)
        self.window.onclick(on_click)
        self.grid = grid


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
                