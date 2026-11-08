import pyxel
from item import Item
from constants import BOARD_HEIGHT, SPRITES, VALID_INGREDIENTS, VALID_STATES


class Ingredient(Item):

    def __init__(self, col, row, name, state = "raw"):
        super().__init__(col, row)
        self.name = name
        self.state = state
    
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
        # Draw drawer
        u_w, v_w = SPRITES["drawer"]
        pyxel.blt(self.x, self.y, 0, u_w, v_w, 16, 16, 0)

        # Draw ingredient
        if self.state == "chopped":
            sprite_key = f"{self.name}_chopped"
        else:
            sprite_key = self.name

        if sprite_key in SPRITES:
            u, v = SPRITES[sprite_key]
            pyxel.blt(self.x, self.y, 0, u, v, 16, 16, 0)

        