import pyxel

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

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Service Rush", display_scale=3)
        pyxel.run(self.update, self.draw)


    def update(self):
        pass

    def draw(self):
        # Clear the screen with a white color
        pyxel.cls(7)

        # Draw service board
        pyxel.rect(0, 0, SCREEN_WIDTH, BOARD_HEIGHT, 0) 

        # Draw kitchen layout
        for row, row_item in enumerate(KITCHEN_LAYOUT):
            for col, item in enumerate(row_item):
                x = col * 16
                y = row * 16 + BOARD_HEIGHT
                if item == "FREE":
                    pyxel.rect(x, y, 16, 16, 7)  # White for free space
                elif item == "WALL":
                    pyxel.rect(x, y, 16, 16, 13)  # Grey for walls
                elif item == "PASS":
                    pyxel.rect(x, y, 16, 16, 10)  # Yellow for pass-through areas
                elif item == "BIN":
                    pyxel.rect(x, y, 16, 16, 8)  # Red gray for bin
                elif item == "FREE_WORK":
                    pyxel.rect(x, y, 16, 16, 4)  # Brown for free work areas
                else:
                    pyxel.rect(x, y, 16, 16, 11)  # Green for items