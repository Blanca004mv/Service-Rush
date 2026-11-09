import pyxel
from constants import SPRITES, ITEM_SIZE, RECIPES

class Dish:
    def __init__(self, recipe_name: str, ingredients: list, is_clean: bool = True):
        self.recipe_name = recipe_name
        if ingredients is None:
            self.ingredients =[]
        else: 
            self.ingredients = ingredients
        self.is_clean = is_clean

    # Recipe name property
    @property
    def recipe_name(self) -> str:
        return self.__recipe_name

    # Recipe name setter
    def recipe_name(self, value: str):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError("Recipe name must be a string or None.")
            val_upper = value.upper()
            if val_upper not in RECIPES:
                raise ValueError(f"Invalid recipe '{value}'. Valid options: {list(RECIPES.keys())}")
            self.__recipe_name = val_upper
        else:
            self.__recipe_name = None

    # Ingredients property
    @property
    def ingredients(self) -> list:
        return self.__ingredients

    # Ingredients setter
    @ingredients.setter
    def ingredients(self, value: list):
        if not isinstance(value, list):
            raise TypeError("Ingredients must be a list.")
        self.__ingredients = value

    # Is clean property
    @property
    def is_clean(self)->bool:
        return self.__is_clean

    # Is clean setter
    @is_clean.setter
    def is_clean(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Is clean must be a boolean.")
        self.__is_clean = value

    # Check if the dish has no ingredients and name
    def is_empty(self) -> bool:
        return len(self.__ingredients) == 0 and self.__recipe_name is None

    def add_ingredient(self, ingredient_name: str):
        if not isinstance(ingredient_name, str):
            raise TypeError("Ingredient name must be a string.")
        self.__ingredients.append(ingredient_name)

    def clear(self):
        self.__ingredients.clear()
        self.__recipe_name = None

    def draw(self, x: int, y: int):
        if not self.is_clean:
            u, v = SPRITES.get("dish_dirty", (80, 48))
        elif self.recipe_name is not None:
            recipe_key = self.recipe_name.lower()
            u, v = SPRITES.get(recipe_key, SPRITES["dish_empty"])
        else:
            u, v = SPRITES["dish_empty"]

        pyxel.blt(x, y, 0, u, v, ITEM_SIZE, ITEM_SIZE, 0)

    