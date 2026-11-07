import pyxel

from app import RECIPES 

class Order:
    def __init__(self, recipe_name):
        self.recipe_name = recipe_name
        self.max_timer_frames = RECIPES[self.recipe_name]["time_limit"]
        self.timer_frames = self.max_timer_frames

    # Recipe name property
    @property
    def recipe_name(self):
        return self.__recipe_name

    # Recipe name setter
    @recipe_name.setter
    def recipe_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Recipe name must be a string.")
        if value not in RECIPES:
            raise ValueError(f"Recipe name must be one of {list(RECIPES.keys())}.")
        self.__recipe_name = value

    # Timer frames property
    @property
    def timer_frames(self):
        return self.__timer_frames

    # Timer frames setter
    @timer_frames.setter
    def timer_frames(self, value):
        if not isinstance(value, int):
            raise TypeError("Timer frames must be an integer.")
        if value < 0:
            raise ValueError("Timer frames cannot be negative.")
        self.__timer_frames = value

    # Max timer frames property
    @property
    def max_timer_frames(self):
        return self.__max_timer_frames

    # Max timer frames setter
    @max_timer_frames.setter
    def max_timer_frames(self, value):
        if not isinstance(value, int):
            raise TypeError("Max timer frames must be an integer.")
        if value <= 0:
            raise ValueError("Max timer frames must be positive.")
        self.__max_timer_frames = value

    def update_timer(self):
        if self.timer_frames > 0:
            self.timer_frames -= 1

    
    def is_expired(self) -> bool:
        return self.timer_frames <= 0