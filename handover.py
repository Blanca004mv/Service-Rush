import pyxel
from item import Item
from dish import Dish
from constants import SPRITES, ITEM_SIZE

class Handover(Item):
    def __init__(self, col: int, row: int):
        super().__init__(col, row)
        self.dish = None

    # Dish property
    @property
    def dish(self):
        return self.__dish

    # Dish setter
    @dish.setter
    def dish(self, value):
        if value is not None and not isinstance(value, Dish):
            raise TypeError("The handover object should be Dish or None.")
        self.__dish = value

    def is_empty(self) -> bool:
        return self.__dish is None

    
    def draw(self):
        u, v = SPRITES["handover"]
        pyxel.blt(self.x, self.y, 0, u, v, ITEM_SIZE, ITEM_SIZE)

        # If there is a dish
        if not self.is_empty():
            self.dish.draw(self.x, self.y)