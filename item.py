from constants import (
    BOARD_HEIGHT, ITEM_SIZE, MAX_COLUMNS, MIN_COLUMNS, MAX_ROWS, MIN_ROWS
)

class Item:
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
        if not (MIN_COLUMNS <= value <= MAX_COLUMNS):
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
        if not (MIN_ROWS <= value <= MAX_ROWS):
            raise ValueError("Row must be between 0 and 8.")
        self.__row = value

    # x property
    @property
    def x(self) -> int:
        return self.col * ITEM_SIZE

    # y property
    @property
    def y(self) -> int:
        return BOARD_HEIGHT + (self.row * ITEM_SIZE)