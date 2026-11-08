import pyxel
from constants import (
    RECIPES, FPS, SPRITES, TICKET_WIDTH, TICKET_HEIGHT, TICKET_BG_COLOR, 
    TICKET_TEXT_COLOR_NORMAL, TICKET_TEXT_COLOR_URGENT, TICKET_CRITICAL_TIME_SEC, 
    DISH_X_SPACING, DISH_Y_SPACING, SECONDS_LEFT_X_SPACING, SECONDS_LEFT_Y_SPACING,
    INGREDIENT_SEPARATION, INGREDIENT_X_SPACING, INGREDIENT_Y_SPACING, INGREDIENTE_SCALE,
    ITEM_SIZE
)


class Order():
    def __init__(self, recipe_name: str):
        """Inicializa la orden delegando las validaciones a sus setters."""
        self.recipe_name = recipe_name
        
        time_limit_sec = RECIPES[self.recipe_name]["time_limit"]
        
        self.timer_frames = time_limit_sec * FPS

    # Recipe name property
    @property
    def recipe_name(self) -> str:
        """Getter para el nombre de la receta."""
        return self.__recipe_name

    # Recipe name setter
    @recipe_name.setter
    def recipe_name(self, value: str):
        """Setter con validación de tipo (TypeError) y valor (ValueError)."""
        if not isinstance(value, str):
            raise TypeError("Recipe name must be a string.")
        if value not in RECIPES:
            raise ValueError(f"Invalid recipe: '{value}'. Valid options: {list(RECIPES.keys())}")
        self.__recipe_name = value

    # Timer frames property
    @property
    def timer_frames(self) -> int:
        return self.__timer_frames

    # Timer frames setter
    @timer_frames.setter
    def timer_frames(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Timer frames must be an integer.")
        self.__timer_frames = value

    def update(self):
        if self.__timer_frames > 0:
            self.__timer_frames -= 1

    def is_expired(self) -> bool:
        return self.__timer_frames <= 0

    def draw(self, x: int, y: int):
        
        # Draw ticket
        pyxel.rect(x, y, TICKET_WIDTH, TICKET_HEIGHT, TICKET_BG_COLOR)

        # Draw dish
        recipe_key_sprites = self.recipe_name.lower()
        u, v = SPRITES[recipe_key_sprites]
        pyxel.blt(x + DISH_X_SPACING, y + DISH_Y_SPACING, 0, u, v, ITEM_SIZE, ITEM_SIZE, 0)

        # Draw ingredients
        ingredients_list = RECIPES[self.recipe_name]["ingredients"]
        for idx, ing in enumerate(ingredients_list):
            clean_ing = ing.lower().replace("_chopped", "")
            ing_x = x + INGREDIENT_X_SPACING + (idx * INGREDIENT_SEPARATION)
            ing_y = y + INGREDIENT_Y_SPACING            
            u_ing, v_ing = SPRITES[clean_ing]
            pyxel.blt(ing_x, ing_y, 0, u_ing, v_ing, ITEM_SIZE, ITEM_SIZE, colkey=0, scale=INGREDIENTE_SCALE)

        # Draw seconds left
        seconds_left = max(0, self.__timer_frames // FPS)
        if seconds_left < TICKET_CRITICAL_TIME_SEC:
            text_color = TICKET_TEXT_COLOR_URGENT
        else:
            text_color = TICKET_TEXT_COLOR_NORMAL
        pyxel.text(x + SECONDS_LEFT_X_SPACING, y + SECONDS_LEFT_Y_SPACING, f"{seconds_left}s", text_color)