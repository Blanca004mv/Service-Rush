# Global constants
SCREEN_WIDTH = 192
SCREEN_HEIGHT = 176
BOARD_HEIGHT = 32
KITCHEN_LAYOUT = [
    # Row 0: Upper cabinets
    ["ONION", "EGG", "CHORIZO", "FREE_WORK", "BOARD", "FREE_WORK", "BLENDER", "FREE_WORK", "FREE_WORK", "FREE_WORK", "FREE_WORK", "SERVE"],
    # Row 1: Chef´s floor
    ["FREE"] * 12,
    # Row 2: Chef´s floor
    ["FREE"] * 12,
    # Row 3: Chef´s floor
    ["FREE"] * 12,
    # Row 4: Division counter
    ["WALL", "PASS", "WALL", "PASS", "WALL", "BIN", "WALL", "PASS", "WALL", "SINK", "PASS", "WALL"],
    # Row 5: Chef´s floor
    ["FREE"] * 12,
    # Row 6: Chef´s floor
    ["FREE"] * 12,
    # Row 7: Chef´s floor
    ["FREE"] * 12,
    # Row 8: Lower cabinets
    ["TOMATO", "POTATO", "FREE_WORK", "FREE_WORK", "FREE_WORK", "BOARD", "FREE_WORK", "PAN", "FREE_WORK", "RETURN", "PLATES", "FREE_WORK"]
]

FPS = 30
SERVICE_DURATION_SEC = 180
SERVICE_DURATION_FRAMES = SERVICE_DURATION_SEC * FPS
MAX_FAILURES = 3

BOARD_MARGIN_RIGHT = 2
Y_SEPARATION = 9
SCORE_Y = 4
FAILURES_Y = SCORE_Y + Y_SEPARATION
TIMER_Y = FAILURES_Y + Y_SEPARATION

TEXT_COLOR = 7

RECIPES = {
    "GAZPACHO": {
        "ingredients": ("TOMATO_CHOPPED", "ONION_CHOPPED"),
        "equipment": "BLENDER",
        "points": 10,
        "time_limit": 48,
        "penalty": -5
    },
    "SPANISH_OMELETTE": {
        "ingredients": ("POTATO_CHOPPED", "ONION_CHOPPED", "EGG"),
        "equipment": "PAN",
        "points": 12,
        "time_limit": 60,
        "penalty": -6
    },
    "BROKEN_EGGS": {
        "ingredients": ("POTATO_CHOPPED", "EGG", "CHORIZO_CHOPPED"),
        "equipment": "PAN",
        "points": 12,
        "time_limit": 60,
        "penalty": -6
    }
}

# Position (u, v) of each sprite  16x16 in the images
SPRITES = {
    # Raw ingredients
    "tomato": (0, 16), "potato": (16, 16), "onion": (32, 16),
    "chorizo": (48, 16), "egg": (64, 16),
    # Chopped ingredients
    "tomato_chopped": (0, 32), "potato_chopped": (16, 32),
    "onion_chopped": (32, 32), "chorizo_chopped": (48, 32),
    # Plates
    "dish_empty": (0, 48), "gazpacho": (16, 48),
    "spanish_omelette": (32, 48), "broken_eggs": (48, 48),
    # Equipment
    "board": (0, 64), "blender": (16, 64), "pan": (32, 64),
    "plates": (48, 64), "bin": (64, 64),
    # Kitchen
    "serve": (0, 80), "worktop": (16, 80), "wall": (32, 80),
    "handover": (48, 80), "drawer": (64, 80),
    "sink": (0, 96), "return": (16, 96), "floor": (32, 96),
    # Optionals + special cases
    "dish_ruined": (64, 48),   
    "dish_dirty": (80, 48),    
    "stars_1": (48, 96), "stars_2": (64, 96), "stars_3": (80, 96),  # Sprint 5
    
}

CHEF_SPRITES = {
    1: {"front": (0, 0),   "back": (16, 0),   "side": (32, 0),
        "front_plate": (48, 0),   "back_plate": (64, 0),   "side_plate": (80, 0)},
    2: {"front": (0, 112), "back": (16, 112), "side": (32, 112),
        "front_plate": (48, 112), "back_plate": (64, 112), "side_plate": (80, 112)},
}

VALID_INGREDIENTS = ("tomato", "potato", "onion", "chorizo", "egg")
VALID_STATES = ("raw", "chopped", "blended", "cooked")

FIRST_ORDER_DELAY_SEC = 3       
ORDER_SPAWN_INTERVAL_SEC = 15
MAX_WAITING_ORDERS = 3

TICKET_WIDTH = 43           
TICKET_HEIGHT = 24          
TICKET_BG_COLOR = 3         
TICKET_TEXT_COLOR_NORMAL = 0 
TICKET_TEXT_COLOR_URGENT = 8 
TICKET_SPACING_X = 48       
TICKET_CRITICAL_TIME_SEC = 10
DISH_X_SPACING = 2
DISH_Y_SPACING = 4
SECONDS_LEFT_X_SPACING = 22
SECONDS_LEFT_Y_SPACING = 16
INGREDIENT_X_SPACING = 16
INGREDIENT_Y_SPACING = 2
INGREDIENT_SEPARATION = 7
INGREDIENTE_SCALE = 0.5
ITEM_SIZE = 16
ORDER_X = 4
ORDER_Y = 4
ORDER_SPACING = 47

MAX_COLUMNS = 11
MIN_COLUMNS = 0
MAX_ROWS = 8
MIN_ROWS = 0

CHEF_1_MAX_ROW = 3
CHEF_1_MIN_ROW = 1
CHEF_2_MAX_ROW = 7
CHEF_2_MIN_ROW = 5