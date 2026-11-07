import pyxel
from constants import BOARD_HEIGHT, CHEF_SPRITES

class Chef:
    def __init__(self, chef_id, start_col, start_row):
        self.chef_id = chef_id
        self.col = start_col
        self.row = start_row
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
        # Check if value taking account the chef id
        if self.chef_id == 1:
            if not (1 <= value <= 3):
                raise ValueError("Row for Chef 1 must be between 1 and 3.")
        if self.chef_id == 2:
            if not (5 <= value <= 7):
                raise ValueError("Row for Chef 2 must be between 5 and 7.")
        self.__row = value

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
        x = self.col * 16
        y = BOARD_HEIGHT + (self.row * 16)  

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
            w = -16
        else:
            w = 16

        pyxel.blt(x, y, 0, u, v, w, 16, 0)