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
    ["WALL", "PASS", "WALL", "PASS", "WALL", "BIN", "WALL", "PASS", "WALL", "WALL", "PASS", "WALL"],
    # Row 5: Chef´s floor
    ["FREE"] * 12,
    # Row 6: Chef´s floor
    ["FREE"] * 12,
    # Row 7: Chef´s floor
    ["FREE"] * 12,
    # Row 8: Lower cabinets
    ["TOMATO", "POTATO", "FREE_WORK", "FREE_WORK", "FREE_WORK", "BOARD", "FREE_WORK", "PAN", "FREE_WORK", "FREE_WORK", "PLATES", "FREE_WORK"]
]

FPS = 30
SERVICE_DURATION_SEC = 180
SERVICE_DURATION_FRAMES = SERVICE_DURATION_SEC * FPS
MAX_FAILURES = 3

SCORE_X = 135
SCORE_Y = 4

FAILURES_X = 135
FAILURES_Y = 13

TIMER_X = 135
TIMER_Y = 22

TEXT_COLOR = 7

RECIPES = {
    "GAZPACHO": {
        "ingredients": ("CHOPPED_TOMATO", "CHOPPED_ONION"),
        "equipment": "BLENDER",
        "points": 10,
        "time_limit": 48 * FPS,
        "penalty": -5
    },
    "SPANISH_OMELETTE": {
        "ingredients": ("CHOPPED_POTATO", "CHOPPED_ONION", "EGG"),
        "equipment": "PAN",
        "points": 12,
        "time_limit": 60 * FPS,
        "penalty": -6
    },
    "BROKEN_EGGS": {
        "ingredients": ("CHOPPED_POTATO", "EGG", "CHOPPED_CHORIZO"),
        "equipment": "PAN",
        "points": 12,
        "time_limit": 60 * FPS,
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
    "omelette": (32, 48), "broken_eggs": (48, 48),
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