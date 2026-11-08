import pyxel
from item import Item
from constants import BOARD_HEIGHT, CHEF_SPRITES, ITEM_SIZE

class Chef(Item):
    def __init__(self, chef_id:int, col:int, row:int):
        super().__init__(col, row)
        self.chef_id = chef_id
        self.direction = "DOWN"
        self.has_dish = False

    # Chef id property
    @property
    def chef_id(self):
        return self.__chef_id

    #Chef id setter  
    @chef_id.setter
    def chef_id(self, value:int):
        # Check if its an integer
        if not isinstance(value, int):
            raise ValueError("Chef ID must be an integer.")
        # Check if the value is either 1 or 2
        if value not in (1, 2):
            raise ValueError("Chef ID must be either 1 or 2.")
        self.__chef_id = value

    
    # Direction property
    @property
    def direction(self):
        return self.__direction

    # Direction setter
    @direction.setter
    def direction(self, value:str):
        # Check if its a string
        if not isinstance(value, str):
            raise ValueError("Direction must be a string.")
        # Check if the value is one of the allowed directions
        if value not in ("UP", "DOWN", "LEFT", "RIGHT"):
            raise ValueError("Direction must be 'UP', 'DOWN', 'LEFT', or 'RIGHT'.")
        self.__direction = value

    # Has dish property
    @property
    def has_dish(self):
        return self.__has_dish

    # Has dish setter
    @has_dish.setter
    def has_dish(self, value:bool):
        # Check if its a boolean
        if not isinstance(value, bool):
            raise ValueError("Has dish must be a boolean.")
        self.__has_dish = value

    # Draw the chef on the screen
    def draw(self):

        if self.direction == "DOWN":
            if self.has_dish:
                state = "front_plate"
            else:
                state = "front"
        elif self.direction == "UP":
            if self.has_dish:
                state = "back_plate"
            else:
                state = "back"
        else:
            if self.has_dish:
                state = "side_plate"
            else:
                state = "side"

        u, v = CHEF_SPRITES[self.chef_id][state]

        if self.direction == "LEFT":
            w = -ITEM_SIZE
        else:
            w = ITEM_SIZE

        pyxel.blt(self.x, self.y, 0, u, v, w, ITEM_SIZE, 0)