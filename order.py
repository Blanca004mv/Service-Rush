import pyxel
from constants import RECIPES, FPS, SPRITES


class Order:
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
        
        seconds_left = max(0, self.__timer_frames // FPS)

        pyxel.rect(x, y, 38, 24, 7)

        recipe_key_sprites = self.recipe_name.lower()
        if recipe_key_sprites in SPRITES:
            u, v = SPRITES[recipe_key_sprites]
            pyxel.blt(x + 2, y + 4, 0, u, v, 16, 16, 0)
        else:
            # Texto de respaldo solo si la clave no estuviera en SPRITES
            short_name = self.recipe_name[:4].upper()
            pyxel.text(x + 3, y + 4, short_name, 0)

        
        color_texto = 8 if seconds_left < 10 else 0
        pyxel.text(x + 22, y + 10, f"{seconds_left}s", color_texto)