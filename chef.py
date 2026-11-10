import pyxel
from dish import Dish
from ingredient import Ingredient
from item import Item
from constants import (
    CHEF_SPRITES, ITEM_SIZE, MAX_COLUMNS, MIN_COLUMNS, CHEF_1_MAX_ROW, CHEF_1_MIN_ROW,
    CHEF_2_MAX_ROW, CHEF_2_MIN_ROW, KITCHEN_LAYOUT, MIN_ROWS, MAX_ROWS
)

class Chef(Item):
    def __init__(self, chef_id:int, col:int, row:int):
        super().__init__(col, row)
        self.chef_id = chef_id
        self.direction = "DOWN"
        self.holding_item = None

    # Chef id property
    @property
    def chef_id(self):
        return self.__chef_id

    # Chef id setter  
    @chef_id.setter
    def chef_id(self, value:int):
        # Check if its an integer
        if not isinstance(value, int):
            raise TypeError("Chef ID must be an integer.")
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
        return self.holding_item is not None

    # Holding item property
    @property
    def holding_item(self):
        return self.__holding_item

    # Holding item setter
    @holding_item.setter
    def holding_item(self, value):
        if value is not None and not isinstance(value, Dish):
            raise TypeError("Holding item must be an instance of Dish or None.")
        self.__holding_item = value 
        
    # Movement restrictions
    def is_valid_move(self, next_col: int, next_row: int) -> bool:
        if not (MIN_COLUMNS<=next_col<=MAX_COLUMNS):
            return False

        if self.chef_id == 1 and not (CHEF_1_MIN_ROW <= next_row <= CHEF_1_MAX_ROW):
            return False
        if self.chef_id == 2 and not (CHEF_2_MIN_ROW <= next_row <= CHEF_2_MAX_ROW):
            return False
        
        
        target_element = KITCHEN_LAYOUT[next_row][next_col]
        if target_element != "FREE":
            return False

        return True

    # Move function
    def move(self, direction: str):
        self.direction = direction

        next_col = self.col
        next_row = self.row

        # Calculate next move
        if direction == "UP":
            next_row -= 1
        elif direction == "DOWN":
            next_row += 1
        elif direction == "LEFT":
            next_col -= 1
        elif direction == "RIGHT":
            next_col += 1

        # Actualize coordinates if possible
        if self.is_valid_move(next_col, next_row):
            self.col = next_col
            self.row = next_row

    # Calculate chef´s looking tile
    def get_target_tile(self) -> tuple[int,int]:
        target_col = self.col
        target_row = self.row

        if self.direction == "UP":
            target_row -= 1
        elif self.direction == "DOWN":
            target_row += 1
        elif self.direction == "LEFT":
            target_col -= 1
        elif self.direction == "RIGHT":
            target_col += 1

        return target_col, target_row
        
    # Get the facing element
    def get_facing_element(self) -> str:
        target_col, target_row = self.get_target_tile()

        if MIN_COLUMNS<= target_col <= MAX_COLUMNS and MIN_ROWS <= target_row <= MAX_ROWS:
            return KITCHEN_LAYOUT[target_row][target_col]
        
        return "OUT_OF_BOUNDS"
    
    # Interactions
    def interact(self, handovers: list):
      facing_element = self.get_facing_element()
      target_col, target_row = self.get_target_tile()

      # If facing handover
      if facing_element == "PASS":
        target_handover = None
        for ho in handovers:
          if ho.col == target_col and ho.row == target_row:
            target_handover = ho
            break

        if target_handover is not None:
          # Without dish and handover has a dish -> get dish
          if not self.has_dish:
            if not target_handover.is_empty():
              self.holding_item = target_handover.dish
              target_handover.dish = None
              print(
                  f"[DEBUG] Chef {self.chef_id} cogió un plato de PASS en"
                  f" ({target_col}, {target_row})."
              )
          # With dish and handover is free -> leave dish
          else:
            if target_handover.is_empty():
              target_handover.dish = self.holding_item
              self.holding_item = None
              print(
                  f"[DEBUG] Chef {self.chef_id} dejó un plato en PASS en"
                  f" ({target_col}, {target_row})."
              )

      # Empty hands
      elif not self.has_dish:
        # If facing plates and being second chef
        if facing_element == "PLATES" and self.chef_id == 2:
          self.holding_item = Dish()
          print(
              f"[DEBUG] Chef {self.chef_id} ha cogido un plato de la pila en"
              f" ({self.col}, {self.row})."
          )

      # Fully hands
      else:
        dish = self.holding_item

        # If facing ingredient
        if facing_element in ("TOMATO", "POTATO", "ONION", "CHORIZO", "EGG"):
          ing_name = facing_element.lower()
          new_ingredient = Ingredient(
              col=target_col, row=target_row, name=ing_name, state="raw"
          )
          dish.add_ingredient(new_ingredient)
          print(
              f"[DEBUG] Chef {self.chef_id} añadió '{ing_name}' al plato."
              f" Ingredientes en el plato: {dish.ingredients}"
          )

        # If  facing bin
        elif facing_element == "BIN":
          dish.clear()
          print(
              f"[DEBUG] Chef {self.chef_id} ha tirado el contenido al BIN."
              " Plato vacío."
          )

        # If facing board
        elif facing_element == "BOARD":
          dish.chop_ingredients()
          print(
              f"[DEBUG] Chef {self.chef_id} ha procesado (picado) los"
              " ingredientes en la tabla."
          )
        
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