import pyxel
from constants import BOARD_HEIGHT, SPRITES, VALID_INGREDIENTS, VALID_STATES


class Ingredient:

    def __init__(self, col, row, name, state = "raw"):
        self.col = col
        self.row = row
        self.name = name
        self.state = state
    
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
    
    # Name property
    @property
    def name(self) -> str:
        return self.__name

    # Name setter
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Ingredient name must be a string.")
        val_lower = value.lower()
        if val_lower not in VALID_INGREDIENTS:
            raise ValueError(f"Invalid ingredient name: '{value}'. Valid options: {VALID_INGREDIENTS}")
        self.__name = val_lower

    # State property
    @property
    def state(self) -> str:
        return self.__state

    # State setter
    @state.setter
    def state(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Ingredient state must be a string.")
        val_lower = value.lower()
        if val_lower not in VALID_STATES:
            raise ValueError(f"Invalid ingredient state: '{value}'. Valid options: {VALID_STATES}")
        self.__state = val_lower

    def chop(self):
        if self.name == "egg":
            return
        if self.state == "raw":
            self.state = "chopped"

    def draw(self):
        x = self.col * 16
        y = BOARD_HEIGHT + (self.row * 16)

        # Draw worktop
        u_w, v_w = SPRITES["worktop"]
        pyxel.blt(x, y, 0, u_w, v_w, 16, 16, 0)

        # Draw ingredient
        if self.state == "chopped":
            sprite_key = f"{self.name}_chopped"
        else:
            sprite_key = self.name

        if sprite_key in SPRITES:
            u, v = SPRITES[sprite_key]
            pyxel.blt(x, y, 0, u, v, 16, 16, 0)