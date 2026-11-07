import pyxel
from constants import BOARD_HEIGHT, SPRITES

class Pan:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.content = None

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

    # COntent property
    @property
    def content(self):
        return self.__content

    # Content setter
    @content.setter
    def content(self, value):
        # Check if the value is either None or a list of strings
        if value is not None and (not isinstance(value, list) or not all(isinstance(item, str) for item in value)):
            raise ValueError("Content must be either None or a list of strings.")
        self.__content = value

    def draw(self):
        x = self.col * 16
        y = BOARD_HEIGHT + (self.row * 16)


        # Draw pan
        u, v = SPRITES["pan"]
        pyxel.blt(x, y, 0, u, v, 16, 16, 0)