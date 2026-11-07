import pyxel
from chef import Chef

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


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Service Rush", display_scale=3)
        
        self.__chef1 = Chef(chef_id=1, start_col=5, start_row=2)  
        self.__chef2 = Chef(chef_id=2, start_col=5, start_row=6) 

        self.__score = 0
        self.__failures = 0
        self.__timer_frames = SERVICE_DURATION_FRAMES

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.__timer_frames > 0:
            self.__timer_frames -= 1

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

        # Draw chefs
        self.__chef1.draw()
        self.__chef2.draw()

        # Draw score, failures, and timer
        total_sec = self.__timer_frames // FPS
        minutos = total_sec // 60
        segundos = total_sec % 60
        time_str = f"{minutos:02d}:{segundos:02d}"

        pyxel.text(2, 4, f"SCORE: {self.__score}", 7)        
        pyxel.text(2, 13, f"FAILURES: {self.__failures}/{MAX_FAILURES}", 7)
        pyxel.text(2, 22, f"TIME: {time_str}", 7)