import pyxel
from item import Item
from constants import SPRITES, ITEM_SIZE

class Board(Item):
    def __init__(self, col: int, row: int):
        super().__init__(col, row)

    
    def draw(self):
        u, v = SPRITES["board"]
        pyxel.blt(self.x, self.y, 0, u, v, ITEM_SIZE, ITEM_SIZE)