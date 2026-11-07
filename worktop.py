import pyxel
from constants import BOARD_HEIGHT, SPRITES

class Worktop:
    def __init__(self, col, row):
        self.col = col
        self.row = row
    
    # Col property
    @property
    def col(self):
        return self.__col
    
    # Col setter
    @col.setter
    def col(self, value:int):
        # Check if its an integer
        if not isinstance(value, int):
            raise ValueError("Column must be an integer.")
        # Check if the value is between 0 and 11
        if not (0 <= value <= 11):
            raise ValueError("Column must be between 0 and 11.")
        self.__col = value
    
    # Row property
    @property
    def row(self):
        return self.__row
    
    # Row setter
    @row.setter
    def row(self, value:int):
        # Check if its an integer
        if not isinstance(value, int):
            raise ValueError("Row must be an integer.")
        # Check if the value is between 0 and 8
        if not (0 <= value <= 8):
            raise ValueError("Row must be between 0 and 8.")
        self.__row = value
    
    def draw(self):
        x = self.col * 16
        y = BOARD_HEIGHT + (self.row * 16)
        u, v = SPRITES["worktop"]
        pyxel.blt(x, y, 0, u, v, 16, 16)